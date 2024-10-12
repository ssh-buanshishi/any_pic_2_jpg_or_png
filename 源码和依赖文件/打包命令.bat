@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem It is recommended to use "Visual Studio Code" to edit this file.
rem д�����ģ���ֹ���±���硣

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
echo �������ظ�����Ŀ⡿
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
echo ������������exe��dll����ִ���ļ����ļ��С�
copy /Y "*.dll" "bin\" >nul
xcopy "ExifTool" "bin\ExifTool\" /Y /E /Q >nul
xcopy "SmartMonTools" "bin\SmartMonTools\" /Y /E /Q >nul

echo.
echo �����������ļ���
rd /s /q "build"
del /f /q "*.spec" >nul

echo.
echo ���ƶ���ִ���ļ����ļ��е���һ��Ŀ¼�¡�
move /Y "bin" "..\"

echo.
echo �����ɣ���ִ���ļ�λ����һ��Ŀ¼�ġ�bin���ļ�����
echo ��һ��Ŀ¼�������������to_jpg.bat���͡�to_png.bat�����ڿ���
echo ���á�any_pic_2_jpg.exe���͡�any_pic_2_png.exe����
echo.
echo ��� ��������˳� ���
echo.
@pause>nul
exit 0