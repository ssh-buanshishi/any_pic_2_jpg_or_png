@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem It is recommended to use "Visual Studio Code" to edit this file.
rem д�����ģ���ֹ���±���硣

setlocal enabledelayedexpansion
cd /d "%~dp0"

rem --collect-all pymupdf --collect-all rawpy --collect-all cairosvg ^
rem --collect-all PIL --collect-all pillow_heif --collect-all pillow_jpls ^
rem --collect-all pySMART --collect-all pythoncom --collect-all wmi ^
rem --collect-all psutil --collect-all filetype --collect-all configparser ^

pyinstaller --onedir --console --debug noarchive ^
 ^
--collect-data PIL           --collect-data pillow_heif      --collect-data pillow_jpls ^
--collect-data pymupdf       --collect-data rawpy            --collect-data cairosvg ^
--collect-data pySMART       --collect-data pythoncom        --collect-data wmi ^
--collect-data tkinter       --collect-data pyautogui        --collect-data pymsgbox ^
--collect-data pywin32       --collect-data pywin32-ctypes ^
--collect-data configparser  --collect-data filetype         --collect-data crc32c ^
 ^
--collect-binaries PIL           --collect-binaries pillow_heif     --collect-binaries pillow_jpls ^
--collect-binaries pymupdf       --collect-binaries rawpy           --collect-binaries cairosvg ^
--collect-binaries pySMART       --collect-binaries pythoncom       --collect-binaries wmi ^
--collect-binaries tkinter       --collect-binaries pyautogui       --collect-data pymsgbox ^
--collect-binaries pywin32       --collect-binaries pywin32-ctypes ^
--collect-binaries configparser  --collect-binaries filetype        --collect-binaries crc32c ^
 ^
--workpath ".\any_pic_2_jpg-build" ^
--clean "any_pic_2_jpg.py"

pyinstaller --onedir --console --debug noarchive ^
 ^
--collect-data PIL           --collect-data pillow_heif      --collect-data pillow_jpls ^
--collect-data pymupdf       --collect-data rawpy            --collect-data cairosvg ^
--collect-data pySMART       --collect-data pythoncom        --collect-data wmi ^
--collect-data tkinter       --collect-data pyautogui        --collect-data pymsgbox ^
--collect-data pywin32       --collect-data pywin32-ctypes ^
--collect-data configparser  --collect-data filetype         --collect-data crc32c ^
 ^
--collect-binaries PIL           --collect-binaries pillow_heif     --collect-binaries pillow_jpls ^
--collect-binaries pymupdf       --collect-binaries rawpy           --collect-binaries cairosvg ^
--collect-binaries pySMART       --collect-binaries pythoncom       --collect-binaries wmi ^
--collect-binaries tkinter       --collect-binaries pyautogui       --collect-data pymsgbox ^
--collect-binaries pywin32       --collect-binaries pywin32-ctypes ^
--collect-binaries configparser  --collect-binaries filetype        --collect-binaries crc32c ^
 ^
--workpath ".\any_pic_2_png-build" ^
--clean "any_pic_2_png.py"

echo ====================================================
echo.
echo �������ظ�����Ŀ⡿
move /Y "dist\any_pic_2_png\any_pic_2_png.exe" "dist\any_pic_2_jpg\" >nul
rd /s /q "dist\any_pic_2_png"
ren "dist\any_pic_2_jpg" "bin" >nul
move /Y "dist\bin" ".\" >nul
rd /s /q "dist"

echo.
echo ������������exe��dll����ִ���ļ����ļ��С�
copy /Y "*.dll" "bin\" >nul
xcopy "ExifTool" "bin\ExifTool\" /Y /E /Q >nul
xcopy "SmartMonTools" "bin\SmartMonTools\" /Y /E /Q >nul

echo.
echo �����������ļ���
rd /s /q ".\any_pic_2_jpg-build"
rd /s /q ".\any_pic_2_png-build"
del /f /q ".\any_pic_2_jpg.spec" >nul
del /f /q ".\any_pic_2_png.spec" >nul

echo.
echo ���ƶ���ִ���ļ����ļ��е���һ��Ŀ¼�¡�
move /Y ".\bin" "..\"

echo.
echo �����ɣ���ִ���ļ�λ����һ��Ŀ¼�ġ�bin���ļ�����
echo ��һ��Ŀ¼�������������to_jpg.bat���͡�to_png.bat�����ڿ���
echo ���á�any_pic_2_jpg.exe���͡�any_pic_2_png.exe����
echo.
echo ��� ��������˳� ���
echo.
@pause>nul
exit 0