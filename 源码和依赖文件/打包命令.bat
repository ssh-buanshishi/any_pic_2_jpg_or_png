@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem It is recommended to use "Visual Studio Code" to edit this file.
rem 写点中文，防止记事本抽风。

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
echo 【清理重复打包的库】
move /Y "dist\any_pic_2_png\any_pic_2_png.exe" "dist\any_pic_2_jpg\" >nul
rd /s /q "dist\any_pic_2_png"
ren "dist\any_pic_2_jpg" "bin" >nul
move /Y "dist\bin" ".\" >nul
rd /s /q "dist"

echo.
echo 【复制依赖的exe和dll到可执行文件的文件夹】
copy /Y "*.dll" "bin\" >nul
xcopy "ExifTool" "bin\ExifTool\" /Y /E /Q >nul
xcopy "SmartMonTools" "bin\SmartMonTools\" /Y /E /Q >nul

echo.
echo 【清理无用文件】
rd /s /q ".\any_pic_2_jpg-build"
rd /s /q ".\any_pic_2_png-build"
del /f /q ".\any_pic_2_jpg.spec" >nul
del /f /q ".\any_pic_2_png.spec" >nul

echo.
echo 【移动可执行文件的文件夹到上一级目录下】
move /Y ".\bin" "..\"

echo.
echo 打包完成，可执行文件位于上一级目录的“bin”文件夹下
echo 上一级目录里的启动器：“to_jpg.bat”和“to_png.bat”现在可以
echo 调用“any_pic_2_jpg.exe”和“any_pic_2_png.exe”了
echo.
echo ★★ 按任意键退出 ★★
echo.
@pause>nul
exit 0