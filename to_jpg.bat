@echo off
rem -------------------- encoding:GB 2312(ANSI) ---------------------
rem It is recommended to use "Visual Studio Code" to edit this file.
rem дһ�����ģ���ֹ���±����
setlocal enabledelayedexpansion

cd /d "%~dp0"
cd /d "bin"

rem ֱ���ڵ�ǰcmd�������У��������´���
rem start "ת����" /B "any_pic_2_jpg.exe" %*
".\any_pic_2_jpg.exe" %*
exit 0