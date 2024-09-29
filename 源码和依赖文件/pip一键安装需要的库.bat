@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem 本文件可将最后的扩展名“.txt”删除，变为“.bat”运行，建议运行前查看“requirements.txt”确认。
rem 如果需要特定版本的python（高低版本或者32、64位的各种特定python），请自行修改下方的pip命令

setlocal enabledelayedexpansion
cd /d "%~dp0"

pip install -r "requirements.txt" -U -i "https://mirrors.aliyun.com/pypi/simple/"
pause
exit 0