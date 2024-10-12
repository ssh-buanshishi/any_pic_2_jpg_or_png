from typing import Union
import os, sys, ctypes, win32pipe, win32file, win32api, win32con
import threading, time, psutil, subprocess, elevate, io
import func_timeout
import configparser
from copy import copy

# 程序所在文件夹
program_dir = os.path.dirname(__file__)
# 程序exe名
app_exe = os.path.basename(sys.argv[0])
# 对应启动的runner
target_runner = "any_pic_2_jpg_runner.exe"
# 当前登录的用户
current_user = os.getlogin()
# 是否是管理员
is_admin = bool(ctypes.WinDLL("shell32.dll").IsUserAnAdmin())

# 可能启动命名管道来传输启动命令行时，使用的管道参数
PIPE_NAME = '\\\\.\\pipe\\any_pic_2_filepath_data_transfer_pipe'
SELF_PIPE_NAME = '\\\\.\\pipe\\any_pic_2_starter_self_data_transfer_pipe'
PIPE_BUFFER_SIZE = 32768
connected = False
#file_handle = None
#wait_loop = True


## 默认配置文件
# 配置文件名
config_file = os.path.abspath(f"{program_dir}\\..\\配置.ini")
# 默认的配置文件放在与脚本同目录下的【my_custom_config_info.py】里了，
# 如果放在这的话，长度太长
from my_custom_config_info import default_config_content

## 日志文件配置
# 日志文件名
log_file = os.path.abspath(f"{program_dir}\\..\\运行日志.log")

## 图像输出配置
# 目标格式，供pillow保存时的“format=”选项使用
target_format = "JPEG"


# ===============   ★★★ 解析配置文件出错时，备用的默认配置 ★★★   ===============

## 弹窗行为管理配置
# 1.【弹窗总开关】
pop_window_main_switch = True

# 2.【单纯双击启动程序“any_pic_2_jpg.exe” / “to_jpg.bat”，
#    没有路径传入时，此程序对应的表现】
#
#   非负整数，可取值：0 | 1 | 2 | 3 | 4 | 5
#
#   0：弹窗提示后，打开 ⇨ 配置文件【配置.ini】供修改编辑。（新手提示）
#
#   1：不弹窗，直接打开 ⇨ 配置文件【配置.ini】供修改编辑。（熟悉后可改为这个）
#
#   2：弹窗提示后，打开 ⇨ 运行日志【运行日志.log】供查看。（2、3是补充备用的快捷方式）
#    
#   3：不弹窗，直接打开 ⇨ 运行日志【运行日志.log】供查看。
#
#
#
#   4：仅弹窗提醒，但不打开配置文件【配置.ini】和【运行日志.log】其中任何一个。
#
#   5：不弹窗，也不打开配置文件【配置.ini】和【运行日志.log】其中任何一个，
#      只在cmd终端留下“无路径传入”的提示。
to_jpg_exe_no_path_parameter_behavior = 1

# 3.【单纯双击启动程序“any_pic_2_png.exe” / “to_png.bat”，
#    没有路径传入时，此程序对应的表现】
# 与上面的2类似
to_png_exe_no_path_parameter_behavior = 5

# 5.【打开关键错误弹窗】
show_critical_error_window = True

# ===============   ★★★ 【结束行】解析配置文件出错时，备用的默认配置 ★★★   ===============



# 检查进程是否唯一
def has_one_more_process() -> bool:
    for proc in psutil.process_iter():
        if proc.name() in {"any_pic_2_jpg_runner.exe","any_pic_2_png_runner.exe"}:
            return True
    return False

# 在无管理员权限的情况下，使用通常写入方法覆盖配置文件
def overwrite_config_file_with_no_admin() -> None:
    with open(config_file , mode="wt" , encoding="utf-8-sig" , errors="replace" , newline="\r\n") as f:
        f.write(default_config_content)
    return


# 处理关键错误
def handle_critical_error(err_str:str) -> None:
    print(f"\n\n{err_str}")
    
    # 如果设置没有关，调用windows的API弹出错误窗口（有声音且醒目）
    if pop_window_main_switch and show_critical_error_window:
        # 单个确认按钮，错误❌图标，弹窗置顶，设置为前台的弹窗
        win32api.MessageBox(0 , err_str , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND) )
    
    print("\n\n==========     【已退出】     ==========\n\n")  

    sys.exit(0)


# 预分配磁盘空间的写入文件方式，能极大减少输出的文件碎片
# 此py脚本写入配置文件专用的函数
def pre_allocate_write_output_file(output_path:str , data:str , encoding="utf-8-sig") -> None:
    
    # 覆盖，不然fsutil会报错，不能创建
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except:
            raise Exception(f"文件【{output_path}】已存在且删除失败，无法预分配空间")
    
    
    if isinstance(data , str):
        data = "\r\n".join(data.splitlines()) # 换成CRLF
        data = data.encode(encoding=encoding , errors="replace")
        
        if (ret := os.system(f"fsutil file createNew \"{output_path}\" {len(data)} >nul")):
            raise Exception(f"无法给【{output_path}】预分配空间")
        
        with open(output_path,mode="br+",buffering=0) as f:
            f.write(data)
    
    else:
        raise Exception("第二个参数data类型错误")
    
    
    # 无返回值
    return


# 读取弹窗的设置
def read_pop_window_config() -> None:
    global pop_window_main_switch , show_critical_error_window
    global to_jpg_exe_no_path_parameter_behavior , to_png_exe_no_path_parameter_behavior

    # 尝试从系统环境变量中读取【弹窗总开关】和【打开关键错误弹窗】的设置
    pop_window_main_switch_got_os_environ = False
    show_critical_error_window_got_os_environ = False
    for k,v in os.environ.items():
        if (tmp := k.lower()) == "any_pic_2_pop_window_main_switch":
            if (tmp := v.lower()) in {'1', 'yes', 'true', 'on'}:
                pop_window_main_switch = True
                pop_window_main_switch_got_os_environ = True
            elif tmp in {'0', 'no', 'false', 'off'}:
                pop_window_main_switch = False
                pop_window_main_switch_got_os_environ = True
        elif tmp == "any_pic_2_show_critical_error_window":
            if (tmp := v.lower()) in {'1', 'yes', 'true', 'on'}:
                show_critical_error_window = True
                show_critical_error_window_got_os_environ = True
            elif tmp in {'0', 'no', 'false', 'off'}:
                show_critical_error_window = False
                show_critical_error_window_got_os_environ = True
    
    # 检查配置文件是否存在，是否要重置（空文件）
    # 准备好配置文件，方便下面直接双击编辑（无路径传入的处理）
    if not os.path.exists(config_file):
        try:
            if is_admin:
                pre_allocate_write_output_file(config_file , default_config_content , encoding="utf-8-sig")
            else:
                overwrite_config_file_with_no_admin()
        except Exception as e:
            handle_critical_error(f"配置文件不存在，且无法写出默认配置文件，\n详情：{e}，\n程序终止")
    
    elif os.path.getsize(config_file) < 32: # 空文件，重置
        try:
            if is_admin:
                pre_allocate_write_output_file(config_file , default_config_content , encoding="utf-8-sig")
            else:
                overwrite_config_file_with_no_admin()
        except Exception as e:
            handle_critical_error(f"无法重置空配置文件，\n详情：{e}，\n程序终止")
    
    
    # 读取和解析配置文件
    try:
        cfg = configparser.ConfigParser()
        with open(config_file ,mode="rt", encoding="utf-8-sig" , newline="\r\n") as f:
            cfg.read_file(f)
        
        
        ## [window_pop_behavior]
        # 1.【弹窗总开关】（系统变量优先）
        if not pop_window_main_switch_got_os_environ:
            try:
                tmp = cfg.getboolean(section="window_pop_behavior" , option="pop_window_main_switch")
            except:
                pass
            else:
                pop_window_main_switch = copy(tmp)
        
        # 2.【单纯双击启动程序“any_pic_2_jpg.exe” / “to_jpg.bat”，
        #    没有路径传入时，此程序对应的表现】
        try:
            tmp = cfg.getint(section="window_pop_behavior" , option="to_jpg_exe_no_path_parameter_behavior")
        except:
            pass
        else:
            if tmp in range(0,8):
                to_jpg_exe_no_path_parameter_behavior = copy(tmp)
        
        # 3.【单纯双击启动程序“any_pic_2_png.exe” / “to_png.bat”，
        #    没有路径传入时，此程序对应的表现】
        try:
            tmp = cfg.getint(section="window_pop_behavior" , option="to_png_exe_no_path_parameter_behavior")
        except:
            pass
        else:
            if tmp in range(0,8):
                to_png_exe_no_path_parameter_behavior = copy(tmp)
        
        # 5.【打开关键错误弹窗】（系统变量优先）
        if not show_critical_error_window_got_os_environ:
            try:
                tmp = cfg.getboolean(section="window_pop_behavior" , option="show_critical_error_window")
            except:
                pass
            else:
                show_critical_error_window = copy(tmp)
    
    except:
        try:
            del cfg #释放些内存
        except:
            pass
        
        # 出错时，如遇到乱七八糟的字符“%()”啥的，尝试覆盖
        try:
            if is_admin:
                pre_allocate_write_output_file(config_file , default_config_content , encoding="utf-8-sig")
            else:
                overwrite_config_file_with_no_admin()
        except:
            handle_critical_error("解析配置文件遇到重大错误，\n尝试覆盖配置文件，却失败，\n程序终止")
    
    else:
        del cfg #释放些内存



# 处理无路径传入
def handle_no_path_in() -> None:
    
    if target_format=="JPEG":
        
        if pop_window_main_switch and to_jpg_exe_no_path_parameter_behavior:
            
            if to_jpg_exe_no_path_parameter_behavior == 1:
                # 1：弹窗提示后，打开配置文件 ⇨ 【配置.ini】供修改编辑。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开配置文件 ⇨ 【配置.ini】 供修改编辑" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if os.path.exists(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 2:
                # 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。
                if os.path.exists(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 3:
                # 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                # 【此函数不操作log_file，所以直接打开】
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开运行日志 ⇨ 【运行日志.log】 供查看" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if os.path.exists(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 4:
                # 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看。
                # 【此函数不操作log_file，所以直接打开】
                if os.path.exists(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 5:
                # 5：弹窗提示后，打开【软件所在目录】。
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开【软件所在目录】" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_jpg_exe_no_path_parameter_behavior == 6:
                # 6：不弹窗，直接打开【软件所在目录】。
                os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_jpg_exe_no_path_parameter_behavior == 7:
                # 7：仅弹窗提醒，但不打开配置文件【配置.ini】、【运行日志.log】和【软件所在目录】其中任何一个。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                win32api.MessageBox(0 , "无路径传入，根据设置，\n接下来，配置文件、运行日志，\n以及软件所在目录，都不会被打开" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
    
    elif target_format=="PNG":
        
        if pop_window_main_switch and to_png_exe_no_path_parameter_behavior:
            
            if to_png_exe_no_path_parameter_behavior == 1:
                # 1：弹窗提示后，打开配置文件 ⇨ 【配置.ini】供修改编辑。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开配置文件 ⇨ 【配置.ini】 供修改编辑" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if os.path.exists(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 2:
                # 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。
                if os.path.exists(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 3:
                # 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                # 【此函数不操作log_file，所以直接打开】
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开运行日志 ⇨ 【运行日志.log】 供查看" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if os.path.exists(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 4:
                # 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看。
                # 【此函数不操作log_file，所以直接打开】
                if os.path.exists(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 5:
                # 5：弹窗提示后，打开【软件所在目录】。
                win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开【软件所在目录】" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_png_exe_no_path_parameter_behavior == 6:
                # 6：不弹窗，直接打开【软件所在目录】。
                os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_png_exe_no_path_parameter_behavior == 7:
                # 7：仅弹窗提醒，但不打开配置文件【配置.ini】、【运行日志.log】和【软件所在目录】其中任何一个。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                win32api.MessageBox(0 , "无路径传入，根据设置，\n接下来，配置文件、运行日志，\n以及软件所在目录，都不会被打开" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
    
    
    sys.exit(0)



# 等待自身接收并传送
def wait_self_connect_and_transfer() -> None:
    # 编码数据到bytes
    input_data = ("\n".join(file_args)).encode(encoding="utf-8",errors="replace")
    # 包装为BytesIO
    input_data = io.BytesIO(input_data)
    
    # 创建管道并等待连接
    named_pipe = win32pipe.CreateNamedPipe(
        SELF_PIPE_NAME,
        win32pipe.PIPE_ACCESS_OUTBOUND | win32pipe.FILE_FLAG_FIRST_PIPE_INSTANCE,
        win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT | win32pipe.PIPE_READMODE_BYTE,
        1,#win32pipe.PIPE_UNLIMITED_INSTANCES,
        PIPE_BUFFER_SIZE,
        PIPE_BUFFER_SIZE, 500, None
    )
    win32pipe.ConnectNamedPipe(named_pipe, None)

    try:
        with input_data:
            while buf := input_data.read(PIPE_BUFFER_SIZE):
                win32file.WriteFile(named_pipe , buf , None)
    except:
        pass
    # 写完就关，接受端捕捉到管道关闭的出错就会停止
    win32api.CloseHandle(named_pipe)

    return


# 尝试获取来自自身创建的管道
def try_get_self_pipe() -> Union[list,None]:
    data_collecter = bytearray()

    retry_time = 0
    file_handle = None
    while retry_time < 3:
        try:
            file_handle = win32file.CreateFile(
                SELF_PIPE_NAME,
                win32file.GENERIC_READ,
                0,
                None,
                win32file.OPEN_EXISTING,
                win32file.FILE_ATTRIBUTE_NORMAL,
                None,
            )
            break
        except:
            retry_time += 1
            time.sleep(0.1)
    
    if file_handle:
        # 读取
        while True:
            try:
                buf = win32file.ReadFile(file_handle, PIPE_BUFFER_SIZE, None)[-1]
                if buf:
                    data_collecter.extend(buf)
                else:
                    break
            except:
                break
        # 解码管道内传来的bytes
        decoded_string = data_collecter.decode(encoding="utf-8" , errors="replace")
        cmd_list = decoded_string.split("\n")
        return cmd_list
    else:
        return None




# 等待接收端(client端)连接读取
def wait_connect() -> None:
    global connected , named_pipe
    
    def worker() -> None:
        global connected , named_pipe
        
        named_pipe = win32pipe.CreateNamedPipe(
            PIPE_NAME,
            win32pipe.PIPE_ACCESS_OUTBOUND | win32pipe.FILE_FLAG_FIRST_PIPE_INSTANCE,
            win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT | win32pipe.PIPE_READMODE_BYTE,
            1,#win32pipe.PIPE_UNLIMITED_INSTANCES,
            PIPE_BUFFER_SIZE,
            PIPE_BUFFER_SIZE, 500, None
        )
        win32pipe.ConnectNamedPipe(named_pipe, None)
        connected = True
        
        return
    
    try:
        func_timeout.func_timeout(8 , worker)
    except:
        connected = False
        os.system("cls")
        handle_critical_error("接收管道准备超时\n可能【any_pic_2_skip_UAC.exe】未启动\n程序终止")
    
    return



# 与runner一起结束，方便编写批处理时阻塞cmd，
# 否则cmd将直接运行“any_pic_2_xxx”的下一条命令，从而可能发生意想不到的情况
def wait_runner_end() -> None:
    start_wait_time = time.time()
    # 等待启动
    while time.time() - start_wait_time < 12:
        if target_runner in {i.name() for i in psutil.process_iter()}:
            break
        time.sleep(0.1)
    # 等待结束
    while target_runner in {i.name() for i in psutil.process_iter()}:
        time.sleep(1)
    
    return


'''
        ........       .......                    .....                                                       
        =@@@@@@@.     ,@@@@@@@                    =@@@@                                                       
        =@@@@@@@^     /@@@@@@@                    =@@@@                                                       
        =@@@@@@@@.   =@@@@@@@@      .]]]]]]`              .]]]`  ,]]]].                                       
        =@@@@=@@@^   @@@@=@@@@    /@@@@@@@@@@@.   =@@@@   =@@@@/@@@@@@@@`                                     
        =@@@@.@@@@. =@@@^=@@@@   /@@@/` .,@@@@^   =@@@@   =@@@@@/. ,@@@@@.                                    
        =@@@@.=@@@\ @@@@.=@@@@          ,]/@@@@   =@@@@   =@@@@^    =@@@@.         ,]]]]]]]]]]]]]]]]]]]`      
        =@@@@. @@@@/@@@^ =@@@@    ,@@@@@@@@@@@@   =@@@@   =@@@@.    =@@@@.         \@@@@@@@@@@@@@@@@@@@@.     
        =@@@@. =@@@@@@@. =@@@@  .@@@@@/[`.=@@@/   =@@@@   =@@@@.    =@@@@.                           =@@^     
        =@@@@.  @@@@@@^  =@@@@  =@@@@`   ,@@@@\   =@@@@   =@@@@.    =@@@@.                           =@@^     
        =@@@@.  =@@@@@.  =@@@@   \@@@@@@@@@@@@@   =@@@@   =@@@@.    =@@@@.                        @@@@@@@@@@  
        ,@@@@.   @@@@/   =@@@@    ,\@@@@[` \@@@^  =@@@O   ,@@@@.    ,@@@@.                        ,@@@@@@@@`  
                                                                                                   =@@@@@@^   
                                                                                                    @@@@@@    
                                                                                                    .@@@@^    
                                                                                                     =@@/     
                                                                                                      \@.     
                                                                                                       `      
'''

os.system("title ★【any_pic_2_jpg】启动器★")
read_pop_window_config()
# 如果没有路径传入，按照设置打开快捷方式，然后退出
if len(sys.argv) < 2:
    handle_no_path_in()

# 检查进程多开冲突
if has_one_more_process():
    handle_critical_error("进程多开错误，同一时间仅允许运行一个进程")

# 先尝试连接自身的管道
if (tmp := try_get_self_pipe()) != None:
    args_from_pipe = True
    file_args = tmp
# 如果没连接到，说明是第一次启动
else:
    args_from_pipe = False
    # 趁还在图片目标路径下（从图片目标路径启动cmd时），收集处理目标的绝对路径
    file_args = [os.path.abspath(i) for i in sys.argv]
    # 抛掉开头1～2个启动器自身的exe，2个的情况是elevate过后，
    # 已提权进程内接受到的sys.argv
    while file_args and (os.path.basename(file_args[0]) == app_exe):
        file_args.pop(0)
    # 配齐启动runner的命令
    file_args.insert(0 , target_runner)


# 来到程序所在文件夹，方便启动命令
os.chdir(program_dir)


# 如果已经是admin权限了（登录用户为Administrator）
if is_admin:
    subprocess.run(args=file_args,shell=True)
    sys.exit(0)
# 已经是子进程了，却依旧没有取得管理员权限
elif args_from_pipe:
    handle_critical_error("未预料到的：子进程权限提升失败")
# 第一次启动，没有管理员权限
else:
    # 如果启动跳过UAC的计划任务失败（返回非0）
    # 就提升启动器自己的权限，此时弹出UAC窗口，允许后此程序重启（启动子进程），
    # 走上方的【如果已经是admin权限了……】分支，
    # 子进程完成后，返回这里退出
    if ( ret := os.system(f"schtasks /Run /TN \"any_pic_2_skip_UAC_for_user--{current_user}\" >nul 2>nul") ):
        # 创建管道并等待传送
        t = threading.Thread(target=wait_self_connect_and_transfer , daemon=True)
        t.start()
        
        try:
            elevate.elevate()
        except:
            handle_critical_error("程序运行需要管理员权限，但似乎被拒绝了")
        # elevate因为被修改了，提升权限完成后要立刻退出，
        # 否则会以【非管理员】的方式执行之后的指令
        # 这里【之后的指令】跟的就是本脚本最后一行“sys.exit(0)”，所以其实不写也没关系
        # 不过为了醒目，还是加上去了
        sys.exit(0)
    
    # 如果成功，用管道传输启动指令
    else:
        # 编码数据到bytes
        input_data = ("\n".join(file_args)).encode(encoding="utf-8",errors="replace")
        # 包装为BytesIO
        input_data = io.BytesIO(input_data)

        print("向替升权限后的进程传送目标路径中，\n如超过10秒无反应，请手动右上角关闭此窗口，或按Ctrl+C终止")
        
        # 等待管道连接
        wait_connect()
        os.system("cls")
        
        # 如果管道准备好了，写入数据
        if connected:
            print("程序运行中，请等待")
            
            try:
                with input_data:
                    while buf := input_data.read(PIPE_BUFFER_SIZE):
                        win32file.WriteFile(named_pipe , buf , None)
                # 写完就关，接受端捕捉到管道关闭的出错就会停止
                win32api.CloseHandle(named_pipe)
                
                # 等待runner进程结束
                wait_runner_end()
            except:
                pass

            # 结束计划任务
            os.system(f"schtasks /End /TN \"any_pic_2_skip_UAC_for_user--{current_user}\" >nul 2>nul")
        
        sys.exit(0)

sys.exit(0)