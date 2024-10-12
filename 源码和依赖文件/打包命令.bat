@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem It is recommended to use "Visual Studio Code" to edit this file.
rem 写点中文，防止记事本抽风。

setlocal enabledelayedexpansion
cd /d "%~dp0"


pyinstaller --onedir --console --debug noarchive ^
 ^
--collect-all psd_tools     --collect-all PyMuPDF ^
--collect-all os            --collect-all sys               --collect-all platform         --collect-all shutil          ^
--collect-all datetime      --collect-all time              --collect-all threading        --collect-all io              ^
--collect-all mmap          --collect-all re                --collect-all subprocess       --collect-all copy            ^
--collect-all elevate       --collect-all configparser      --collect-all filetype         --collect-all tkinter         ^
--collect-all pyautogui     --collect-all pymsgbox          --collect-all pywin32          --collect-all pywin32-ctypes  ^
--collect-all ctypes        --collect-all pythoncom         --collect-all pillow_heif      --collect-all func_timeout    ^
--collect-all psutil        --collect-all charset_mnbvc     --collect-all chardet          --collect-all crc32c          ^
--collect-all rawpy         --collect-all cairosvg          --collect-all PIL              --collect-all pillow_jpls     ^
--clean  "any_pic_2_jpg_runner.py"


pyinstaller --onedir --console --debug noarchive --clean "any_pic_2_png_runner.py"

pyinstaller --onedir --console --debug noarchive --clean "any_pic_2_jpg.py"

pyinstaller --onedir --console --debug noarchive --clean "any_pic_2_png.py"

pyinstaller --onedir --console --debug noarchive --clean "any_pic_2_UAC_skipper_installer.py"

pyinstaller --onedir --console --debug noarchive --clean "any_pic_2_skip_UAC.py"



echo ====================================================
echo.
echo 【清理重复打包的库】
move /Y "dist\any_pic_2_png_runner\any_pic_2_png_runner.exe" "dist\any_pic_2_jpg_runner\" >nul
move /Y "dist\any_pic_2_jpg\any_pic_2_jpg.exe" "dist\any_pic_2_jpg_runner\" >nul
move /Y "dist\any_pic_2_png\any_pic_2_png.exe" "dist\any_pic_2_jpg_runner\" >nul
move /Y "dist\any_pic_2_UAC_skipper_installer\any_pic_2_UAC_skipper_installer.exe" "dist\any_pic_2_jpg_runner\" >nul
move /Y "dist\any_pic_2_skip_UAC\any_pic_2_skip_UAC.exe" "dist\any_pic_2_jpg_runner\" >nul

rd /s /q "dist\any_pic_2_png_runner"
rd /s /q "dist\any_pic_2_jpg"
rd /s /q "dist\any_pic_2_png"
rd /s /q "dist\any_pic_2_UAC_skipper_installer"
rd /s /q "dist\any_pic_2_skip_UAC"

ren "dist\any_pic_2_jpg_runner" "bin" >nul
move /Y "dist\bin" ".\" >nul
rd /s /q "dist"

echo.
echo 【复制依赖的exe和dll到可执行文件的文件夹】
copy /Y "*.dll" "bin\" >nul
xcopy "ExifTool" "bin\ExifTool\" /Y /E /Q >nul
xcopy "SmartMonTools" "bin\SmartMonTools\" /Y /E /Q >nul

echo.
echo 【清理无用文件】
rd /s /q "build"
del /f /q "*.spec" >nul

echo.
echo 【移动可执行文件的文件夹到上一级目录下】
move /Y "bin" "..\"

echo.
echo 打包完成，可执行文件位于上一级目录的“bin”文件夹下
echo 上一级目录里的启动器：“to_jpg.bat”和“to_png.bat”现在可以
echo 调用“any_pic_2_jpg.exe”和“any_pic_2_png.exe”了
echo.
echo ★★ 按任意键退出 ★★
echo.
@pause>nul
exit 0