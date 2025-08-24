import os,sys,subprocess,shutil,zipfile

try:
    # 检查python版本是否在3.8以上
    if sys.version_info.major < 3:
        raise Exception("Python 版本过低，至少要3.8")
    if (sys.version_info.major == 3) and (sys.version_info.minor) < 8:
        raise Exception("Python 版本过低，至少要3.8")
    
    print("为了exe和依赖项的文件布局的需要，\n检查pyinstaller版本是否支持命令【--contents-directory=】中……\n\n")
    
    # 检查pyinstaller版本是否在6.1.0及以上
    # 获取命令行结果
    stdout, stderr = b"",b""
    process = subprocess.Popen(args="pyinstaller --version", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # 获取命令输出结果
    stdout, stderr = process.communicate()
    if process.returncode or stderr:
        raise Exception("运行【pyinstaller --version】命令时出错，检查是否安装了pyinstaller")
    if not stdout:
        raise Exception("pyinstaller运行【--version】命令时未输出结果")
    # 转换输出结果和判断版本
    version_num_list = stdout.decode("utf-8",errors="replace").strip().split(".")
    if (len(version_num_list) < 3):
        raise Exception("pyinstaller版本输出不正常，分割点小于3个")
    for i,num in enumerate(version_num_list):
        if not num.isdigit():
            raise Exception("pyinstaller版本输出不正常，分割点之间出现非数字")
        else:
            version_num_list[i] = int(num)
    if version_num_list[0] < 6:
        raise Exception("pyinstaller版本过低，至少要达到6.1.0")
    elif version_num_list[0] == 6 and version_num_list[1] < 1:
        raise Exception("pyinstaller版本过低，至少要达到6.1.0")
    os.system("cls")

except Exception as e:
    print(str(e))
    print("\n")
    print("★★ 按任意键退出 ★★")
    os.system("@pause>nul")
    sys.exit(2)


# 程序所在文件夹
program_dir = os.path.dirname(__file__)

os.chdir(f"{program_dir}\\..")


module_include_list = [
    "os","sys","shutil",
    "datetime","time","threading","io",
    "mmap","re","subprocess","copy","configparser","pywin32-ctypes",
    "pymupdf",
    "psd_tools","scipy","skimage","numpy",
    "filetype",
    "win32api","win32con","win32file","win32gui","win32print"
    "ctypes",
    "pillow_heif",
    "psutil","charset_mnbvc","crc32c",
    "rawpy","cairosvg","PIL","pillow_jpls",
]

include_cmd = " ".join([(f"--collect-all {i}") for i in module_include_list])

py_file_list = [
    "any_pic_2_jpg.py",
    "any_pic_2_png.py",
]
# 选择了老版pyinstaller的icon，不然win7下可能会显示不出来
cmd_head = "pyinstaller --onedir --console --debug noarchive --icon icon-console.ico --contents-directory=."
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

    shutil.move(src="dist\\any_pic_2_png\\any_pic_2_png.exe",dst="dist\\any_pic_2_jpg\\")

    shutil.rmtree("dist\\any_pic_2_png")

    shutil.move("dist\\any_pic_2_jpg",".\\")
    os.rename("any_pic_2_jpg","bin")
    shutil.rmtree("dist")

    print("\n")
    print("====================================================")
    print("\n")
    print("【复制依赖的exe和dll到可执行文件的文件夹】")

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