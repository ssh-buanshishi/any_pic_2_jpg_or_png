import os,sys,elevate,ctypes,subprocess,shutil,zipfile

if (ret:=os.system("pyinstaller --version >nul 2>nul")):
    print("找不到pyinstaller，可能未安装")
    print("\n")
    print("★★ 按任意键退出 ★★")
    os.system("@pause>nul")
    sys.exit(0)

# 程序所在文件夹
program_dir = os.path.dirname(__file__)
# 是否是管理员
is_admin = bool(ctypes.WinDLL("shell32.dll").IsUserAnAdmin())
if not is_admin:
    try:
        elevate.elevate()
    except:
        pass
    sys.exit(0)

os.chdir(f"{program_dir}\\..")


module_include_list = [
    "os","sys","platform","shutil",
    "datetime","time","threading","io",
    "mmap","re","subprocess","copy","configparser","pywin32-ctypes",
    "pymupdf",
    "psd_tools","scipy","skimage","numpy",
    "elevate","filetype",
    "pyautogui","pymsgbox",
    "win32api","win32con","win32file","win32pipe",
    "ctypes","pythoncom",
    "pillow_heif","func_timeout",
    "psutil","charset_mnbvc","chardet","crc32c",
    "rawpy","cairosvg","PIL","pillow_jpls",
]

include_cmd = " ".join([(f"--collect-all {i}") for i in module_include_list])

py_file_list = [
    "any_pic_2_jpg_runner.py",
    "any_pic_2_png_runner.py",
    "any_pic_2_jpg.py",
    "any_pic_2_png.py",
    "any_pic_2_UAC_skipper_installer.py",
    "any_pic_2_skip_UAC.py",
]

cmd_head = "pyinstaller --onedir --console --debug noarchive"
try:
    for i , py in enumerate(py_file_list):
        if i==0:
            cmd_line = f"{cmd_head}  {include_cmd}  --clean  {py}"
        else:
            cmd_line = f"{cmd_head}  --clean  {py}"
        subprocess.run(args=cmd_line,shell=True,check=True)
except:
    print("pyinstaller编译出错")
    print("\n")
    print("★★ 按任意键退出 ★★")
    os.system("@pause>nul")
    sys.exit(0)


try:
    print("====================================================")
    print("\n")
    print("【清理重复打包的库】")

    shutil.move(src="dist\\any_pic_2_png_runner\\any_pic_2_png_runner.exe",dst="dist\\any_pic_2_jpg_runner\\")
    shutil.move(src="dist\\any_pic_2_jpg\\any_pic_2_jpg.exe",dst="dist\\any_pic_2_jpg_runner\\")
    shutil.move(src="dist\\any_pic_2_png\\any_pic_2_png.exe",dst="dist\\any_pic_2_jpg_runner\\")
    shutil.move(src="dist\\any_pic_2_UAC_skipper_installer\\any_pic_2_UAC_skipper_installer.exe",dst="dist\\any_pic_2_jpg_runner\\")
    shutil.move(src="dist\\any_pic_2_skip_UAC\\any_pic_2_skip_UAC.exe",dst="dist\\any_pic_2_jpg_runner\\")

    shutil.rmtree("dist\\any_pic_2_png_runner")
    shutil.rmtree("dist\\any_pic_2_jpg")
    shutil.rmtree("dist\\any_pic_2_png")
    shutil.rmtree("dist\\any_pic_2_UAC_skipper_installer")
    shutil.rmtree("dist\\any_pic_2_skip_UAC")

    shutil.move("dist\\any_pic_2_jpg_runner",".\\")
    os.rename("any_pic_2_jpg_runner","bin")
    shutil.rmtree("dist")

    print("\n")
    print("====================================================")
    print("\n")
    print("【复制依赖的exe和dll到可执行文件的文件夹】")

    shutil.copytree("ExifTool","bin\\ExifTool\\")
    with zipfile.ZipFile("【必要的依赖文件】.zip") as f:
        f.extractall(path="bin")
    
    print("\n")
    print("====================================================")
    print("\n")
    print("【清理无用文件】")

    shutil.rmtree("build")
    os.system("del /f /q \"*.spec\" >nul")

    print("\n")
    print("====================================================")
    print("\n")
    print("【移动可执行文件的文件夹到上一级目录下】")

    shutil.move("bin","..\\")
    
except Exception as e:
    print(f"出错了，详情：{e}")
    print("\n")
    print("★★ 按任意键退出 ★★")
else:
    print(
    """
    打包完成，可执行文件位于上一级目录的“bin”文件夹下
    上一级目录里的启动器：“to_jpg.bat”和“to_png.bat”现在可以
    调用“any_pic_2_jpg.exe”和“any_pic_2_png.exe”了

    ★★ 按任意键退出 ★★

    """
    )
finally:
    os.system("@pause>nul")
    sys.exit(0)