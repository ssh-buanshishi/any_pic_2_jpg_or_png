@echo off
rem -------------------- encoding:GBK (ANSI) ---------------------
rem ��������ǰ�鿴��requirements.txt��ȷ�ϡ�
rem �����Ҫ�ض��汾��python���ߵͰ汾����32��64λ�ĸ����ض�python�����������޸��·���pip����

setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ��������ǰ�鿴��requirements.txt��ȷ���Ƿ���Ҫ�����Լ���Ҫ�޸Ļ򾫼�
echo �����Ҫ�ض��汾��python���ߵͰ汾����32��64λ�ĸ����ض�python����
echo ���˳���bat����������б༭�޸��·���pip����
echo.
echo ��� ��ȷ���������밴�������           ��� 
echo ��� ����Ҫ��ֹ�˳����밴���Ͻ��˳���ť����� 

@pause>nul

pip install -r "requirements.txt" -U -i "https://mirrors.aliyun.com/pypi/simple/"

pause
exit 0