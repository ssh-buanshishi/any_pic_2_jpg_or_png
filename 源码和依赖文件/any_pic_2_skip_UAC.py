import os, sys, ctypes, win32pipe, win32file, win32api, win32con
import threading, time, psutil, subprocess, elevate, io

# 程序所在文件夹
program_dir = os.path.dirname(__file__)
# 程序exe名（供错误弹窗标题使用）
app_exe = os.path.basename(sys.argv[0])
# 当前登录的用户
current_user = os.getlogin()
# 启动命名管道来传输启动命令行时，使用的管道参数
PIPE_NAME = '\\\\.\\pipe\\any_pic_2_filepath_data_transfer_pipe'
PIPE_BUFFER_SIZE = 32768
#connected = False
file_handle = None
wait_loop = True


# 等待发送端【any_pic_2_jpg.exe】（server端）的管道就位
def try_get_pipe() -> None:
    global file_handle
    
    while wait_loop:
        try:
            file_handle = win32file.CreateFile(
                PIPE_NAME,
                win32file.GENERIC_READ,
                0,
                None,
                win32file.OPEN_EXISTING,
                win32file.FILE_ATTRIBUTE_NORMAL,
                None,
            )
            break
        except:
            time.sleep(0.1)
    
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


try:
    os.chdir(program_dir)
    if (len(sys.argv) == 2) and (sys.argv[1] == "pipe_on"):
        
        if ctypes.WinDLL("shell32.dll").IsUserAnAdmin():
            data_collecter = bytearray()
            
            # 等待连接，超时时间为6秒
            t = threading.Thread(target=try_get_pipe , daemon=True)
            t.start()
            t.join(timeout=6)

            wait_loop = False
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
                
                # 启动runner
                subprocess.run(args=cmd_list,shell=True)

            
            else:
                win32api.MessageBox(0 , "发送管道准备超时\n可能【any_pic_2_jpg/png.exe】未启动\n程序终止" , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
        
        else:
            win32api.MessageBox(0 , "错误，未取得管理员权限\n程序终止" , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))
    
    else:
        win32api.MessageBox(0 , "输入参数错误，请勿单独启动此exe\n程序终止" , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND))

except:
    pass


sys.exit(0)