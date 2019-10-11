import win32com.client
import pyautogui
import dnf_type

dnf = win32com.client.Dispatch("dm.dmsoft")
result = dnf.Reg("wlasd56883401415f4af81067979d140b2e8c5e42", '1.10')
qq_id=1
if result == 1:
    # 注册成功
    print("注册成功")
    dnf_type.dqandpath(dnf, qq_id) # 自动上号函数
else:
    print("注册失败")


