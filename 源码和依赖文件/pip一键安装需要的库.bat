@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem ���ļ��ɽ�������չ����.txt��ɾ������Ϊ��.bat�����У���������ǰ�鿴��requirements.txt��ȷ�ϡ�
rem �����Ҫ�ض��汾��python���ߵͰ汾����32��64λ�ĸ����ض�python�����������޸��·���pip����

setlocal enabledelayedexpansion
cd /d "%~dp0"

pip install -r "requirements.txt" -U -i "https://mirrors.aliyun.com/pypi/simple/"
pause
exit 0