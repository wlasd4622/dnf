import win32com.client
import pyautogui
import dnf_type
qq_id = 1 
dnf = win32com.client.Dispatch("dm.dmsoft")
dnf.Reg("151080018559ddcb89689090b60c7af5266c699ece5", "0001")
dnf_type.dqandpath(dnf, qq_id) # 自动上号函数

