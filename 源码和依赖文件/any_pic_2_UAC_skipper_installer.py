import elevate,ctypes,os,sys,win32api,win32con,platform,datetime

# 程序exe名
app_exe = os.path.basename(sys.argv[0])
# 如果不是管理员，提升权限，等待提升权限后的子进程结束后，退出
# 提升权限后，会跳过这个if执行下面的
if not bool(ctypes.WinDLL("shell32.dll").IsUserAnAdmin()):
    try:
        elevate.elevate()
    except:
        win32api.MessageBox(0 , "安装跳过UAC弹窗的计划任务需要管理员权限，\n但似乎被拒绝了" , app_exe , (win32con.MB_OK | win32con.MB_ICONERROR | win32con.MB_TOPMOST | win32con.MB_SETFOREGROUND) )
    finally:
        # elevate因为被修改了，提升权限完成后要立刻退出，
        # 否则会以【非管理员】的方式执行之后的指令
        sys.exit(0)


xml_template = """<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
    <RegistrationInfo>
        <Date>【_create_time_】</Date>
        <Author>By：不谙世事的雨滴【吾爱破解论坛】</Author>
        <Description>帮助【any_pic_2_jpg_or_png】跳过UAC弹窗的计划任务</Description>
    </RegistrationInfo>
    <Triggers />
    <Principals>
        <Principal id="Author">
            <UserId>【_pc_user_name_】</UserId>
            <LogonType>InteractiveToken</LogonType>
            <RunLevel>HighestAvailable</RunLevel>
        </Principal>
    </Principals>
    <Settings>
        <MultipleInstancesPolicy>StopExisting</MultipleInstancesPolicy>
        <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
        <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
        <AllowHardTerminate>false</AllowHardTerminate>
        <StartWhenAvailable>true</StartWhenAvailable>
        <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
        <IdleSettings>
            <StopOnIdleEnd>false</StopOnIdleEnd>
            <RestartOnIdle>false</RestartOnIdle>
        </IdleSettings>
        <AllowStartOnDemand>true</AllowStartOnDemand>
        <Enabled>true</Enabled>
        <Hidden>false</Hidden>
        <RunOnlyIfIdle>false</RunOnlyIfIdle>
        <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
        <UseUnifiedSchedulingEngine>false</UseUnifiedSchedulingEngine>
        <WakeToRun>false</WakeToRun>
        <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
        <Priority>7</Priority>
    </Settings>
    <Actions Context="Author">
        <Exec>
            <Command>cmd</Command>
            <Arguments>/C start \"title\" /D \"【_start_path_】\" any_pic_2_skip_UAC.exe pipe_on</Arguments>
        </Exec>
    </Actions>
</Task>"""


start_path = f"{os.path.dirname(__file__)}\\"
current_user = os.getlogin()
pc_user_name = f"{platform.node()}\\{current_user}"


xml_template = xml_template.replace("【_start_path_】",start_path)
xml_template = xml_template.replace("【_pc_user_name_】",pc_user_name)

system_tmp_path = os.environ.get("TEMP",".")
xml_temp_output = f"{system_tmp_path}\\any_pic_2_skip_UAC.xml"



os.system("title 绕过UAC弹窗计划任务【安装 / 卸载】")
choice = input(
"""
★★ 注意，装卸操作仅限于【当前登录的用户】 ★★

直接按回车：                【安装】绕过UAC弹窗的计划任务
输入“1” 或 大小写字母“I”： 【安装】绕过UAC弹窗的计划任务
输出“2” 或 大小写字母“U”： 【卸载】绕过UAC弹窗的计划任务

请输入后按回车执行："""
)



if choice.upper() in {"","1","2","I","U"}:
    os.system(f"schtasks /End /TN \"\\any_pic_2_skip_UAC_for_user--{current_user}\" >nul 2>nul")
    os.system(f"schtasks /Delete /TN \"\\any_pic_2_skip_UAC_for_user--{current_user}\" /F >nul 2>nul")
    print("\n尝试卸载（旧的计划任务）完成\n")

if choice.upper() in {"","1","I"}:
    # 获取创建时间
    create_time = datetime.datetime.now().isoformat()
    xml_template = xml_template.replace("【_create_time_】",create_time)
    # 写出xml文件供调用
    with open(xml_temp_output , mode="wt" , encoding="utf-16" , errors="replace" , newline="\r\n") as f:
        f.write(xml_template)
    # 安装计划任务
    ret = os.system(f"cls&&schtasks /Create /TN \"\\any_pic_2_skip_UAC_for_user--{current_user}\" /XML \"{xml_temp_output}\"")
    if ret:
        print("\n❌ 绕过UAC弹窗的计划任务【安装失败】 ❌\n")
    else:
        print("\n★ 绕过UAC弹窗的计划任务【安装成功】！ ★\n")

try:
    os.remove(xml_temp_output)
except:
    pass


print("按任意键退出")
os.system("@pause>nul")
sys.exit(0)