# ==================  快速响应无路径输入的情况  ==================
#
import os,sys,configparser,msvcrt,io
from contextlib import suppress
from copy import copy
import psutil,win32file,win32api,win32con
from my_custom_config_info import default_config_content

#显示并记录
def log(content:str) -> None:
    print(content,file=log_handle)
    print(content)
    return

# 处理关键错误
def handle_critical_error(err_str:str , log_handle_present:bool=True) -> None:
    # 在终端、日志里输出错误信息
    if log_handle_present:
        log(f"\n\n{err_str}")
    else:
        print(f"\n\n{err_str}")
    
    # 如果设置没有关，调用windows的API弹出错误窗口（有声音且醒目）
    if pop_window_main_switch and show_critical_error_window:
        # 单个确认按钮，错误❌图标，弹窗置顶，设置为前台的弹窗
        win32api.MessageBox(0 , err_str , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND) )
    
    if log_handle_present:
        global log_handle
        with suppress(Exception): log("\n\n==========     【已退出】     ==========\n\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝"+"\n"*15)
        with suppress(Exception): log_handle.close()
        with suppress(Exception): concat_log()
    
    else:
        print("\n\n==========     【已退出】     ==========\n\n")
    

    sys.exit(0)


# 处理无路径传入
def handle_no_path_in() -> None:
    
    if target_format=="JPEG":
        
        if pop_window_main_switch and to_jpg_exe_no_path_parameter_behavior:
            
            if to_jpg_exe_no_path_parameter_behavior == 1:
                # 1：弹窗提示后，打开配置文件 ⇨ 【配置.ini】供修改编辑。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开配置文件 ⇨ 【配置.ini】 供修改编辑" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL) and os.path.isfile(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 2:
                # 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。
                if os.path.isfile(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 3:
                # 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                # 【此函数不操作log_file，所以直接打开】
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开运行日志 ⇨ 【运行日志.log】 供查看" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL) and os.path.isfile(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 4:
                # 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看。
                # 【此函数不操作log_file，所以直接打开】
                if os.path.isfile(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_jpg_exe_no_path_parameter_behavior == 5:
                # 5：弹窗提示后，打开【软件所在目录】。
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开【软件所在目录】" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL):
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
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开配置文件 ⇨ 【配置.ini】 供修改编辑" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL) and os.path.isfile(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 2:
                # 2：不弹窗，直接打开配置文件 ⇨ 【配置.ini】供修改编辑。
                if os.path.isfile(config_file):
                    os.system(f"start \"title\" notepad \"{config_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 3:
                # 3：弹窗提示后，打开运行日志 ⇨ 【运行日志.log】供查看。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                # 【此函数不操作log_file，所以直接打开】
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开运行日志 ⇨ 【运行日志.log】 供查看" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL) and os.path.isfile(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 4:
                # 4：不弹窗，直接打开运行日志 ⇨ 【运行日志.log】供查看。
                # 【此函数不操作log_file，所以直接打开】
                if os.path.isfile(log_file):
                    os.system(f"start \"title\" notepad \"{log_file}\"")
            elif to_png_exe_no_path_parameter_behavior == 5:
                # 5：弹窗提示后，打开【软件所在目录】。
                ret = win32api.MessageBox(0 , "无路径传入，即将根据设置，\n打开【软件所在目录】" , app_exe , (win32con.MB_OKCANCEL | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
                if (ret != win32con.IDCANCEL):
                    os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_png_exe_no_path_parameter_behavior == 6:
                # 6：不弹窗，直接打开【软件所在目录】。
                os.system(f"start \"title\" explorer \"{program_dir}\\..\"")
            elif to_png_exe_no_path_parameter_behavior == 7:
                # 7：仅弹窗提醒，但不打开配置文件【配置.ini】、【运行日志.log】和【软件所在目录】其中任何一个。
                # 单个确认按钮，警告⚠图标，弹窗置顶，设置为前台的弹窗
                win32api.MessageBox(0 , "无路径传入，根据设置，\n接下来，配置文件、运行日志，\n以及软件所在目录，都不会被打开" , app_exe , (win32con.MB_OK | win32con.MB_ICONWARNING | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
    
    
    sys.exit(0)


# Windows上创建文件时进行空间预分配，使之具有连续非碎片化空间
def win_preallocate_newfile(
    # 日常使用参数
    file:str, size:int, exist_ok:bool=False,
    buffering:int=-1,
    text_mode:bool=False, encoding:str="utf-8-sig", 
    errors=None, newline="\r\n",
) -> io.BytesIO:

    # 分区名
    drive_name = os.path.splitdrive(os.path.abspath(file))[0] + "\\"
    # 文件系统
    fs_type = tmp if ( tmp := (fs_info_dict.get(drive_name))[0] ) else ""
    new_fs = True if (fs_type in {"NTFS","ReFS"}) else False
    # 簇大小
    cluster_size = tmp if ( tmp := (fs_info_dict.get(drive_name))[-1] ) else 1
    # 与簇大小对齐的文件分配空间
    al_size = (size + (cluster_size - remain_size)) if (remain_size := size%cluster_size) else size

    # 检查文件是否已经存在
    if os.path.isfile(file) and (not exist_ok):
        raise Exception("文件已存在，且未设置覆盖")
    
    
    # 上面为止文件都没有正式打开
    # 下面套个try是为了方便在失败时关掉句柄和删除残留
    try:
        # 打开一个python文件句柄
        if text_mode:
            py_fh = open(file, mode="wt+", encoding=encoding, buffering=buffering, errors=errors, newline=newline)
        else:
            py_fh = open(file, mode="wb+", buffering=buffering)
        
        # 转换为windows的句柄方便操作
        win_hf = msvcrt.get_osfhandle(py_fh.fileno())
        
        # 设置文件的磁盘分配空间
        win32file.SetFileInformationByHandle(win_hf , win32file.FileAllocationInfo , al_size)
        
        # 根据上面的配置结果，选择是否在一开始就移动EOF至文件的分配大小
        if new_fs:
            # 移动EOF至分配的文件大小
            # 虽然EOF的大小（文件大小）不需要对齐簇大小，
            # 不过这里设置成对齐簇大小的al_size，多一丢丢文件的实际大小，问题也不大
            win32file.SetFileInformationByHandle(win_hf , win32file.FileEndOfFileInfo , al_size)

    except Exception as x:
        e = copy(x) # 如果不找个新变量copy过来，下面的with suppress(Exception)会使存储异常的变量“人间蒸发”
        with suppress(Exception): py_fh.close()
        with suppress(Exception): os.remove(file)
        raise e
    
    return py_fh 


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

# 4.【打开处理完毕时的弹窗】
show_finish_window = True

# 5.【打开关键错误弹窗】
show_critical_error_window = True

# ===============   ★★★ 【结束行】解析配置文件出错时，备用的默认配置 ★★★   ===============



# 程序自身所在的文件夹，和程序的名字
# 程序自身所在的文件夹为脚本或者exe所在目录，记录为program_dir，定位到处理目标处理完后，还要返回来
program_dir = os.path.dirname(__file__)
app_exe = os.path.basename(sys.argv[0])
# 配置文件名
config_file = os.path.abspath(f"{program_dir}\\..\\配置.ini")
# 日志文件名
log_file = os.path.abspath(f"{program_dir}\\..\\运行日志.log")

## 图像输出配置
# 目标扩展名
target_ext = "png"
# 目标格式，供pillow保存时的“format=”选项使用
target_format = "PNG"

# 存放文件系统和磁盘类型
fs_info_dict = dict()
# 获取分区（包括网络磁盘、虚拟挂载磁盘）的文件系统信息，为后面的硬链接功能的条件判断做准备
for partition in psutil.disk_partitions(all=True):
    section = getattr(partition,"mountpoint","") # 盘符
    fs_type = getattr(partition,"fstype","") # 文件系统类型
    try:
        # 获取每扇区字节数，和每簇的扇区数
        sectors_per_cluster , bytes_per_sector , _ ,_ =win32file.GetDiskFreeSpace(section)
    except:
        cluster_size = 0
    else:
        # 相乘得到簇大小
        cluster_size = bytes_per_sector * sectors_per_cluster
    
    fs_info_dict[copy(section)] = (copy(fs_type) , copy(cluster_size))

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
if not os.path.isfile(config_file):
    try:
        with win_preallocate_newfile(config_file , 32*1024 , exist_ok=True , text_mode=True ,errors="replace") as f:
            f.write(default_config_content)
            f.truncate()
    except Exception as e:
        handle_critical_error(f"配置文件不存在，且无法写出默认配置文件，\n详情：{e}，\n程序终止" , log_handle_present=False)

elif ((config_file_size:=os.path.getsize(config_file)) < 32) or (config_file_size > 1024**2): # 空文件或文件大小大于1 MiB（不正常），重置
    try:
        with win_preallocate_newfile(config_file , 32*1024 , exist_ok=True , text_mode=True ,errors="replace") as f:
            f.write(default_config_content)
            f.truncate()
    except Exception as e:
        handle_critical_error(f"无法重置空配置文件，\n详情：{e}，\n程序终止" , log_handle_present=False)

# 读取和解析配置文件中的部分关键信息
try:
    cfg = configparser.ConfigParser()
    with open(config_file ,mode="rt", encoding="utf-8-sig" , newline="\r\n") as f:
        cfg.read_file(f)
except:
    # 出错时，如遇到乱七八糟的字符“%()”啥的，尝试覆盖
    try:
        with win_preallocate_newfile(config_file , 32*1024 , exist_ok=True , text_mode=True ,errors="replace") as f:
            f.write(default_config_content)
            f.truncate()
    except:
        handle_critical_error("解析配置文件遇到重大错误，\n尝试覆盖配置文件，却失败，\n程序终止" , log_handle_present=False)
    
    
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

# 4.【打开处理完毕时的弹窗】
try:
    tmp = cfg.getboolean(section="window_pop_behavior" , option="show_finish_window")
except:
    pass
else:
    show_finish_window = copy(tmp)

# 5.【打开关键错误弹窗】（系统变量优先）
if not show_critical_error_window_got_os_environ:
    try:
        tmp = cfg.getboolean(section="window_pop_behavior" , option="show_critical_error_window")
    except:
        pass
    else:
        show_critical_error_window = copy(tmp)

if len(sys.argv) < 2:
    handle_no_path_in()







# ==================  继续加载剩余的库和函数  ==================
#
# 代码注释库
from typing import Union , Optional
# 基础库
import ctypes, shutil, datetime, time, locale #os,sys,msvcrt
# from contextlib import suppress
import threading, mmap, re, subprocess #io
#from copy import copy
# 配置文件读取，与检测文件类型的库
import filetype #,configparser
# 弹小窗的库
import tkinter
# 一些调用windows系统dll需要的库
import win32gui, win32print # win32file, win32api, win32con,
# 硬件检测的库
#import psutil

# 代码源自“better_zipfile”库（https://pypi.org/project/better-zipfile/  ， https://github.com/aplmikex/better_zipfile/blob/main/better_zipfile/fixcharset_zipfile.py），
# 自己稍作修改，放在与脚本同目录下的【my_custom_zipfile.py】
#
# 可以有效防止解析压缩包时，以及解压时，中文文件名出现乱码，
# 虽然说livp的zip压缩包里面全是英文名文件，但是觉得还是得事先准备准备
#
# 使用这个库需提前安装：【charset-mnbvc】，版本大于等于0.0.12
# 
# 用下面这句import之后，用法和原本python自带的zipfile无差别
import my_custom_zipfile as zipfile

## 图像库和插件
# 处理raw图像的库
import rawpy
# 转换SVG的库
import cairosvg
# 处理PSD图像的库
from psd_tools import PSDImage
# 读取PDF的库，以及用于PDF中图片去重（多个xref指向同一个图片的数据）的crc32校验库
import pymupdf, crc32c
# Pillow
from PIL import Image , ImageOps
# 挂在Pillow上的jpls（JPEG-LS,JPEG-Lossless）编解码插件（https://pypi.org/project/pillow-jpls/）
# PS：战未来的“屠龙宝刀”😅
import pillow_jpls
# 挂在Pillow上的heic、avif编解码插件（https://pypi.org/project/pillow-heif/）
from pillow_heif import register_heif_opener, register_avif_opener
register_heif_opener(
    # 参见：https://pillow-heif.readthedocs.io/en/latest/options.html
    quality=-1,
    thumbnails=False,
    save_to_12bit=True,
    allow_incorrect_headers=True,
)
register_avif_opener(
    # 参见：https://pillow-heif.readthedocs.io/en/latest/options.html
    quality=-1,
    thumbnails=False,
    save_to_12bit=True,
    allow_incorrect_headers=True,
)



# 程序自身所在的文件夹，和程序的名字
# 程序自身所在的文件夹为脚本或者exe所在目录，记录为program_dir，定位到处理目标处理完后，还要返回来
# program_dir = os.path.dirname(__file__)
# app_exe = os.path.basename(sys.argv[0])
# cmd终端使用的默认推荐编码
cmd_encoding = locale.getpreferredencoding()


# 告诉操作系统使用程序自身的dpi适配
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    try:
        ctypes.windll.User32.SetProcessDPIAware()
    except:
        pass
# 获取屏幕的缩放比例
hDC = win32gui.GetDC(0)
dpi1 = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
dpi2 = win32print.GetDeviceCaps(hDC, win32con.HORZRES)
scale_factor = int(round(dpi1/dpi2 , 2) * 100)


# 展示打赏信息的py，位于与脚本同目录下的【my_sponsor_info.py】
#
# 为了不让某些二道贩子轻易替换打赏信息，让我给他们数钱，
# 此py文件里的show_sponsor_info()函数，
# 在分享出去的源码里是空的，请各位理解一下。
# 毕竟所有的核心转换功能的源码我都免费分享出去了。
#
# 我也并不能阻止有实力的人，在我分享出去的源码里，
# 稍微改动下加上自己的收款码赚钱，或者通过逆向等手段强行替换打赏信息。
# 就如“防君子不防小人”，
# 如果想用我的程序或者源码赚点钱，只要是想，终究防不住的。
#
# 不过我这边最起码的防范措施还是得做一下。
#
# 希望那些准备拿来我的源代码吃饭的人，到时候能有点人性，
# 人在做天在看，钱我不指望你能分我，最起码的注明原作者信息什么的工作你得做好
# 
from my_sponsor_info import show_sponsor_info







### 配置

## 默认配置文件
# 配置文件名
# config_file = os.path.abspath(f"{program_dir}\\..\\配置.ini")
# 默认的配置文件放在与脚本同目录下的【my_custom_config_info.py】里了，
# 如果放在这的话，长度太长
#from my_custom_config_info import default_config_content

## 日志文件配置
# 日志文件名
#log_file = os.path.abspath(f"{program_dir}\\..\\运行日志.log")
# 暂时存放本次运行的日志，运行结尾会跟之前的合并，方便把最新的记录放在文件最前面
tmp_log_file = os.path.abspath(f"{program_dir}\\..\\tmp.log")

## 输出前后缀设置
# 输入为文件夹时，输出文件夹的前缀（文件夹的目录结构，以及其中输出的文件名保持不变）
setted_output_prefix = "【输出】"
# 输入为单文件时，输出文件的后缀，“【输出】”两字加在前面比较丑
single_file_output_suffix = ".output"

'''
##保留的参数
# 本来打算放出错的文件的，想想还是先通过看日志确定哪些出错吧，
# 毕竟还原目录结构的话，出错文件只有一两个的话，找起来比较麻烦
setted_error_prefix = "【出错】"
'''

## 单图片输入限制大小：2 GiB（2 × 1024^3 字节）
# 根据pillow文档来的，实际上文档的意思估计是图片完全加载好后，所占用的内存限制
# 虽然图片加载前的尺寸可以大于或小于这个值，但还是设置为 2 GiB 比较保守吧
filesize_limit = 2 * (1024**3)




# ===============   ★★★ 解析配置文件出错时，备用的默认配置 ★★★   ===============
"""
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

# 4.【打开处理完毕时的弹窗】
show_finish_window = True

# 5.【打开关键错误弹窗】
show_critical_error_window = True
"""



## 文件夹转移方法配置
# 6.【复制策略】
# 输入为文件夹时，其中文件出错或跳过时的复制策略
# 非负整数，可取值：0|1|2
#     0：默认，先尝试硬链接，不行再拷贝
#     1：只用拷贝
#     2：只用硬链接
copy_method = 0


# 7.【输出的jpg图片质量】
# 正整数，取值范围：(0-100]，左开右闭（质量为0的jpg我觉得有点危险）
jpg_quality = 98
# pillow文档里推荐的是95，再往上也不是不可以，不过文件大小估计会显著增大，因为会禁用一些压缩算法
# 不过处理速度因此明显变快，我这边测试选取的是98，98比95明显快些
# 需要高质量输出的场景下，可以改为100。
# 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-saving

# 8.【jpg子采样选项】
# 非负整数，可取值：0|1|2 ，其所代表含义如下所示
#     0：4:4:4
#     1：4:2:2
#     2：4:2:0
jpg_subsample_option = 0
#这边测试由1到0的尺寸增加不大，为了色彩，推荐选择“0”
# 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#jpeg-saving

# 9.【png无损压缩（zip）的等级】
# 非负整数，取值范围：[0-9]，双闭区间
# 压缩前后数据都是无损的，数字越高，zip压缩等级越高，耗时间和CPU越高，
# 注意！数值为0时不压缩，输出的文件非常大！不推荐！
png_compress_level = 1
# 自己测试过，compress_level在0-1变化过程中文件显著变小，0是不压缩的，1是无损急速压缩，
# 数字再往上文件尺寸减少的量级几乎可以忽略，而且速度越来越慢，还不如用1快速，
# 毕竟现在很少在乎这么点图片文件尺寸的大小了，而且还要图片是无损的。
# 说明参见：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving


## 格式选择配置

# 10.【用户自定义排除的格式】
# 这边默认排除掉一些常见的、能轻松打开的图像格式
user_defined_excluded_format_set = {"JPEG" , "PNG" , "BMP" , "ICO" , "PSD"}

# 11.【排除已经是目标格式的文件】
exclude_target_format = True

# 12.【是否转换RAW图片】
convert_raw  = True


# 13.【是否转换苹果LIVP动态照片】
convert_livp = True
# 14.【苹果LIVP动态照片直接输出，不转换】
livp_direct_output = False


# 15.【是否转换华为动态照片】
convert_hwlp = True
# 16.【华为动态照片直接输出，不转换】
hwlp_direct_output = True


# 17.【是否转换PDF】
convert_pdf = True
# 18.【PDF转换模式】
#     0:默认，导出PDF中嵌入的图片，和PDF整个页面的渲染图
#     1:仅导出PDF中嵌入的图片
#     2:仅导出整个页面的渲染图
pdf_mode = 0
# 19.【PDF内嵌图片直接输出】
pdf_inside_pic_direct_output = True
# 20.【PDF页面渲染图缩放比例】（浮点数）
pdf_page_render_zoom_ratio = 2.0


# 21.【是否转换SVG】
convert_svg = True
# 22.【SVG转换后直接输出PNG】
svg_direct_output_png = True


# 23.【是否转换微信加密的dat图片】
convert_wechat_dat = True
# 24.【微信dat图片解密后直接输出，不转换】
wechat_dat_direct_output = True


## exif设置
# 25.【转换时是否保留RAW图片的exif】
perserve_raw_pic_exif = False
# 26.【转换时是否保留普通图片的exif】
perserve_common_pic_exif = True
# 27.【转换时是否使用exiftool额外增强保存一次exif】
exif_enhance = False
# 28.【调用exiftool后，是否整理覆写产生的磁盘碎片】
# 此项设置已作废
#   0:默认
#   1:总是
#   2:从不
#defrag_after_exiftool = 0



## 拷贝缓冲区大小设置和日志文件预分配大小
# 29.【拷贝文件的内存缓冲区大小】
# 正整数，单位：字节，配置文件输入单位：MiB
copy_file_buffer_size = 256*1024**2
# 30.【给日志文件预分配的空间】
# 正整数，单位：字节，配置文件输入单位：MiB
log_file_allocate_size = 10*1024**2


# ===============   ★★★ 【结束行】解析配置文件出错时，备用的默认配置 ★★★   ===============




# Pillow支持的格式
supported_format_set = {
    "AVIF" , "BLP" , "BMP" ,
    "BUFR" , "CUR" , "DCX" ,
    "DDS" , "DIB" , "EPS" ,
    "FITS" , "FLI" , "FTEX" ,
    "GBR" , "GIF" , "GRIB" ,
    "HDF5" , "HEIF" , "ICNS" ,
    "ICO" , "IM" , "IMT" ,
    "IPTC" , "JPEG" , "JPEG-LS" ,
    "JPEG2000" , "MCIDAS" , "MPEG" ,
    "MSP" , "PCD" , "PCX" , "PIXAR" ,
    "PNG" , "PPM" , "PSD" , "QOI" ,
    "SGI" , "SPIDER" , "SUN" , "TGA" ,
    "TIFF" , "WEBP" , "WMF" , "XBM" ,
    "XPM" , "XVTHUMB" ,
}

# 额外支持的文件偏移量特征
# 参考于：https://www.garykessler.net/library/file_sigs.html
ex_File_Signatures_dict = \
{
    "image/eps-1" : 
    (
        (0 , os.SEEK_SET) ,

        b"%!PS-Adobe-3.0 EPSF-3.0"
    ),
    
    "image/eps-2" :
    (
        (0x1e , os.SEEK_SET) ,

        b"%!PS-Adobe-3.0 EPSF-3.0"
    ),
    
    "image/tga" :
    (
        (-18 , os.SEEK_END) ,

        b"TRUEVISION-XFILE\x2e\x00"
    ),
    
    "image/dds" :
    (
        (0 , os.SEEK_SET) ,

        b"DDS"
    ),
    
    "image/icns" :
    (
        (0 , os.SEEK_SET) ,

        b"icns"
    ),
}


# 尝试猜测微信dat图片类型的列表
wechat_xor_decode_guess_tuple = \
(
    (
        (0 , os.SEEK_SET) , b"\xFF\xD8" , "jpg" #jpg
    ),
    
    (
        (0 , os.SEEK_SET) , b"\x89PNG\x0D\x0A\x1A\x0A" , "png" #png
    ),
    
    (
        (0 , os.SEEK_SET) , b"GIF87a" , "gif" #gif-1
    ),
    
    (
        (0 , os.SEEK_SET) , b"GIF89a" , "gif" #gif-2
    ),
    
    (
        (8 , os.SEEK_SET) , b"WEBP" , "webp" #webp
    ),
    
    (
        (4 , os.SEEK_SET) , b"ftypheic" , "heic" #heic
    ),
    
    (
        (0 , os.SEEK_SET) , b"BM" , "bmp" #bmp
    ),
)














# 自定义内存映射磁盘文件
class my_custom_mmap(mmap.mmap):
    # zipfile传入的fp需要有“.seekable”，mmap在python_3.8.6还不支持“.seekable”后缀，
    # 这里手动添加
    def seekable(self):
        return True


#当前时间
def current_time() -> str:
    return str(copy(datetime.datetime.now().time()))


'''
## 保留未使用的函数
# 创建未处理错误文件输出文件夹
def make_error_dir(origin_name:str) -> None:
    global error_folder_name
    error_folder_name = error_folder_name + origin_name

    if (not os.path.exists(error_folder_name)):
        os.mkdir(error_folder_name)
    elif len(os.listdir(error_folder_name)) != 0:#文件夹为空，就不创建新的了
        #防止冲突
        time_infor = current_time().replace(":","-")
        error_folder_name = "".join([error_folder_name,"【",time_infor,"】"])
        os.mkdir(error_folder_name)

    if folderlist:
        os.chdir(error_folder_name)
        for folder in folderlist:
            os.mkdir(folder)
        os.chdir("..")
    
    #无返回值
    return
'''

# 获取单文件的输出文件名
def make_single_out_name(basename:str , ext:str) -> str:
    if os.path.exists(tmp := f"{basename}.{ext}"):
        time_infor = current_time().replace(":","-")
        output_name = f"{basename}.【{time_infor}】.{ext}"
        return output_name
    else:
        return tmp


# 创建输出文件夹
def make_output_dir(origin_name:str) -> None:
    global output_folder_name
    output_folder_name = output_folder_name + origin_name
    
    if (not os.path.exists(output_folder_name)):
        os.mkdir(output_folder_name)
    elif len(os.listdir(output_folder_name)) != 0:#文件夹为空，就不创建新的了
        #防止冲突
        time_infor = current_time().replace(":","-")
        output_folder_name = "".join([output_folder_name,"【",time_infor,"】"])
        os.mkdir(output_folder_name)
    
    if folderlist:
        os.chdir(output_folder_name)
        for folder in folderlist:
            # folderlist是按层级排序的，深度浅的排在前面，是由os.walk中的topdown参数控制的（这里是默认状态）
            os.mkdir(folder)
        os.chdir("..")
    
    #无返回值
    return


# 转移修改时间，因为是复制或者从两种动态照片里原样导出的
def transfer_modify_time(f_input:Union[str , zipfile.ZipInfo], transfer_locate_path:str) -> None:
    
    if isinstance(f_input , str):
        with suppress(Exception):
            # access_time是来凑数的，毕竟time的tuple必须要两个参数
            # 【访问时间】设置为：【拷贝/原样导出】的文件的【创建时间】
            access_time = os.path.getctime(transfer_locate_path)
            modify_time = os.path.getmtime(f_input)
            os.utime(transfer_locate_path , (access_time , modify_time))
    
    elif isinstance(f_input , zipfile.ZipInfo):
        with suppress(Exception):
            access_time = os.path.getctime(transfer_locate_path)
            modify_time = time.mktime(f_input.date_time + (0,0,-1))
            os.utime(transfer_locate_path , (access_time , modify_time))
    
    # 无返回值
    return

# 尝试删除传入的文件或文件夹
def try_remove(file:str) -> None:
    if os.path.isfile(file):
        with suppress(Exception): os.remove(file)
    elif os.path.isdir(file):
        with suppress(Exception): shutil.rmtree(file)
    # 无返回值
    return


# 尝试解码
def try_decode(input_bytes:bytes) -> str:
    output = ""
    for encoding in {"utf-8-sig",cmd_encoding}:
        try:
            output = input_bytes.decode(encoding=encoding , errors="strict")
        except:
            pass
        else:
            break
    # 不行的话用utf-8强行解码
    if not output:
        output = input_bytes.decode(encoding="utf-8-sig" , errors="replace")
    return output


# 预分配磁盘空间的写入文件方式，能极大减少输出的文件碎片
def pre_allocate_write_output_file(output_path:str , data:Union[io.BytesIO, zipfile.ZipExtFile, bytes, str] , encoding:Optional[str]="utf-8-sig") -> None:
    try_remove(output_path)

    if isinstance(data , (io.BytesIO , zipfile.ZipExtFile)):
        data.seek(0 , os.SEEK_END)
        filesize = data.tell()
        
        data.seek(0 , os.SEEK_SET)
        with win_preallocate_newfile(output_path, filesize) as f:
            # 一次性全部“f.write(data.getvalue())”的话，
            # data在写入前估计又会被复制一次，虽然这个过程是短暂的
            while buf := data.read(copy_file_buffer_size):
                f.write(buf)
            # 截断多余的分配空间
            f.truncate()
        data.close() # 及时释放内存，多次close（包括退出with语句时的close）也没关系
    
    elif isinstance(data , bytes):
        with win_preallocate_newfile(output_path, len(data)) as f:
            f.write(data)
            # 截断多余的分配空间
            f.truncate()
    
    elif isinstance(data , str):
        data = "\r\n".join(data.splitlines()) # 换成CRLF
        data = data.encode(encoding=encoding , errors="replace")
        
        with win_preallocate_newfile(output_path,len(data)) as f:
            f.write(data)
			# 截断多余的分配空间
            f.truncate()
    
    else:
        raise Exception("第二个参数data类型错误")
    
    
    # 无返回值
    return




# 检查文件系统类型是否支持硬链接，据此决定是否替换复制策略
def check_fs(path:str) -> None:
    global runtime_copy_method

    fs_type = fs_info_dict.get(f"{os.path.splitdrive(path)[0]}\\" , "")
    if isinstance(fs_type , tuple):
        fs_type = fs_type[0]
    
    # 配置此路径的复制策略
    if fs_type in {"NTFS","ReFS"}:# 目前仅有NTFS和高版本的ReFS支持硬链接
        runtime_copy_method = copy_method
    else:
        # 这里调整运行时的复制策略，可以防止产生一堆“降级为拷贝”这种提醒的文件
        runtime_copy_method = 1
        if copy_method == 2:
            log("★ 文件系统类型不是NTFS或ReFS，不支持硬链接，已替换复制策略为【只用拷贝】")
    


# 从属于“transfer_file()”，由“transfer_file()”以及调用它的其他函数捕捉错误
def copy_file(input_locate_path:str, transfer_locate_path:str , mmap_f: Optional[my_custom_mmap] = None):
    
    if isinstance(mmap_f , my_custom_mmap) and (not mmap_f.closed):
        mmap_f.seek(0 , os.SEEK_SET)
        with win_preallocate_newfile(transfer_locate_path, mmap_f.size()) as dst:
            # 虽然不清楚windows内存映射的文件读到内存中的量（缓冲的大小）
            # 但这总好过dst.write(mmap_f.read())，前面这个估计会又把内容全部复制一遍
            while buf := mmap_f.read(copy_file_buffer_size):
                dst.write(buf)
            # 截断多余的分配空间
            dst.truncate()
    
    else:
        with open(input_locate_path , mode="rb") as src , win_preallocate_newfile(transfer_locate_path, os.path.getsize(input_locate_path)) as dst:
            while buf := src.read(copy_file_buffer_size):
                dst.write(buf)
            # 截断多余的分配空间
            dst.truncate()
    
    # 无返回值
    return
        


# 拷贝转移不需要处理的或者出错的文件
def transfer_file(input_locate_path:str, transfer_locate_path:str, mmap_f: Optional[my_custom_mmap] = None) -> None:
    global transfer_error_list , down_to_copy_list
    try_remove(transfer_locate_path)
    
    if runtime_copy_method == 0:
        try:
            win32file.CreateHardLink(transfer_locate_path , input_locate_path)
        
        except:
            try_remove(transfer_locate_path)# 删除可能输出的问题残留
            log("⚠ 降级为拷贝")

            try:
                copy_file(input_locate_path , transfer_locate_path , mmap_f)
            except:
                try_remove(transfer_locate_path)# 删除可能输出的问题残留
                log("❌ 拷贝失败")
                transfer_error_list.append(copy(input_locate_path))
            else:
                transfer_modify_time(input_locate_path,transfer_locate_path)
                log("✅ 拷贝成功")
                down_to_copy_list.append(copy(input_locate_path))
        
        else:
            log("✅ 硬链接成功")
    
    
    elif runtime_copy_method == 1:
        try:
            copy_file(input_locate_path , transfer_locate_path , mmap_f)
        except:
            try_remove(transfer_locate_path)# 删除可能输出的问题残留
            log("❌ 拷贝失败")
            transfer_error_list.append(copy(input_locate_path))
        else:
            transfer_modify_time(input_locate_path,transfer_locate_path)
            log("✅ 拷贝成功")
    
    
    elif runtime_copy_method == 2:
        try:
            win32file.CreateHardLink(transfer_locate_path , input_locate_path)
        except:
            try_remove(transfer_locate_path)# 删除可能输出的问题残留
            log("❌ 硬链接失败")
            transfer_error_list.append(copy(input_locate_path))
        else:
            log("✅ 硬链接成功")
    
    
    
    #无返回值
    return


# cmd标题栏展示文字
def show_title(string:str) -> None:
    author = " -- By: 不谙世事的雨滴 【吾爱破解论坛】"
    string = string.ljust(32," ")
    os.system(f"title {string}{author}")
    
    #无返回值
    return


# 在标题栏展示进度
def show_progress() -> None:
    while in_progress:
        text = "".join(
            [
                "【" , (   (f"{seq_num}／{seq_total}").rjust( 2*len(str(seq_total)) + 2 , " " )   ) , "】",
                (f"{progress_completed}／{file_total}").rjust( 2*len(str(file_total)) + 2 , " " ),
            ]
        )
        
        show_title(text)
        time.sleep(0.25-0.03)
    
    # 无返回值
    return


# 重置一些列表和变量
def reset_collections() -> None:
    global filelist , folderlist , error_list , excluded_list , transfer_error_list 
    global down_to_copy_list
    global progress_completed , file_total
    global output_folder_name #, error_folder_name
    
    filelist.clear()
    folderlist.clear()
    
    error_list.clear()
    excluded_list.clear()
    transfer_error_list.clear()
    down_to_copy_list.clear()
    
    
    progress_completed = 0
    file_total = 0
    
    output_folder_name = setted_output_prefix
    #error_folder_name = setted_error_prefix
    
    #无返回值
    return

# 判断是否只有一帧，排除动画
# .is_animated 在pillow里不是每种格式都支持的
# 参见：https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.is_animated
# .n_frame 也类似
def has_only_one_frame(im:Image) -> bool:
    if hasattr(im , "is_animated") and im.is_animated:
        return False
    else:
        return True


# 判断是否为raw文件，如果是的话返回句柄，反之返回None
def try_get_raw(src:my_custom_mmap):
    src.seek(0 , os.SEEK_SET)
    try:
        raw_structure = rawpy.imread(src)
    except:
        return None
    else:
        return raw_structure






# ExifTool增强处理（全程在内存中，现在只需一次写入磁盘了）
def exiftool_enhance_process(src_file_path: str , Initial_processed_image_fd: io.BytesIO , output_file_path: str) -> None:
    out_data = b""
    err = b""
    
    try:
        # 【-Orientation#=1】：上面“ImageOps.exif_transpose()”已经将照片翻转好了，所以这边要重置翻转
        # 最后一个“-”表示stdin；倒数第二个“-”，跟在“-o”后面的表示stdout。
        p = subprocess.Popen(args=f"exiftool -TagsFromFile \"{src_file_path}\" -Orientation#=1 -o - -" , stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True)
        out_data , err = p.communicate(Initial_processed_image_fd.getvalue())
    except Exception as e:
        err = try_decode(err)
        err_string = f"exiftool增强转移时，与exiftool进程交互时出错，详情：{e}。"
        if err:
            err_string += f"捕捉到的exiftool输出的的stderr：{err}"
        raise Exception(err_string)

    
    if p.returncode == 0:
        if out_data:
            try:
                pre_allocate_write_output_file(output_file_path , out_data)
            except Exception as e:
                raise Exception(f"在exiftool增强转移后，预分配写出时出错，详情：{e}")
        else:
            raise Exception("exiftool增强转移时，ExifTool返回的stdout中无数据")
    else:
        err = try_decode(err)
        err_string = "exiftool增强转移时，ExifTool返回非零值，估计出错了。"
        if err:
            err_string += f"捕捉到的exiftool输出的的stderr：{err}"
        raise Exception(err_string)





# 转换和（初步）保存图片
def pic_save(output_path: Optional[str] = "" , preserve_exif: Optional[bool] = True , exif_rotate: Optional[bool] = True , output_to_memory_io: Optional[bool] = False) -> Union[io.BytesIO , None]:
    global im
    
    if exif_rotate:
        # 处理exif旋转信息，详情：https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.exif_transpose
        # 看过官网的源码：https://pillow.readthedocs.io/en/stable/_modules/PIL/ImageOps.html#exif_transpose
        # ，这一步处理中，原图片exif旋转信息会被清除，防止图片保存后因为exif旋转信息残留，导致方向错误
        ImageOps.exif_transpose(im , in_place=True)
    
    # 如果最终转换为jpg、bmp，因为不支持透明层，所以要转换为RGB模式
    if im.has_transparency_data and (target_format in {"JPEG","BMP"}):
        im = im.convert('RGB')
    
    if preserve_exif:
        if output_to_memory_io:
            ret_io = io.BytesIO()
            # 保存，参数帮助：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving
            im.save(fp=ret_io , format=target_format , compress_level=png_compress_level , exif=im.getexif() )
            # 返回装载数据的io供exiftool使用
            return ret_io
        else:
            with io.BytesIO() as tmp_io:
                # 保存，参数帮助：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving
                im.save(fp=tmp_io , format=target_format , compress_level=png_compress_level , exif=im.getexif() )
                pre_allocate_write_output_file(output_path , tmp_io)
            # 无返回值
            return None
    else:
        if output_to_memory_io:
            ret_io = io.BytesIO()
            # 保存，参数帮助：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving
            im.save(fp=ret_io , format=target_format , compress_level=png_compress_level )
            # 返回装载数据的io供exiftool使用
            return ret_io
        else:
            with io.BytesIO() as tmp_io:
                # 保存，参数帮助：https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png-saving
                im.save(fp=tmp_io , format=target_format , compress_level=png_compress_level )
                pre_allocate_write_output_file(output_path , tmp_io)
            # 无返回值
            return None



# 日志合并，新的在前
def concat_log() -> None:
    
    try:
        with open(log_file , mode="rt" , encoding="utf-8-sig" , errors="replace" , newline="\r\n") as src_history:
            history = src_history.read(10**9)# 保留10^9个字符
    except:
        history = ""
    
    
    try:
        with open(tmp_log_file , mode="rt" , encoding="utf-8-sig" , errors="replace" , newline="\r\n") as src_now:
            now = src_now.read(10**9).rstrip("\x00") # 保留10^9个字符，清除预分配空间尾部未使用，一直是原样的“\x00”
    except:
        now = ""
    
    
    try:
        pre_allocate_write_output_file(log_file , (now + history) , encoding="utf-8-sig")
    except Exception as e:
        raise Exception(f"日志合并写入出错，详情：{e}")
    else:
        try_remove(tmp_log_file)
    
    # 无返回值
    return


# 猜测文件类型
def get_type(f:Union[my_custom_mmap , zipfile.ZipExtFile]) -> str:
    global wechat_xor_key 
    global mp4_start_offset , mp4_end_offset , jpg_end_offset
    global raw_structure
    
    try:
        mimetype = filetype.guess_mime(f)
    except:
        mimetype = None
    
    # PSD需要走特殊的处理方法
    if mimetype == "image/vnd.adobe.photoshop":
        return (mimetype := "special/psd")

    # （1）EPS的mime检测出来就是"application/postscript"
    #     "application/postscript"还有可能是非图片，要走最下面的匹配扩展的特征字典，
    #     只有满足下面的条件，才是EPS图片
    # （2）如果是jpg文件头的话，还要在下面判断一下是否是华为动态照片
    # （3）raw格式图片需要统一走rawpy处理，很多raw格式图片文件的文件头都是基于tiff的
    #      所以要先尝试检测raw，如果不行，再传回tiff的结果
    if mimetype and (mimetype not in {"application/postscript" , "image/jpeg" , "image/tiff" , "image/x-canon-cr2"}):
        return mimetype
    
    if (mimetype != "application/postscript"):
        # 下面判断的格式都不可能在livp文件（zip文件）里，所以忽略zipfile打开的文件句柄
        # 如果已经出"application/postscript"的结果了，跳过这里走下面的，加快点速度
        # "image/tiff" , "image/x-canon-cr2"同理
        if isinstance(f , my_custom_mmap):
            
            if not mimetype:
                
                # 判断是否为SVG格式，尺寸可能很小，最小文件大小不作限制
                # 需要限制搜索范围加快速度
                if (filesize:=f.size()) > 4096:
                    if (  (f.find(b"<svg",0,2048) != -1) and (f.rfind(b"</svg",(filesize-2048),filesize) != -1)  ) \
                    or (  (f.find(b"<\x00s\x00v\x00g",0,2048) != -1) and (f.rfind(b"<\x00/\x00s\x00v\x00g",(filesize-2048),filesize) != -1)  ) : # 可能存在的 UTF-16 编码
                        return (mimetype := "special/svg")
                else:
                    if (  (f.find(b"<svg") != -1) and (f.rfind(b"</svg") != -1)  ) \
                    or (  (f.find(b"<\x00s\x00v\x00g") != -1) and (f.rfind(b"<\x00/\x00s\x00v\x00g") != -1)  ) : # 可能存在的 UTF-16 编码
                        return (mimetype := "special/svg")
                
                
                # 判断是否为微信dat加密图片
                if f.size() > 128:
                    key_set = set()
                    for seek_point , compare_target , ext in wechat_xor_decode_guess_tuple:
                        # 每次循环都要清除，毕竟每次比对的样板不同
                        # 不能因为上一次比对的结果残留，影响下一轮的比对
                        key_set.clear()
                        
                        offset , ref = seek_point
                        try:
                            f.seek(offset , ref)
                        except:
                            continue
                        
                        # zip会适应最短的字符串，其余多余的全部会舍去，
                        # 这里固定从源文件读取32个字节，应该够特征compare_target的字节长度了，
                        # 包括以后可能新增进wechat_xor_decode_guess_tuple的特征的字节长度
                        for src , cmp in zip(f.read(32) , compare_target):
                            # 整个过程看起来如下图：
                            #
                            # 从源文件读取指定位置指定长度的字节串:     [0x12] [0x55] [0xff] [0x11] …… [0x23]   ||   [0xCD] [0xAD] …… （从源文件多读，被“zip()”舍去的字节）
                            # 　　　　　　　　　　　　　　⇩
                            #     　　　　　　　　　　　异或　　　　　　　 ^      ^      ^      ^   ……    ^
                            # 　　　　　　　　　　　　　　⇩
                            # 　自建图片特征列表里用来比对的字节串:     [0x00] [0x45] [0x79] [0x18] …… [0x24]
                            # 　　　　　　　　　　　　　　||　　　　　　　 =      =      =      =         =
                            # 　　　　　　　　　　　　　异或的结果:     [0x12] [0x10] [0x86] [0x09] …… [0x07] 
                            #
                            #     注：zip()打包好后，每组的[0x..]由字节转换为整数，所以才能进行异或运算
                            #
                            #     -->> 取按照排列顺序异或每一位的【异或的结果】，到不重复的集合【key_set】
                            #
                            key_set.add(src ^ cmp)
                        
                        # 如果满足有且仅有唯一的异或结果（没有异或结果的情况应该是read()读不到数据），
                        # 这个结果即为异或解密密钥，
                        # 代表dat大概率解密成功，大概率确定为微信dat异或加密图片
                        if len(key_set) == 1:
                            # 除了传出解密密钥方便后续解密外，也传出真实的扩展名“ext”方便输出文件
                            wechat_xor_key = ((list(key_set))[0]  ,  ext)
                            return (mimetype := "special/wechat_dat")
                        #else:
                            #continue
                
                
                # 尝试检测raw格式，同样最小大小不作限制
                if (raw_structure := try_get_raw(f)):
                    return (mimetype := "special/raw")
            
            
            # 判断是否为华为动态照片
            elif (mimetype == "image/jpeg") and f.size() > 128:
                mp4_start_offset = None
                mp4_end_offset = None
                jpg_end_offset = None
                
                f.seek(-40,os.SEEK_END)
                finder = f.tell()
                readed_bytes = f.read(40)
                f.seek(0)
                
                if ( not readed_bytes.endswith(b"\xFF\xD9") ) \
                and ( re.match("^[\d]+[:][\d]+[ ]+LIVE_[\d]+[ ]+$" , readed_bytes.decode(encoding='cp437',errors='replace') , re.I) ):
                    mp4_end_offset = copy(finder)
                    
                    if (finder := f.find(b"ctrace\x00\x00")) != -1 :
                        jpg_search_end = copy(finder)
                        mp4_start_offset = copy(finder) + 8
                        
                        if ( finder := f.rfind( (b"\xFF\xD9" + b"\x00"*8*5) , 0 , jpg_search_end  )) != -1 :
                            jpg_end_offset = copy(finder) + 2
                
                if jpg_end_offset and mp4_start_offset and mp4_end_offset:
                    return (mimetype := "special/hwlp")
                else:
                    return mimetype # 此时mimetype为"image/jpeg"
            
            
            # 判断是否为基于tiff的RAW，
            # 或者如果是CR2，替换CR2的mime为"special/raw"
            elif mimetype in {"image/tiff" , "image/x-canon-cr2"}:
                
                if (raw_structure := try_get_raw(f)):
                    return (mimetype := "special/raw")
                # 如果无法检测出RAW，可能是真的tiff
                elif mimetype == "image/tiff":
                    return mimetype
                # rawpy是支持CR2的，如果没识别出来，说明应该出问题了
                elif mimetype == "image/x-canon-cr2":
                    return (mimetype := "")
        
        # 如果是zip文件里的，就不走上面的代码
        # 华为动态图片应该不会在livp里
        elif isinstance(f , zipfile.ZipExtFile) and (mimetype == "image/jpeg"):
            return mimetype
    
    
    
    # 如果上面没给出结果并返回，或者为"application/postscript"，
    # 尝试匹配扩展的特征字典
    for k,v in ex_File_Signatures_dict.items():
        seek_point , compare_target = v
        offset , ref = seek_point
        try:
            f.seek(offset , ref)
        except:
            continue
        
        if f.read(len(compare_target)) == compare_target:
            return (mimetype := k)
    
    # 上面只要有结果，就被立马return掉了，能到这边的就是没有结果的
    # 为了防止出现 "image/" in None 报错，替换为空字符串
    return (mimetype := "")


# 检查进程是否唯一
def has_one_more_process() -> bool:
    instance_num = 0
    for proc in psutil.process_iter():
        if proc.name() in {"any_pic_2_jpg.exe","any_pic_2_png.exe"}:
            instance_num += 1
        if instance_num > 1:
            return True
    return False



'''
# 已废弃，因为exiftool现在不需要在磁盘上覆写转移exif了，
# 转移exif的写入直到预分配一次性写出磁盘前，全程在内存中
# 所以也就不需要整理碎片了
# wmi检测物理磁盘类型，wmi库的速度很慢，要分离出单独的线程，在程序一开始就运行
def wmi_check_physical_disk() -> None:
    global pd_dict
    
    # 不在线程中这么做会报错
    pythoncom.CoInitialize()
    
    for physical_disk in wmi.WMI().Win32_DiskDrive():
        try:
            if pySMART.Device(f'/dev/pd{physical_disk.Index}').rotation_rate :
                is_hdd = True
            else:
                is_hdd = False
        except:
            is_hdd = False
        
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                partition_letter = getattr(logical_disk,"DeviceID","")
                pd_dict[copy(partition_letter)] = copy(is_hdd)
    
    # 与“pythoncom.CoInitialize()”相对应
    pythoncom.CoUninitialize()
    
    return
'''


# 结束时的弹窗
def close_up() -> None:
    
    def center_window(window:tkinter.Tk):
        # 获取屏幕的宽度和高度
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        width = window.winfo_width()
        height = window.winfo_height()
        # 计算窗口左上角的坐标
        center_x = int(screen_width/2 - width/2)
        center_y = int(screen_height/2 - height/2)
        # 将窗口定位到计算出的位置
        window.geometry(f'{width}x{height}+{center_x}+{center_y}')
    
    def show_log() -> None:
        root.destroy()
        if os.path.isfile(log_file):
            os.system(f"start \"title\" notepad \"{log_file}\"")
    
    def show_sinfor() -> None:
        # 取消当前窗口置顶
        root.wm_attributes("-topmost", 0)
        show_sponsor_info(scale_factor,root)
    
    if pop_window_main_switch and show_finish_window:
        # 创建一个Tkinter窗口
        root = tkinter.Tk()
        # 暂时隐藏，避免闪屏
        root.withdraw()
        # 设置程序缩放
        if scale_factor != 100:
            root.tk.call('tk', 'scaling', scale_factor/75)
        # 标题
        root.title(app_exe)
        # 提示词
        tkinter.Label(root,text="处理完毕",font="宋体 40").grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        tkinter.Button(root,text="完成",font="微软雅黑 15 bold",command=root.destroy).grid(row=3, column=0, padx=10, pady=10)
        tkinter.Button(root,text="查看运行日志",font="微软雅黑 15 bold",command=show_log).grid(row=3, column=1, padx=10, pady=10)
        tkinter.Button(root,text="给作者加个鸡腿",font="微软雅黑 15 bold",command=show_sinfor).grid(row=3, column=2, padx=10, pady=10)
        # 自动调整窗口大小
        root.update_idletasks()
        # 调用函数来居中窗口
        center_window(root)
        # 重新显示窗口
        root.deiconify()
        # 播放提示音
        win32api.MessageBeep(win32con.MB_ICONINFORMATION)
        # 设置窗口为置顶显示，锁定大小
        root.wm_attributes("-topmost", 1)
        root.resizable(False, False)
        root.mainloop()
    
    # 无返回值
    return




# # # # # # # # # # # # # # # 初始化变量 # # # # # # # # # # # # # # #

# 解析传入的命令行（路径）
# 趁还在图片目标路径下（从图片目标路径启动cmd时），收集处理目标的绝对路径
args=[os.path.abspath(i) for i in sys.argv[1:]]


# 如果不是以分隔符结尾，要补上分隔符“;”，
# 在刚刚装好的win7虚拟机上吃了一亏，然后补上的
if not (os.environ['PATH']).endswith(";"):
    os.environ['PATH'] += ";"
# 添加exiftool路径添加到到临时环境变量，方便运行exiftool
os.environ['PATH'] += f"{program_dir}\\ExifTool\\;"
#os.environ['PATH'] += f"{program_dir}\\SmartMonTools\\;"

#输出【文件/文件夹】名称的前缀
output_folder_name = setted_output_prefix
#error_folder_name = setted_error_prefix

#存放单个路径下，文件、文件夹的列表
filelist = []
folderlist = []

#存放处理进度
seq_num = 0
seq_total = len(args)
progress_completed = 0
file_total = 0

#是否还在进行中，给显示进度的线程判断结束条件使用
in_progress = True
#故障文件列表
error_list = []
#排除文件列表
excluded_list = []
#转移时出错的文件列表
transfer_error_list = []
#转移时降级为拷贝后成功拷贝的文件列表
down_to_copy_list = []
#用于给pdf中图片去重的crc集合
crc32_set = set()


# # # # # # # # # # # # # # # 初始化变量 # # # # # # # # # # # # # # #



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




# 检查重复进程
if has_one_more_process():
    handle_critical_error("程序仅允许同一时间有一个进程存在，程序终止" , log_handle_present=False)


# 检查组件exiftool
if (ret := os.system("exiftool -ver >nul 2>nul")):
    handle_critical_error("找不到程序组件【ExifTool】，程序终止" , log_handle_present=False)



show_title("读取配置文件中...")

"""
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

# 4.【打开处理完毕时的弹窗】
try:
    tmp = cfg.getboolean(section="window_pop_behavior" , option="show_finish_window")
except:
    pass
else:
    show_finish_window = copy(tmp)

# 5.【打开关键错误弹窗】（系统变量优先）
if not show_critical_error_window_got_os_environ:
    try:
        tmp = cfg.getboolean(section="window_pop_behavior" , option="show_critical_error_window")
    except:
        pass
    else:
        show_critical_error_window = copy(tmp)
"""


## [transfer]
# 6.【复制策略】
try:
    tmp = cfg.getint(section="transfer" , option="copy_method")
except:
    pass
else:
    if tmp in range(0,3):
        copy_method = copy(tmp)


## [quality]
# 7.【输出的jpg图片质量】
try:
    tmp = cfg.getint(section="quality" , option="jpg_quality")
except:
    pass
else:
    if tmp in range(1,101):
        jpg_quality = copy(tmp)

# 8.【jpg子采样选项】
try:
    tmp = cfg.getint(section="quality" , option="jpg_subsample_option")
except:
    pass
else:
    if tmp in range(0,3):
        jpg_subsample_option = copy(tmp)

# 9.【png无损压缩（zip）的等级】
try:
    tmp = cfg.getint(section="quality" , option="png_compress_level")
except:
    pass
else:
    if tmp in range(0,10):
        png_compress_level = copy(tmp)


## [format]
# 10.【用户自定义排除的格式】
try:
    tmp = cfg.get(section="format" , option="user_defined_excluded_format_set")
except:
    pass
else:
    tmp = {i.upper() for i in re.split(r"[\s]*[,|，|、|/|\\|\|]+[\s]*",tmp) if i.upper() in supported_format_set}
    user_defined_excluded_format_set = copy(tmp)

# 11.【排除已经是目标格式的文件】
try:
    tmp = cfg.getboolean(section="format" , option="exclude_target_format")
except:
    pass
else:
    exclude_target_format = copy(tmp)

# 12.【是否转换RAW图片】
try:
    tmp = cfg.getboolean(section="format" , option="convert_raw")
except:
    pass
else:
    convert_raw = copy(tmp)

# 13.【是否转换苹果LIVP动态照片】
try:
    tmp = cfg.getboolean(section="format" , option="convert_livp")
except:
    pass
else:
    convert_livp = copy(tmp)

# 14.【苹果LIVP动态照片直接输出，不转换】
try:
    tmp = cfg.getboolean(section="format" , option="livp_direct_output")
except:
    pass
else:
    livp_direct_output = copy(tmp)

# 15.【是否转换华为动态照片】
try:
    tmp = cfg.getboolean(section="format" , option="convert_hwlp")
except:
    pass
else:
    convert_hwlp = copy(tmp)

# 16.【华为动态照片直接输出，不转换】
try:
    tmp = cfg.getboolean(section="format" , option="hwlp_direct_output")
except:
    pass
else:
    hwlp_direct_output = copy(tmp)

# 17.【是否转换PDF】
try:
    tmp = cfg.getboolean(section="format" , option="convert_pdf")
except:
    pass
else:
    convert_pdf = copy(tmp)

# 18.【PDF转换模式】
try:
    tmp = cfg.getint(section="format" , option="pdf_mode")
except:
    pass
else:
    if tmp in range(0,3):
        pdf_mode = copy(tmp)

# 19.【PDF内嵌图片直接输出，不转换】
try:
    tmp = cfg.getboolean(section="format" , option="pdf_inside_pic_direct_output")
except:
    pass
else:
    pdf_inside_pic_direct_output = copy(tmp)

# 20.【PDF页面渲染图缩放比例】
try:
    tmp = cfg.getfloat(section="format" , option="pdf_page_render_zoom_ratio")
except:
    pass
else:
    if tmp > 0:
        pdf_page_render_zoom_ratio = copy(tmp)

# 21.【是否转换SVG】
try:
    tmp = cfg.getboolean(section="format" , option="convert_svg")
except:
    pass
else:
    convert_svg = copy(tmp)

# 22.【SVG转换后直接输出PNG】
try:
    tmp = cfg.getboolean(section="format" , option="svg_direct_output_png")
except:
    pass
else:
    svg_direct_output_png = copy(tmp)

# 23.【是否转换微信加密的dat图片】
try:
    tmp = cfg.getboolean(section="format" , option="convert_wechat_dat")
except:
    pass
else:
    convert_wechat_dat = copy(tmp)

# 24.【微信dat图片解密后直接输出，不转换】
try:
    tmp = cfg.getboolean(section="format" , option="wechat_dat_direct_output")
except:
    pass
else:
    wechat_dat_direct_output = copy(tmp)


## [exif]
# 25.【转换时是否保留RAW图片的exif】
try:
    tmp = cfg.getboolean(section="exif" , option="perserve_raw_pic_exif")
except:
    pass
else:
    perserve_raw_pic_exif = copy(tmp)

# 26.【转换时是否保留普通图片的exif】
try:
    tmp = cfg.getboolean(section="exif" , option="perserve_common_pic_exif")
except:
    pass
else:
    perserve_common_pic_exif = copy(tmp)

# 27.【转换时是否使用exiftool额外增强保存一次exif】
try:
    tmp = cfg.getboolean(section="exif" , option="exif_enhance")
except:
    pass
else:
    exif_enhance = copy(tmp)


"""
# 此项设置已作废
# 28.【调用exiftool后，是否整理覆写产生的磁盘碎片】
try:
    tmp = cfg.getint(section="exif" , option="defrag_after_exiftool")
except:
    pass
else:
    if tmp in range(0,3):
        defrag_after_exiftool = copy(tmp)
"""


## [buffer]
# 29.【拷贝文件的内存缓冲区大小】MiB
try:
    tmp = cfg.getint(section="buffer" , option="copy_file_buffer_size")
except:
    pass
else:
    if tmp > 0:
        # 不大于可用内存的1/4
        copy_file_buffer_size = min( tmp*1024**2 , (psutil.virtual_memory().available)//4 )

# 30.【给临时日志文件预分配的空间】MiB
try:
    tmp = cfg.getint(section="buffer" , option="log_file_allocate_size")
except:
    pass
else:
    if tmp > 0:
        log_file_allocate_size = min(tmp*1024**2 , 4*10**9) # 10**9个字符限制，每个字符4字节计算

with suppress(Exception): del cfg #释放些内存


show_title("获取信息并配置中...")

try:
    # 上次运行可能因为出错产生的残留临时日志文件
    if os.path.isfile(tmp_log_file):
        concat_log()
except Exception as e:
    handle_critical_error(f"无法合并上次运行残留的临时日志文件，\n详情：{e}，程序终止" , log_handle_present=False)


try:
    # 预先分配空间给临时日志文件
    log_handle = win_preallocate_newfile(tmp_log_file, log_file_allocate_size, text_mode=True, encoding="utf-8-sig", errors="raplace", newline="\r\n" , buffering=1) # CRLF，行缓冲，遇到换行符就flush

except Exception as e:
    handle_critical_error(f"\n\n无法创建日志文件，\n详情：{e}，程序终止" , log_handle_present=False)


with log_handle:
    
    try:
        # 日志文件头1
        log(
            "\n".join([
                f"＝＝＝＝＝＝＝＝＝＝＝　▶　{str(datetime.datetime.now())}　◀　＝＝＝＝＝＝＝＝＝＝＝",
                "\n",
                f"【弹窗总开关】：{pop_window_main_switch}",
                f"【打开关键错误弹窗】：{show_critical_error_window}        ||       【打开处理完毕时的弹窗】：{show_finish_window}",
                f"【单纯双击启动程序“any_pic_2_jpg.exe” / “to_jpg.bat” 的表现模式】：{to_jpg_exe_no_path_parameter_behavior}",
                f"【单纯双击启动程序“any_pic_2_png.exe” / “to_png.bat” 的表现模式】：{to_png_exe_no_path_parameter_behavior}",
                "\n\n",
            ])
        )
        
        
        # 配置运行时排除的格式
        if exclude_target_format:
            runtime_excluded_format_set = user_defined_excluded_format_set | {copy(target_format)}
        else:
            runtime_excluded_format_set = copy(user_defined_excluded_format_set)
        
        
        os.system("cls")
        # 启动进度展示线程
        t = threading.Thread(target=show_progress , daemon=True)
        t.start()
        
        # 日志记录头2
        log(
            
            "\n".join([
                
                "程序识别出的参考信息　　⇩　⇩\n",
                "格式：盘符 --> (分区文件系统 , 簇大小)",
                "-----------------------------------------",
                "\n".join([f"{k} --> {v}" for k,v in fs_info_dict.items()]),
                "-----------------------------------------",
                "\n\n",
                f"转换目标格式：【{target_format}】（扩展名：【.{target_ext}】）",
                "格式排除列表：" + ("、".join(runtime_excluded_format_set)),
                f"复制策略：{copy_method}",
                "\n",
                f"【输出的jpg图片质量】配置为：{jpg_quality}        ||        【jpg子采样选项】配置为：{jpg_subsample_option}",
                f"【png无损压缩（zip）的等级】配置为：{png_compress_level}",
                "\n",
                f"转换RAW格式图片：{convert_raw}        ||        转换PDF：{convert_pdf}        ||        PDF转换模式：{pdf_mode}",
                f"PDF页面渲染图缩放比例：{pdf_page_render_zoom_ratio}        ||        PDF内嵌图片直接输出：{pdf_inside_pic_direct_output}",
                f"转换LIVP格式图片：{convert_livp}        ||        LIVP动态照片直接输出：{livp_direct_output}",
                f"转换华为动态照片：{convert_hwlp}        ||        华为动态照片直接输出：{hwlp_direct_output}",
                f"转换SVG图片：{convert_svg}        ||        SVG转换后直接输出PNG：{svg_direct_output_png}",
                f"转换微信加密的dat图片：{convert_wechat_dat}        ||        微信dat图片解密后直接输出，不转换：{wechat_dat_direct_output}",
                "\n",
                f"保留RAW图片的exif：{perserve_raw_pic_exif}        ||        保留普通图片的exif：{perserve_common_pic_exif}",
                f"使用exiftool额外增强保存一次exif ：{exif_enhance}",
                "\n",
                f"拷贝文件的内存缓冲区大小 ：{copy_file_buffer_size//1024//1024} MiB",
                f"给临时日志文件预分配的空间大小 ：{log_file_allocate_size//1024//1024} MiB",
                "\n\n\n\n\n",
                "任务日志：⇩　⇩　⇩",
                "\n",
            ])
        
        )
        
        
        
        for seq_num , target_path in enumerate(args , start=1):
            
            reset_collections()
            log(f"【{seq_num}】　→　＜　{target_path}　＞\n")
            
            if not (os.path.exists(target_path)):
                log("❗　路径不存在")
                error_list.append(copy(target_path))
                continue
            
            # 检查目标路径所在盘符的文件系统类型是否支持硬链接
            # 并配置此目标路径是否需要在调用exiftool后整理碎片文件
            check_fs(target_path)
            
            # 目标是单个文件的情况
            if os.path.isfile(target_path):
                
                file_total = 1
                
                os.chdir(os.path.dirname(target_path))
                
                input_locate_path = os.path.basename(target_path)
                # 单文件不需要转移，所以不需要transfer_locate_path
                output_locate_base = f"{os.path.splitext(input_locate_path)[0]}{single_file_output_suffix}"
                
                if not os.path.getsize(input_locate_path):
                    log(f"▷     【{input_locate_path}】 是空文件，跳过")
                    excluded_list.append(copy(input_locate_path))
                    progress_completed += 1
                    continue
                
                try:
                    src_f = open(input_locate_path,mode="rb")
                    mf = my_custom_mmap(src_f.fileno(),length=0,access=mmap.ACCESS_READ)
                except Exception as e:
                    with suppress(Exception): mf.close()
                    with suppress(Exception): src_f.close()
                    log(f"▷▷       【{input_locate_path}】 作为文件打开时出错，跳过。详情：{e}")
                    error_list.append(copy(input_locate_path))
                    progress_completed = 1
                    continue
                
                
                
                with src_f , mf :
                    
                    if mf.size() > filesize_limit:
                        log(f"▷     【{input_locate_path}】 超过文件大小限制（{filesize_limit}），跳过")
                        excluded_list.append(copy(input_locate_path))
                        progress_completed = 1
                        continue
                    
                    try:
                        mimetype = get_type(mf)
                    except Exception as e:
                        log(f"×    【{input_locate_path}】 获取mimetype出错，详情：{e}")
                        error_list.append(copy(input_locate_path))
                        progress_completed = 1
                        continue
                    
                    
                    # 处理微信dat加密图片
                    if mimetype == "special/wechat_dat":
                        
                        if convert_wechat_dat:
                            
                            try:
                                int_key , ext = wechat_xor_key
                                wechat_output_name = make_single_out_name(output_locate_base , ext)
                                convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                                
                                with io.BytesIO( bytes( (i ^ int_key) for i in bytearray(mf) ) )  as  decoded_data_io:
                                    
                                    if wechat_dat_direct_output:
                                        pre_allocate_write_output_file( wechat_output_name , decoded_data_io )
                                        transfer_modify_time(input_locate_path , wechat_output_name)
                                    
                                    else:
                                        with Image.open(decoded_data_io) as im:
                                            
                                            if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                # 需要转换，原来的文件数据没用了
                                                # 确保im完全加载，然后关掉decoded_data_io节省内存
                                                im.load()
                                                # load方法自动关掉了decoded_data_io，这边只是重复确认一下
                                                decoded_data_io.close()
                                                # 将im中的图片保存
                                                pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                                transfer_modify_time(input_locate_path , convert_out_locate_path)
                                            
                                            else:
                                                log(f"🔔   微信dat图片【{input_locate_path}】因格式被排除或含有多个帧，虽已设置强制转换，但仍直接导出")
                                                # 如果在这行注释的地方用im.close()，decoded_data_io也会被关掉，所以没太好的方法，暂时留着吧
                                                pre_allocate_write_output_file( wechat_output_name , decoded_data_io )
                                                transfer_modify_time(input_locate_path , wechat_output_name)
                            
                            
                            except Exception as e:
                                try_remove(wechat_output_name)
                                try_remove(convert_out_locate_path)
                                log(f"×    微信dat图片【{input_locate_path}】转换格式失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            
                            else:
                                log(f"√  微信dat图片【{input_locate_path}】转换成功")
                        
                        else:
                            log(f"◎        微信dat图片设置为不转换，跳过【{input_locate_path}】")
                            excluded_list.append(copy(input_locate_path))
                    
                    
                    # 处理华为动态图片
                    elif mimetype == "special/hwlp":
                        
                        if convert_hwlp:
                            hwlp_jpg_output_path = make_single_out_name(output_locate_base , "jpg")
                            hwlp_mp4_output_path = make_single_out_name(output_locate_base , "mp4")
                            convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                            
                            try:
                                with io.BytesIO(mf[0:jpg_end_offset]) as jpg_io:
                                    # 导出图片
                                    if hwlp_direct_output:
                                        pre_allocate_write_output_file(hwlp_jpg_output_path , jpg_io)
                                        transfer_modify_time(input_locate_path , hwlp_jpg_output_path)
                                    else:
                                        with Image.open(jpg_io) as im :
                                            if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                # 需要转换，原来的文件数据没用了
                                                # 确保im完全加载，然后关掉jpg_io节省内存
                                                im.load()
                                                # load方法自动关掉了jpg_io，这边只是重复确认一下
                                                jpg_io.close()
                                                # 将im中的图片保存
                                                pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                                transfer_modify_time(input_locate_path , convert_out_locate_path)
                                            else:
                                                log(f"🔔   华为动态照片【{input_locate_path}】因格式被排除或含有多个帧，虽已设置强制转换，但仍直接导出")
                                                # 如果在这行注释的地方用im.close()，jpg_io也会被关掉，所以没太好的方法，暂时留着吧
                                                pre_allocate_write_output_file(hwlp_jpg_output_path , jpg_io)
                                                transfer_modify_time(input_locate_path , hwlp_jpg_output_path)
                                
                                # 导出视频
                                pre_allocate_write_output_file(hwlp_mp4_output_path , mf[mp4_start_offset:mp4_end_offset])
                                transfer_modify_time(input_locate_path , hwlp_mp4_output_path)
                            
                            except Exception as e:
                                try_remove(hwlp_jpg_output_path)# 删除可能输出的问题残留
                                try_remove(hwlp_mp4_output_path)# 删除可能输出的问题残留
                                try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                
                                log(f"× ×  【{input_locate_path}】 作为华为动态照片导出时失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            
                            else:
                                log(f"√       华为动态照片【{input_locate_path}】导出成功")
                        
                        else:
                            log(f"◎        华为动态照片被设置为不转换，跳过【{input_locate_path}】")
                            excluded_list.append(copy(input_locate_path))
                    
                    
                    # 处理SVG
                    elif mimetype == "special/svg":
                        
                        if convert_svg:
                            svg_output_name = make_single_out_name(output_locate_base , "png")
                            convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                            
                            try:
                                
                                with io.BytesIO() as tmp_io:
                                    #mf.seek(0 , os.SEEK_SET)
                                    # 这个mf（mmap.mmap）属实有点特殊，如果没有修改cairosvg库
                                    # 在这里如果不“seek(0)”的话，下面一行就读不到mf的文件数据
                                    # （我已经改了cairosvg库，所以注释掉了）
                                    cairosvg.svg2png(file_obj=mf , write_to=tmp_io)
                                    
                                    if svg_direct_output_png or (target_format=="PNG"):
                                        pre_allocate_write_output_file(svg_output_name , tmp_io)
                                        transfer_modify_time(input_locate_path , svg_output_name)
                                    else:
                                        with Image.open(tmp_io) as im:
                                            if (not has_only_one_frame(im)):
                                                log(f"🔔   svg图片【{input_locate_path}】因含有多个帧，虽已设置强制转换，但仍直接导出")
                                                pre_allocate_write_output_file(svg_output_name , tmp_io)
                                                transfer_modify_time(input_locate_path , svg_output_name)
                                            else:
                                                # 需要转换，原来的文件数据没用了
                                                # 确保im完全加载，然后关掉tmp_io节省内存
                                                im.load()
                                                # load方法自动关掉了tmp_io，这边只是重复确认一下
                                                tmp_io.close()
                                                
                                                
                                                # exiftool支持从源SVG文件读取exif
                                                if exif_enhance:
                                                    # cairosvg输出的PNG应该没有关于旋转的exif定义，所以这边不根据exif旋转图片了
                                                    with pic_save(preserve_exif=perserve_common_pic_exif , exif_rotate=False , output_to_memory_io=True) as exif_tmp_io:
                                                        # im已转出文件，可以关掉省内存了
                                                        im.close()
                                                        # 使用exiftool对exif进行增强转移
                                                        exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                                else:
                                                    # cairosvg输出的PNG应该没有关于旋转的exif定义，所以这边不根据exif旋转图片了
                                                    pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif , exif_rotate=False)
                                                transfer_modify_time(input_locate_path , convert_out_locate_path)
                            
                            except Exception as e:
                                try_remove(svg_output_name)# 删除可能输出的问题残留
                                try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                log(f"×    SVG图片【{input_locate_path}】转换格式失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            
                            else:
                                log(f"√  SVG图片【{input_locate_path}】转换成功")
                        
                        
                        
                        else:
                            log(f"◎        SVG图片设置为不转换，跳过【{input_locate_path}】")
                            excluded_list.append(copy(input_locate_path))
                    
                    
                    # 处理RAW格式
                    elif mimetype == "special/raw":
                        
                        if convert_raw:
                            convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                            
                            with raw_structure:
                                try:
                                    # 【use_camera_wb=True】：使用相机的白平衡
                                    rgb = raw_structure.postprocess(use_camera_wb=True)
                                except Exception as e:
                                    log(f"× × ×    【{input_locate_path}】 raw文件在rawpy后处理中出错，详情：{e}")
                                    error_list.append(copy(input_locate_path))
                                    progress_completed = 1
                                    continue
                            
                            try:
                                im = Image.fromarray(rgb)
                                im.load() # 确保矩阵删除释放内存前被完全加载
                            except Exception as x:
                                e = copy(x)
                                # 释放内存，一个RAW格式图片转换出的矩阵尺寸应该很大
                                with suppress(Exception): del rgb
                                log(f"× × ×    【{input_locate_path}】 raw文件在pillow打开传递过来的向量中出错，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            else:
                                # 释放内存，一个RAW格式图片转换出的矩阵尺寸应该很大
                                with suppress(Exception): del rgb
                            
                            with im:
                                try:
                                    if perserve_raw_pic_exif:
                                        # 传递过来的array中不含有exif，且上面rawpy后处理中已经根据raw中的exif，把图片翻转摆正了
                                        # 所以这边也不根据exif翻转图片，万一真的有exif传过来，再翻转就乱套了
                                        with pic_save(preserve_exif=False , exif_rotate=False , output_to_memory_io=True) as exif_tmp_io:
                                            # im已转出文件，可以关掉省内存了
                                            im.close()
                                            # 使用exiftool转移raw图片的exif
                                            exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                    else:
                                        # 传递过来的array中不含有exif，且上面rawpy后处理中已经根据raw中的exif，把图片翻转摆正了
                                        # 所以这边也不根据exif翻转图片，万一真的有exif传过来，再翻转就乱套了
                                        pic_save(output_path=convert_out_locate_path , preserve_exif=False , exif_rotate=False)
                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                
                                except Exception as e:
                                    try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                    log(f"× × ×    【{input_locate_path}】 raw文件在pillow保存为“{target_format}”中出错，详情：{e}")
                                    error_list.append(copy(input_locate_path))
                                    progress_completed = 1
                                    continue
                                else:
                                    log(f"√ 【{input_locate_path}】 raw文件转换成功")
                        
                        
                        else:
                            with suppress(Exception): raw_structure.close()
                            log(f"◎        RAW格式图片被设置为不转换，跳过【{input_locate_path}】")
                            excluded_list.append(copy(input_locate_path))
                            progress_completed = 1
                            continue
                    
                    
                    # 处理PSD图像
                    elif mimetype == "special/psd":
                        
                        if "PSD" not in runtime_excluded_format_set:
                            
                            convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                            
                            try:
                                mf.seek(0,0)
                                im = PSDImage.open(mf)
                            except Exception as e:
                                log(f"×    【{input_locate_path}】 作为PSD图片打开时失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            
                            try:
                                im = im.composite(apply_icc=True)
                            except Exception as e:
                                log(f"×    PSD图片【{input_locate_path}】处理失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue

                            try:
                                if exif_enhance:
                                    # 将im中的图片保存
                                    with pic_save(preserve_exif=perserve_common_pic_exif , output_to_memory_io=True) as exif_tmp_io:
                                        # im已转出文件，可以关掉省内存了
                                        im.close()
                                        # 使用exiftool对exif进行增强转移
                                        exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                else:
                                    # 将im中的图片保存
                                    pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                transfer_modify_time(input_locate_path , convert_out_locate_path)
                            
                            except Exception as e:
                                try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                log(f"×    PSD图像【{input_locate_path}】转换格式失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            else:
                                log(f"√ 【{input_locate_path}】 转换成功")
                        
                        else:
                            log(f"▷        图像【{input_locate_path}】的格式【PSD】被排除，不转换")
                            excluded_list.append(copy(input_locate_path))


                    # 处理一般pillow可处理的图片
                    elif "image/" in mimetype:
                        
                        try:
                            im = Image.open(mf)
                        except Exception as e:
                            log(f"×    【{input_locate_path}】 作为图片打开时失败，详情：{e}")
                            error_list.append(copy(input_locate_path))
                            progress_completed = 1
                            continue
                        
                        with im:
                            
                            if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                
                                convert_out_locate_path = make_single_out_name(output_locate_base , target_ext)
                                
                                try:
                                    if exif_enhance:
                                        # 将im中的图片保存
                                        with pic_save(preserve_exif=perserve_common_pic_exif , output_to_memory_io=True) as exif_tmp_io:
                                            # im已转出文件，可以关掉省内存了
                                            im.close()
                                            # 使用exiftool对exif进行增强转移
                                            exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                    else:
                                        # 将im中的图片保存
                                        pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                
                                except Exception as e:
                                    try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                    log(f"×    【{input_locate_path}】 转换格式失败，详情：{e}")
                                    error_list.append(copy(input_locate_path))
                                    progress_completed = 1
                                    continue
                                else:
                                    log(f"√ 【{input_locate_path}】 转换成功")
                            
                            else:
                                log(f"▷        【{input_locate_path}】 的格式被排除或含有多个帧，不转换")
                                excluded_list.append(copy(input_locate_path))
                    
                    
                    # 处理PDF
                    elif mimetype == "application/pdf":
                        
                        if convert_pdf:
                            
                            crc32_set.clear()
                            pdf_output_main_dir = make_single_out_name(output_locate_base , "")
                            
                            try:
                                pdf_handle = pymupdf.Document(stream=mf , filetype="pdf")
                            except Exception as e:
                                log(f"×    【{input_locate_path}】 作为PDF打开时失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            
                            try:
                                with pdf_handle:
                                    # 创建和PDF同名（不带扩展名）的输出文件夹
                                    os.mkdir(pdf_output_main_dir)
                                    
                                    if pdf_mode in {0,1}:
                                        
                                        inside_img_output_path = f"{pdf_output_main_dir}\\PDF中嵌入的图片"
                                        os.mkdir(inside_img_output_path)
                                        
                                        
                                        pic_num = 1
                                        for xref in range(1 , pdf_handle.xref_length()):
                                            
                                            try:
                                                img_dict = pdf_handle.extract_image(xref)
                                            except:
                                                continue
                                            
                                            # 是图片、有文件数据、数据不重复
                                            if (file_data := img_dict.get('image',None)) \
                                            and (crc_value := crc32c.crc32c(file_data)) not in crc32_set:
                                                crc32_set.add(crc_value)
                                                ext = img_dict.get("ext","")
                                                
                                                del img_dict # 已经没用了
                                                
                                                try:
                                                    file_data = io.BytesIO(file_data)
                                                    with file_data:
                                                        if pdf_inside_pic_direct_output:
                                                            pre_allocate_write_output_file((single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{ext}")  ,  file_data)
                                                        else:
                                                            with Image.open(file_data) as im:
                                                                if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                                    # 需要转换，原来的文件数据没用了
                                                                    # 确保im完全加载，然后关掉file_data节省内存
                                                                    im.load()
                                                                    # load方法自动关掉了file_data，这边只是重复确认一下
                                                                    file_data.close()
                                                                    # 将im中的图片保存
                                                                    pic_save(output_path = (single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{target_ext}") , preserve_exif=perserve_common_pic_exif)
                                                                else:
                                                                    # 如果在这行注释的地方用im.close()，file_data也会被关掉，所以没太好的方法，暂时留着吧
                                                                    pre_allocate_write_output_file((single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{ext}")  ,  file_data)
                                                    transfer_modify_time(input_locate_path , single_pic_path)
                                                except:
                                                    continue
                                                else:
                                                    pic_num += 1
                                        
                                        if pic_num == 1:#无图片成功导出
                                            try_remove(inside_img_output_path)
                                    
                                    if pdf_mode in {0,2}:
                                        inside_page_render_output_path = f"{pdf_output_main_dir}\\PDF页面渲染图"
                                        os.mkdir(inside_page_render_output_path)
                                        mat = pymupdf.Matrix(pdf_page_render_zoom_ratio , pdf_page_render_zoom_ratio)
                                        
                                        page_num = 1
                                        for page in pdf_handle.pages():
                                            try:
                                                page_pixmap = page.get_pixmap(matrix=mat)
                                                with io.BytesIO() as tmp_io:
                                                    # 生成的页面渲染图中不带透明信息，除非上面一步get_pixmap()传入了“alpha=True”
                                                    # 详情请看：https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_pixmap
                                                    # 应该大概率不含exif信息（包括旋转信息）
                                                    page_pixmap.pil_save(fp=tmp_io , format=target_format , compress_level=png_compress_level )
                                                    pre_allocate_write_output_file((single_page_path:=f"{inside_page_render_output_path}\\{str(page_num).zfill(3)}.{target_ext}") , tmp_io)
                                                transfer_modify_time(input_locate_path , single_page_path)
                                            except:
                                                continue
                                            else:
                                                page_num += 1
                                        
                                        if page_num == 1:#无页面成功渲染
                                            try_remove(inside_page_render_output_path)
                            
                            
                            except Exception as e:
                                try_remove(pdf_output_main_dir)# 删除可能输出的问题残留
                                log(f"×    PDF文件【{input_locate_path}】转换格式失败，详情：{e}")
                                error_list.append(copy(input_locate_path))
                                progress_completed = 1
                                continue
                            else:
                                log(f"√    PDF文件【{input_locate_path}】转换成功")
                        
                        else:
                            log(f"◎      PDF被设置为不转换，跳过【{input_locate_path}】")
                            excluded_list.append(copy(input_locate_path))
                    
                    
                    # livp格式是zip压缩包
                    elif mimetype == "application/zip":
                        
                        zip_extra_path = "."
                        
                        try:
                            zfh = zipfile.ZipFile(mf)
                            z_object_list = zfh.infolist()
                            z_file_info_list = [i for i in z_object_list if i.is_file()] # 排除zip里的文件夹
                            log(f"▷        【{input_locate_path}】 满足zip文件条件，可能是livp文件")
                        except Exception as e:
                            with suppress(Exception): zfh.close()
                            log(f"×    【{input_locate_path}】 作为压缩包打开处理过程中出错，详情：{e}")
                            error_list.append(copy(input_locate_path))
                            progress_completed = 1
                            continue
                        
                        with zfh:
                            
                            # 如果压缩包里存在1个文件夹，其下2个文件，“.namelist()”中个数就会是3个
                            if len(z_file_info_list) == len(z_object_list) == 2:
                                
                                log(f"▷▷       【{input_locate_path}】 满足livp文件数量为2个的特征")
                                
                                if convert_livp:
                                    successfully_processed_zfile_num = 0
                                    for z_info in z_file_info_list:
                                        z_file = z_info.filename
                                        z_name = os.path.splitext(z_file)[0]
                                        z_output_locate_path = f"{zip_extra_path}\\{z_name}.{target_ext}"
                                        z_copy_out_locate_path = f"{zip_extra_path}\\{z_file}"
                                        
                                        try:
                                            f = zfh.open(z_info)
                                        except Exception as e:
                                            log(f"×    【{input_locate_path} ⇨ {z_file}】 作为压缩包下的文件打开出错，已跳过，详情：{e}")
                                            continue
                                        
                                        with f:
                                            
                                            try:
                                                mimetype = get_type(f)
                                            except Exception as e:
                                                log(f"×    【{input_locate_path} ⇨ {z_file}】 获取mimetype出错，详情：{e}")
                                                continue
                                            
                                            
                                            if ("image/" in mimetype) or ( (tmp := (os.path.splitext(z_file)[1][1:]).lower()) in {"jpg","jpeg","heic","heif","png","bmp","tiff"} ):
                                                
                                                if livp_direct_output:
                                                    try:
                                                        pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                        transfer_modify_time(z_info , z_copy_out_locate_path)
                                                    except Exception as e:
                                                        try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                        log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 直接输出失败，详情：{e}")
                                                        continue
                                                    else:
                                                        log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 直接输出成功 √")
                                                
                                                else:
                                                    try:
                                                        im = Image.open(f)
                                                    except Exception as e:
                                                        log(f"▷▷▷▷ × × ×【{input_locate_path} ⇨ {z_file}】 作为图片打开时出错，详情：{e}")
                                                        continue
                                                    
                                                    with im:
                                                        
                                                        if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                            log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 需要转换图片格式")
                                                            
                                                            try:
                                                                # 需要转换，原来的文件数据没用了
                                                                # 确保im完全加载，然后关掉f节省内存
                                                                im.load()
                                                                # load方法自动关掉了f，这边只是重复确认一下
                                                                f.close()
                                                                # 将im中的图片保存
                                                                pic_save(output_path=z_output_locate_path , preserve_exif=perserve_common_pic_exif)
                                                                transfer_modify_time(z_info , z_output_locate_path)
                                                            
                                                            except Exception as e:
                                                                try_remove(z_output_locate_path)# 删除可能输出的问题残留
                                                                log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 转换格式失败，详情：{e}")
                                                                continue
                                                            else:
                                                                log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 转换成功 √")
                                                        
                                                        else:
                                                            log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 的格式被排除或含有多个帧，不转换，原样导出")
                                                            
                                                            try:
                                                                # 如果在这行注释的地方用im.close()，f也会被关掉，所以没太好的方法，暂时留着吧
                                                                pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                                transfer_modify_time(z_info , z_copy_out_locate_path)
                                                            except Exception as e:
                                                                try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                                log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 提取失败，详情：{e}")
                                                                continue
                                                            else:
                                                                log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 导出成功 √")
                                            
                                            
                                            
                                            elif ("video/" in mimetype) or (tmp in {"mov","m4v","mp4","ts","mkv","flv"}):
                                                
                                                log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 为livp文件附带视频片段，原样导出")
                                                
                                                try:
                                                    pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                    transfer_modify_time(z_info , z_copy_out_locate_path)
                                                except Exception as e:
                                                    try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                    log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 提取失败，详情：{e}")
                                                    continue
                                                else:
                                                    log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 导出成功 √")
                                            
                                            else:
                                                log(f"▶▶▶       【{input_locate_path} ⇨ {z_file}】 为其他文件")
                                            
                                            successfully_processed_zfile_num += 1
                                    
                                    if successfully_processed_zfile_num != 2:
                                        log(f"×    【{input_locate_path}】 作为压缩包打开处理过程中出错，跳过")
                                        error_list.append(f"{input_locate_path}")
                                
                                else:
                                    log(f"◎        LIVP格式图片被设置为不转换，跳过【{input_locate_path}】")
                                    excluded_list.append(copy(input_locate_path))
                            
                            else:
                                log(f"▷▷       【{input_locate_path}】 为普通压缩包，跳过")
                                excluded_list.append(copy(input_locate_path))
                    
                    # 曾经遇到一个苹果动态照片mov和heic扩展名被互换的情况
                    # 尝试新增修正扩展名的功能
                    elif (mimetype == "video/quicktime") and (not input_locate_path.lower().endswith(".mov")):
                        mov_correct_output_name = make_single_out_name(output_locate_base,"mov")
                        
                        log(f"▷        【{input_locate_path}】 的扩展名应为【mov】")
                        log("▷▷    修正扩展名后保持原样硬链接或拷贝到输入文件所在文件夹")
                        transfer_file(input_locate_path, mov_correct_output_name, mf)
                        excluded_list.append(copy(input_locate_path))
                    
                    
                    # 顺带把mp4也尝试修正
                    elif (mimetype == "video/mp4") and (not input_locate_path.lower().endswith(".mp4")):
                        mp4_correct_output_name = make_single_out_name(output_locate_base,"mp4")
                        
                        log(f"▷        【{input_locate_path}】 的扩展名应为【mp4】")
                        log("▷▷    修正扩展名后保持原样硬链接或拷贝到输入文件所在文件夹")
                        transfer_file(input_locate_path, mp4_correct_output_name, mf)
                        excluded_list.append(copy(input_locate_path))
                    
                    
                    else:
                        log(f"▷        【{input_locate_path}】 不是图片文件，跳过")
                        excluded_list.append(copy(input_locate_path))
                
                progress_completed = 1
            
            
            
            # 目标路径是文件夹的情况 
            elif os.path.isdir(target_path):
                # 递归扫描所有文件和文件夹，文件夹列表用作建立输出的目录结构时使用
                os.chdir(target_path)
                for root , foldersets , filesets in os.walk("."):
                    for file in filesets:
                        filelist.append(f"{root}\\{file}"[2:])
                    for folder in foldersets:
                        folderlist.append(f"{root}\\{folder}"[2:])
                os.chdir("..")
                
                input_folder_name = os.path.basename(target_path)
                make_output_dir(input_folder_name) # 函数中决定了全局变量：output_folder_name = "xxxxxx"
                
                file_total = len(filelist)
                
                for file in filelist:
                    
                    log("\n")
                    
                    input_locate_path = f"{input_folder_name}\\{file}"
                    transfer_locate_path = f"{output_folder_name}\\{file}"
                    output_locate_base = f"{output_folder_name}\\{os.path.splitext(file)[0]}"
                    
                    if not os.path.getsize(input_locate_path):
                        log(f"▷     【{input_locate_path}】 是空文件")
                        log(f"▷▷    保持原样硬链接或拷贝到输出目录")
                        transfer_file(input_locate_path, transfer_locate_path)
                        excluded_list.append(copy(input_locate_path))
                        progress_completed += 1
                        continue
                    
                    try:
                        src_f = open(input_locate_path,mode="rb")
                        mf = my_custom_mmap(src_f.fileno(),length=0,access=mmap.ACCESS_READ)
                    except Exception as e:
                        with suppress(Exception): mf.close()
                        with suppress(Exception): src_f.close()
                        log(f"▷▷       【{input_locate_path}】 作为文件打开时出错，详情：{e}。\n           跳过，尝试保持原样硬链接或拷贝到输出目录")
                        transfer_file(input_locate_path, transfer_locate_path)
                        error_list.append(copy(input_locate_path))
                        progress_completed += 1
                        continue
                    
                    
                    
                    with src_f , mf :
                        
                        if mf.size() > filesize_limit:
                            log(f"▷     【{input_locate_path}】 超过文件大小限制（{filesize_limit}），跳过")
                            log(f"▷▷    保持原样硬链接或拷贝到输出目录")
                            transfer_file(input_locate_path, transfer_locate_path, mf)
                            excluded_list.append(copy(input_locate_path))
                            progress_completed += 1
                            continue
                        
                        try:
                            mimetype = get_type(mf)
                        except Exception as e:
                            log(f"×    【{input_locate_path}】 获取mimetype出错，详情：{e}")
                            log(f"▷▷    保持原样硬链接或拷贝到输出目录")
                            transfer_file(input_locate_path, transfer_locate_path, mf)
                            error_list.append(copy(input_locate_path))
                            progress_completed += 1
                            continue
                        
                        # 处理微信dat加密图片
                        if mimetype == "special/wechat_dat":
                            
                            if convert_wechat_dat:
                                
                                try:
                                    int_key , ext = wechat_xor_key
                                    wechat_output_name = f"{output_locate_base}.{ext}"
                                    convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                    
                                    with io.BytesIO( bytes( (i ^ int_key) for i in bytearray(mf) ) )  as  decoded_data_io:
                                        
                                        if wechat_dat_direct_output:
                                            pre_allocate_write_output_file( wechat_output_name , decoded_data_io )
                                            transfer_modify_time(input_locate_path , wechat_output_name)
                                        
                                        else:
                                            with Image.open(decoded_data_io) as im:
                                                
                                                if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                    # 需要转换，原来的文件数据没用了
                                                    # 确保im完全加载，然后关掉decoded_data_io节省内存
                                                    im.load()
                                                    # load方法自动关掉了decoded_data_io，这边只是重复确认一下
                                                    decoded_data_io.close()
                                                    # 将im中的图片保存
                                                    pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                                
                                                else:
                                                    log(f"🔔   微信dat图片【{input_locate_path}】因格式被排除或含有多个帧，虽已设置强制转换，但仍直接导出")
                                                    # 如果在这行注释的地方用im.close()，decoded_data_io也会被关掉，所以没太好的方法，暂时留着吧
                                                    pre_allocate_write_output_file( wechat_output_name , decoded_data_io )
                                                    transfer_modify_time(input_locate_path , wechat_output_name)
                                
                                
                                except Exception as e:
                                    try_remove(wechat_output_name)
                                    try_remove(convert_out_locate_path)
                                    log(f"×    微信dat图片【{input_locate_path}】转换格式失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                
                                else:
                                    log(f"√  微信dat图片【{input_locate_path}】转换成功")
                            
                            else:
                                log(f"◎        微信dat图片设置为不转换，跳过【{input_locate_path}】")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))
                        
                        
                        # 处理华为动态图片
                        elif mimetype == "special/hwlp":
                            
                            if convert_hwlp:
                                hwlp_jpg_output_path = f"{output_locate_base}.jpg"
                                hwlp_mp4_output_path = f"{output_locate_base}.mp4"
                                convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                
                                try:
                                    with io.BytesIO(mf[0:jpg_end_offset]) as jpg_io:
                                        # 导出图片
                                        if hwlp_direct_output:
                                            pre_allocate_write_output_file(hwlp_jpg_output_path , jpg_io)
                                            transfer_modify_time(input_locate_path , hwlp_jpg_output_path)
                                        else:
                                            with Image.open(jpg_io) as im :
                                                if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                    # 需要转换，原来的文件数据没用了
                                                    # 确保im完全加载，然后关掉jpg_io节省内存
                                                    im.load()
                                                    # load方法自动关掉了jpg_io，这边只是重复确认一下
                                                    jpg_io.close()
                                                    # 将im中的图片保存
                                                    pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                                else:
                                                    log(f"🔔   华为动态照片【{input_locate_path}】因格式被排除或含有多个帧，虽已设置强制转换，但仍直接导出")
                                                    # 如果在这行注释的地方用im.close()，jpg_io也会被关掉，所以没太好的方法，暂时留着吧
                                                    pre_allocate_write_output_file(hwlp_jpg_output_path , jpg_io)
                                                    transfer_modify_time(input_locate_path , hwlp_jpg_output_path)
                                    
                                    # 导出视频
                                    pre_allocate_write_output_file(hwlp_mp4_output_path , mf[mp4_start_offset:mp4_end_offset])
                                    transfer_modify_time(input_locate_path , hwlp_mp4_output_path)
                                
                                except Exception as e:
                                    try_remove(hwlp_jpg_output_path)# 删除可能输出的问题残留
                                    try_remove(hwlp_mp4_output_path)# 删除可能输出的问题残留
                                    try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                    
                                    log(f"× ×  【{input_locate_path}】 作为华为动态照片导出时失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                
                                else:
                                    log(f"√       华为动态照片【{input_locate_path}】导出成功")
                            
                            else:
                                log(f"◎        华为动态照片被设置为不转换，跳过【{input_locate_path}】")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))
                        
                        
                        # 处理SVG
                        elif mimetype == "special/svg":
                            
                            if convert_svg:
                                svg_output_name = f"{output_locate_base}.png"
                                convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                
                                try:
                                    
                                    with io.BytesIO() as tmp_io:
                                        #mf.seek(0 , os.SEEK_SET)
                                        # 这个mf（mmap.mmap）属实有点特殊，如果没有修改cairosvg库
                                        # 在这里如果不“seek(0)”的话，下面一行就读不到mf的文件数据
                                        # （我已经改了cairosvg库，所以注释掉了）
                                        cairosvg.svg2png(file_obj=mf , write_to=tmp_io)
                                        
                                        if svg_direct_output_png or (target_format=="PNG"):
                                            pre_allocate_write_output_file(svg_output_name , tmp_io)
                                            transfer_modify_time(input_locate_path , svg_output_name)
                                        else:
                                            with Image.open(tmp_io) as im:
                                                if (not has_only_one_frame(im)):
                                                    log(f"🔔   svg图片【{input_locate_path}】因含有多个帧，虽已设置强制转换，但仍直接导出")
                                                    pre_allocate_write_output_file(svg_output_name , tmp_io)
                                                    transfer_modify_time(input_locate_path , svg_output_name)
                                                else:
                                                    # 需要转换，原来的文件数据没用了
                                                    # 确保im完全加载，然后关掉tmp_io节省内存
                                                    im.load()
                                                    # load方法自动关掉了tmp_io，这边只是重复确认一下
                                                    tmp_io.close()
                                                        
                                                    
                                                    # exiftool支持从源SVG文件读取exif
                                                    if exif_enhance:
                                                        # cairosvg输出的PNG应该没有关于旋转的exif定义，所以这边不根据exif旋转图片了
                                                        with pic_save(preserve_exif=perserve_common_pic_exif , exif_rotate=False , output_to_memory_io=True) as exif_tmp_io:
                                                            # im已转出文件，可以关掉省内存了
                                                            im.close()
                                                            # 使用exiftool对exif进行增强转移
                                                            exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                                    else:
                                                        # cairosvg输出的PNG应该没有关于旋转的exif定义，所以这边不根据exif旋转图片了
                                                        pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif , exif_rotate=False)
                                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                
                                except Exception as e:
                                    try_remove(svg_output_name)# 删除可能输出的问题残留
                                    try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                    log(f"×    SVG图片【{input_locate_path}】转换格式失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                
                                else:
                                    log(f"√  SVG图片【{input_locate_path}】转换成功")
                            
                            
                            
                            else:
                                log(f"◎        SVG图片设置为不转换，跳过【{input_locate_path}】")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))
                        
                        
                        # 处理RAW格式
                        elif mimetype == "special/raw":
                            
                            if convert_raw:
                                convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                
                                with raw_structure:
                                    try:
                                        # 【use_camera_wb=True】：使用相机的白平衡
                                        rgb = raw_structure.postprocess(use_camera_wb=True)
                                    except Exception as e:
                                        log(f"× × ×    【{input_locate_path}】 raw文件在rawpy后处理中出错，详情：{e}")
                                        log("▷▷    保持原样硬链接或拷贝到输出目录")
                                        transfer_file(input_locate_path, transfer_locate_path, mf)
                                        error_list.append(copy(input_locate_path))
                                        progress_completed += 1
                                        continue
                                
                                try:
                                    im = Image.fromarray(rgb)
                                    im.load() # 确保矩阵删除释放内存前被完全加载
                                except Exception as e:
                                    # 释放内存，一个RAW格式图片转换出的矩阵尺寸应该很大
                                    with suppress(Exception): del rgb
                                    log(f"× × ×    【{input_locate_path}】 raw文件在pillow打开传递过来的向量中出错，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                else:
                                    # 释放内存，一个RAW格式图片转换出的矩阵尺寸应该很大
                                    with suppress(Exception): del rgb
                                
                                with im:
                                    try:
                                        if perserve_raw_pic_exif:
                                            # 传递过来的array中不含有exif，且上面rawpy后处理中已经根据raw中的exif，把图片翻转摆正了
                                            # 所以这边也不根据exif翻转图片，万一真的有exif传过来，再翻转就乱套了
                                            with pic_save(preserve_exif=False , exif_rotate=False , output_to_memory_io=True) as exif_tmp_io:
                                                # im已转出文件，可以关掉省内存了
                                                im.close()
                                                # 使用exiftool转移raw图片的exif
                                                exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                        else:
                                            # 传递过来的array中不含有exif，且上面rawpy后处理中已经根据raw中的exif，把图片翻转摆正了
                                            # 所以这边也不根据exif翻转图片，万一真的有exif传过来，再翻转就乱套了
                                            pic_save(output_path=convert_out_locate_path , preserve_exif=False , exif_rotate=False)
                                        transfer_modify_time(input_locate_path , convert_out_locate_path)
                                    
                                    except Exception as e:
                                        try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                        log(f"× × ×    【{input_locate_path}】 raw文件在pillow保存为“{target_format}”中出错，详情：{e}")
                                        log("▷▷    保持原样硬链接或拷贝到输出目录")
                                        transfer_file(input_locate_path, transfer_locate_path, mf)
                                        error_list.append(copy(input_locate_path))
                                        progress_completed += 1
                                        continue
                                    else:
                                        log(f"√ 【{input_locate_path}】 raw文件转换成功")
                            
                            
                            else:
                                with suppress(Exception): raw_structure.close()
                                log(f"◎        RAW格式图片被设置为不转换，跳过【{input_locate_path}】")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))
                                progress_completed += 1
                                continue
                        
                        
                        # 处理PSD图像
                        elif mimetype == "special/psd":
                            
                            if "PSD" not in runtime_excluded_format_set:
                                
                                convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                
                                try:
                                    mf.seek(0,0)
                                    im = PSDImage.open(mf)
                                except Exception as e:
                                    log(f"×    【{input_locate_path}】 作为PSD图片打开时失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                
                                try:
                                    im = im.composite(apply_icc=True)
                                except Exception as e:
                                    log(f"×    PSD图片【{input_locate_path}】处理失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue

                                try:
                                    if exif_enhance:
                                        # 将im中的图片保存
                                        with pic_save(preserve_exif=perserve_common_pic_exif , output_to_memory_io=True) as exif_tmp_io:
                                            # im已转出文件，可以关掉省内存了
                                            im.close()
                                            # 使用exiftool对exif进行增强转移
                                            exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                    else:
                                        # 将im中的图片保存
                                        pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                    transfer_modify_time(input_locate_path , convert_out_locate_path)
                                
                                except Exception as e:
                                    try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                    log(f"×    PSD图像【{input_locate_path}】转换格式失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                else:
                                    log(f"√ 【{input_locate_path}】 转换成功")
                            
                            else:
                                log(f"▷        图像【{input_locate_path}】的格式【PSD】被排除，不转换")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))

                        
                        
                        # 处理一般pillow可处理的图片
                        elif "image/" in mimetype:
                            
                            try:
                                im = Image.open(mf)
                            except Exception as e:
                                log(f"×    【{input_locate_path}】 作为图片打开时失败，详情：{e}")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                error_list.append(copy(input_locate_path))
                                progress_completed += 1
                                continue
                            
                            with im:
                                
                                if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                    convert_out_locate_path = f"{output_locate_base}.{target_ext}"
                                    
                                    try:
                                        if exif_enhance:
                                            # 将im中的图片保存
                                            with pic_save(preserve_exif=perserve_common_pic_exif , output_to_memory_io=True) as exif_tmp_io:
                                                # im已转出文件，可以关掉省内存了
                                                im.close()
                                                # 使用exiftool对exif进行增强转移
                                                exiftool_enhance_process(input_locate_path , exif_tmp_io , convert_out_locate_path)
                                        else:
                                            # 将im中的图片保存
                                            pic_save(output_path=convert_out_locate_path , preserve_exif=perserve_common_pic_exif)
                                        transfer_modify_time(input_locate_path , convert_out_locate_path)
                                    
                                    except Exception as e:
                                        try_remove(convert_out_locate_path)# 删除可能输出的问题残留
                                        log(f"×    【{input_locate_path}】 转换格式失败，详情：{e}")
                                        log("▷▷    保持原样硬链接或拷贝到输出目录")
                                        transfer_file(input_locate_path, transfer_locate_path, mf)
                                        error_list.append(copy(input_locate_path))
                                        progress_completed += 1
                                        continue
                                    else:
                                        log(f"√ 【{input_locate_path}】 转换成功")
                                
                                else:
                                    log(f"▷        【{input_locate_path}】 的格式被排除或含有多个帧，不转换")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    excluded_list.append(copy(input_locate_path))
                        
                        
                        # 处理PDF
                        elif mimetype == "application/pdf":
                            
                            if convert_pdf:
                                
                                crc32_set.clear()
                                pdf_output_main_dir = copy(transfer_locate_path)
                                
                                try:
                                    pdf_handle = pymupdf.Document(stream=mf , filetype="pdf")
                                except Exception as e:
                                    log(f"×    【{input_locate_path}】 作为PDF打开时失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                
                                try:
                                    with pdf_handle:
                                        # 创建和PDF同名（带扩展名）的输出文件夹
                                        # 之所以不去掉扩展名，是因为输入和输出文件夹的目录结构是相同的
                                        # 输入文件夹下难保会出现和pdf文件同名（无pdf扩展名）的文件夹，在输入文件夹下，是不冲突且合理的
                                        # 但在输出文件夹，这种情况下如果pdf的输出文件夹去掉了“.pdf”扩展名，就会产生冲突
                                        os.mkdir(pdf_output_main_dir)
                                        
                                        if pdf_mode in {0,1}:
                                            
                                            inside_img_output_path = f"{pdf_output_main_dir}\\PDF中嵌入的图片"
                                            os.mkdir(inside_img_output_path)
                                            
                                            
                                            pic_num = 1
                                            for xref in range(1 , pdf_handle.xref_length()):
                                                
                                                try:
                                                    img_dict = pdf_handle.extract_image(xref)
                                                except:
                                                    continue
                                                
                                                # 是图片、有文件数据、数据不重复
                                                if (file_data := img_dict.get('image',None)) \
                                                and (crc_value := crc32c.crc32c(file_data)) not in crc32_set:
                                                    crc32_set.add(crc_value)
                                                    ext = img_dict.get("ext","")
                                                    
                                                    del img_dict # 已经没用了
                                                    
                                                    try:
                                                        file_data = io.BytesIO(file_data)
                                                        with file_data:
                                                            if pdf_inside_pic_direct_output:
                                                                pre_allocate_write_output_file((single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{ext}")  ,  file_data)
                                                            else:
                                                                with Image.open(file_data) as im:
                                                                    if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                                        # 需要转换，原来的文件数据没用了
                                                                        # 确保im完全加载，然后关掉file_data节省内存
                                                                        im.load()
                                                                        # load方法自动关掉了file_data，这边只是重复确认一下
                                                                        file_data.close()
                                                                        # 将im中的图片保存
                                                                        pic_save(output_path = (single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{target_ext}") , preserve_exif=perserve_common_pic_exif)
                                                                    else:
                                                                        # 如果在这行注释的地方用im.close()，file_data也会被关掉，所以没太好的方法，暂时留着吧
                                                                        pre_allocate_write_output_file((single_pic_path:=f"{inside_img_output_path}\\{str(pic_num).zfill(3)}.{ext}")  ,  file_data)
                                                        transfer_modify_time(input_locate_path , single_pic_path)
                                                    except:
                                                        continue
                                                    else:
                                                        pic_num += 1
                                            
                                            if pic_num == 1:#无图片成功导出
                                                try_remove(inside_img_output_path)
                                        
                                        if pdf_mode in {0,2}:
                                            inside_page_render_output_path = f"{pdf_output_main_dir}\\PDF页面渲染图"
                                            os.mkdir(inside_page_render_output_path)
                                            mat = pymupdf.Matrix(pdf_page_render_zoom_ratio , pdf_page_render_zoom_ratio)
                                            
                                            page_num = 1
                                            for page in pdf_handle.pages():
                                                try:
                                                    page_pixmap = page.get_pixmap(matrix=mat)
                                                    with io.BytesIO() as tmp_io:
                                                        # 生成的页面渲染图中不带透明信息，除非上面一步get_pixmap()传入了“alpha=True”
                                                        # 详情请看：https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_pixmap
                                                        # 应该大概率不含exif信息（包括旋转信息）
                                                        page_pixmap.pil_save(fp=tmp_io , format=target_format , compress_level=png_compress_level )
                                                        pre_allocate_write_output_file((single_page_path:=f"{inside_page_render_output_path}\\{str(page_num).zfill(3)}.{target_ext}") , tmp_io)
                                                    transfer_modify_time(input_locate_path , single_page_path)
                                                except:
                                                    continue
                                                else:
                                                    page_num += 1
                                            
                                            if page_num == 1:#无页面成功渲染
                                                try_remove(inside_page_render_output_path)
                                
                                
                                except Exception as e:
                                    try_remove(pdf_output_main_dir)# 删除可能输出的问题残留
                                    log(f"×    PDF文件【{input_locate_path}】转换格式失败，详情：{e}")
                                    log("▷▷    保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    error_list.append(copy(input_locate_path))
                                    progress_completed += 1
                                    continue
                                else:
                                    log(f"√    PDF文件【{input_locate_path}】转换成功")
                            
                            else:
                                log(f"◎      PDF被设置为不转换，跳过【{input_locate_path}】")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                excluded_list.append(copy(input_locate_path))
                        
                        
                        # livp格式是zip压缩包
                        elif mimetype == "application/zip":
                            
                            zip_extra_path = os.path.dirname(output_locate_base) # file是相对路径，所以这里不能用：zip_extra_path = f"{output_folder_name}"
                            
                            try:
                                zfh = zipfile.ZipFile(mf)
                                z_object_list = zfh.infolist()
                                z_file_info_list = [i for i in z_object_list if i.is_file()] # 排除zip里的文件夹
                                log(f"▷        【{input_locate_path}】 满足zip文件条件，可能是livp文件")
                            except Exception as e:
                                with suppress(Exception): zfh.close()
                                log(f"×    【{input_locate_path}】 作为压缩包打开处理过程中出错，详情：{e}")
                                log("▷▷    保持原样硬链接或拷贝到输出目录")
                                transfer_file(input_locate_path, transfer_locate_path, mf)
                                error_list.append(copy(input_locate_path))
                                progress_completed += 1
                                continue
                            
                            with zfh:
                                
                                # 如果压缩包里存在1个文件夹，其下2个文件，“.namelist()”中个数就会是3个
                                if len(z_file_info_list) == len(z_object_list) == 2:
                                    
                                    log(f"▷▷       【{input_locate_path}】 满足livp文件数量为2个的特征")
                                    
                                    if convert_livp:
                                        successfully_processed_zfile_num = 0
                                        for z_info in z_file_info_list:
                                            z_file = z_info.filename
                                            z_name = os.path.splitext(z_file)[0]
                                            z_output_locate_path = f"{zip_extra_path}\\{z_name}.{target_ext}"
                                            z_copy_out_locate_path = f"{zip_extra_path}\\{z_file}"
                                            
                                            try:
                                                f = zfh.open(z_info)
                                            except Exception as e:
                                                log(f"×    【{input_locate_path} ⇨ {z_file}】 作为压缩包下的文件打开出错，已跳过，详情：{e}")
                                                continue
                                            
                                            with f:
                                                
                                                try:
                                                    mimetype = get_type(f)
                                                except Exception as e:
                                                    log(f"×    【{input_locate_path} ⇨ {z_file}】 获取mimetype出错，详情：{e}")
                                                    continue
                                                
                                                
                                                if ("image/" in mimetype) or ( (tmp := (os.path.splitext(z_file)[1][1:]).lower()) in {"jpg","jpeg","heic","heif","png","bmp","tiff"} ):
                                                    
                                                    if livp_direct_output:
                                                        try:
                                                            pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                            transfer_modify_time(z_info , z_copy_out_locate_path)
                                                        except Exception as e:
                                                            try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                            log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 直接输出失败，详情：{e}")
                                                            continue
                                                        else:
                                                            log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 直接输出成功 √")
                                                    
                                                    else:
                                                        try:
                                                            im = Image.open(f)
                                                        except Exception as e:
                                                            log(f"▷▷▷▷ × × ×【{input_locate_path} ⇨ {z_file}】 作为图片打开时出错，详情：{e}")
                                                            continue
                                                        
                                                        with im:
                                                            
                                                            if (im.format not in runtime_excluded_format_set) and has_only_one_frame(im):
                                                                log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 需要转换图片格式")
                                                                
                                                                try:
                                                                    # 需要转换，原来的文件数据没用了
                                                                    # 确保im完全加载，然后关掉f节省内存
                                                                    im.load()
                                                                    # load方法自动关掉了f，这边只是重复确认一下
                                                                    f.close()
                                                                    # 将im中的图片保存
                                                                    pic_save(z_output_locate_path , preserve_exif=perserve_common_pic_exif)
                                                                    transfer_modify_time(z_info , z_output_locate_path)
                                                                except Exception as e:
                                                                    try_remove(z_output_locate_path)# 删除可能输出的问题残留
                                                                    log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 转换格式失败，详情：{e}")
                                                                    continue
                                                                else:
                                                                    log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 转换成功 √")
                                                            
                                                            else:
                                                                log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 的格式被排除或含有多个帧，不转换，原样导出")
                                                                
                                                                try:
                                                                    # 如果在这行注释的地方用im.close()，f也会被关掉，所以没太好的方法，暂时留着吧
                                                                    pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                                    transfer_modify_time(z_info , z_copy_out_locate_path)
                                                                except Exception as e:
                                                                    try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                                    log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 提取失败，详情：{e}")
                                                                    continue
                                                                else:
                                                                    log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 导出成功 √")
                                                
                                                
                                                
                                                elif ("video/" in mimetype) or (tmp in {"mov","m4v","mp4","ts","mkv","flv"}):
                                                    
                                                    log(f"▷▷▷       【{input_locate_path} ⇨ {z_file}】 为livp文件附带视频片段，原样导出")
                                                    
                                                    try:
                                                        pre_allocate_write_output_file(z_copy_out_locate_path , f)
                                                        transfer_modify_time(z_info , z_copy_out_locate_path)
                                                    except Exception as e:
                                                        try_remove(z_copy_out_locate_path)# 删除可能输出的问题残留
                                                        log(f"  × × ×      【{input_locate_path} ⇨ {z_file}】 提取失败，详情：{e}")
                                                        continue
                                                    else:
                                                        log(f"▷▷▷▷      【{input_locate_path} ⇨ {z_file}】 导出成功 √")
                                                
                                                else:
                                                    log(f"▶▶▶       【{input_locate_path} ⇨ {z_file}】 为其他文件")
                                                
                                                successfully_processed_zfile_num += 1
                                        
                                        if successfully_processed_zfile_num != 2:
                                            log(f"×    【{input_locate_path}】 作为压缩包打开处理过程中出错，保持原样硬链接或拷贝到输出目录")
                                            transfer_file(input_locate_path, transfer_locate_path, mf)
                                            error_list.append(f"{input_locate_path}")
                                    
                                    else:
                                        log(f"◎        LIVP格式图片被设置为不转换，跳过【{input_locate_path}】")
                                        log("▷▷    保持原样硬链接或拷贝到输出目录")
                                        transfer_file(input_locate_path, transfer_locate_path, mf)
                                        excluded_list.append(copy(input_locate_path))
                                
                                else:
                                    log(f"▷▷       【{input_locate_path}】 为普通压缩包，保持原样硬链接或拷贝到输出目录")
                                    transfer_file(input_locate_path, transfer_locate_path, mf)
                                    excluded_list.append(copy(input_locate_path))
                        
                        
                        # 曾经遇到一个苹果动态照片mov和heic扩展名被互换的情况
                        # 尝试新增修正扩展名的功能
                        elif (mimetype == "video/quicktime") and (not input_locate_path.lower().endswith(".mov")):
                            mov_correct_output_name = f"{output_locate_base}.mov"
                            
                            log(f"▷        【{input_locate_path}】 的扩展名应为【mov】")
                            log("▷▷    修正扩展名后保持原样硬链接或拷贝到输出目录")
                            transfer_file(input_locate_path, mov_correct_output_name, mf)
                            excluded_list.append(copy(input_locate_path))
                        
                        
                        # 顺带把mp4也尝试修正
                        elif (mimetype == "video/mp4") and (not input_locate_path.lower().endswith(".mp4")):
                            mp4_correct_output_name = f"{output_locate_base}.mp4"
                            
                            log(f"▷        【{input_locate_path}】 的扩展名应为【mp4】")
                            log("▷▷    修正扩展名后保持原样硬链接或拷贝到输出目录")
                            transfer_file(input_locate_path, mp4_correct_output_name, mf)
                            excluded_list.append(copy(input_locate_path))
                        
                        
                        
                        
                        
                        else:
                            log(f"▷        【{input_locate_path}】 不是图片文件，保持原样硬链接或拷贝到输出目录")
                            transfer_file(input_locate_path, transfer_locate_path, mf)
                            excluded_list.append(copy(input_locate_path))
                    
                    
                    progress_completed += 1
            
            
            # 其他特殊情况
            else:
                log("❓　特殊路径类型，可能为符号链接或者其他特殊对象，软件不支持")
                error_list.append(copy(target_path))
            
            log("\n"*5)
            
            # 展示错误
            if error_list:
                log("❌　❌　❌　出错的文件有：\n　　　　" + ("\n　　　　".join(error_list)))
                log("\n"*5)
            # 展示转移中出错的文件
            if transfer_error_list:
                log("❌　❌　❌　跳过或出错后，在转移过程中出错的文件有：\n　　　　" + ("\n　　　　".join(transfer_error_list)))
                log("\n"*5)
            # 展示降级为拷贝后成功复制的文件
            if down_to_copy_list:
                log("⚠　⚠　⚠　降级为拷贝后，成功复制的文件有：\n　　　　" + ("\n　　　　".join(down_to_copy_list)))
                log("\n"*5)
            # 展示跳过的文件
            if excluded_list:
                log("✏　✏　✏　跳过的文件有：\n　　　　" + ("\n　　　　".join(excluded_list)))
                log("\n"*5)
        
        
        log("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝"+"\n"*15)
    
    
    
    except Exception as e:
        
        handle_critical_error(f"程序遭遇未预料到的错误，\n详情：{e}，\n程序终止")




# 合并日志
try:
    concat_log()
except Exception as e :
    handle_critical_error(f"合并日志出错，\n详情：{e}，\n程序终止" , log_handle_present=False)

print("★★★  处理完成  ★★★\n\n\n")
in_progress = False # 告诉进度展示线程该结束了
with suppress(Exception): close_up()


print("\n\n==========     【已退出】     ==========\n\n")
sys.exit(0)

