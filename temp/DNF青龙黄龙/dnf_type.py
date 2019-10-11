import os
import pyautogui

def mou_mv_click(dnf, mdx, mdy, time):
    """
    # param: mdx 目标x
    # param: mdy 目标y
    # param: time 延时时间
    """
    dnf.Delay(50)
    dnf.MoveTo(mdx, mdy)
    dnf.Delay(time)
    dnf.LeftClick()
    dnf.Delay(time)

def find_picture(dnf, fwx, fwy, fwx1, fwy1, name):
    """
    # param: fwx 找图范围左上x坐标
    # param: fwy 找图范围左上y坐标
    # param: fwx1 找图范围右下x坐标
    # param: fwy1 找图范围右下y坐标
    # param: name 指定查找的图片名
    # param: ret 返回值为元组
    """
    intx = 0
    inty = 0
    ret = dnf.FindPic(fwx, fwy, fwx1, fwy1, name, "000000", 0.9, 0, intx, inty)
    return ret[0]

def find_color(dnf, fwx, fwy, fwx1, fwy1, name, color):
    """
    # param: fwx 找色范围左上x坐标
    # param: fwy 找色范围左上y坐标
    # param: fwx1 找色范围右下x坐标
    # param: fwy1 找色范围右下y坐标
    # param: color 指定查找的颜色值
    """
    intx = 0
    inty = 0
    ret = dnf.FindColor(fwx, fwy, fwx1, fwy1, color, 1.0, 0, intx, inty)
    return ret[0]
    
def find_str(dnf, fwx, fwy, fwx1, fwy1, name, color):
    """
    # param: fwx 找字范围左上x坐标
    # param: fwy 找字范围左上y坐标
    # param: fwx1 找字范围右下x坐标
    # param: fwy1 找字范围右下y坐标
    # param: name 指定找字字符串
    # param: color 指定查找的颜色值
    """
    intx = 0
    inty = 0
    ret = dnf.FindStr(fwx, fwy, fwx1, fwy1, name, color, 1.0, intx, inty)
    return ret[0]
def key_type(dnf, type, vk_code = "", key_str = "", time = ""):
    """
    # param: type 指定键盘操作的类型 0 - 键盘按下 1 - 键盘按键 4 - 键盘弹起 5 - 键盘发送字符串
    # param: vk_code 指定键盘键码
    # param: key_str 指定虚拟键key_str
    # param: time 指定延时时间
    """
    if type == 0:
        dnf.KeyDown(vk_code)
    elif type == 1:
        dnf.KeyPress(vk_code)
    elif type == 2:
        dnf.KeyDownChar(key_str)
    elif type == 3:
        dnf.KeyPressChar(key_str)
    elif type == 4:
        dnf.KeyUp(vk_code)
    elif type == 5:
        dnf.KeyPressStr(key_str,time)
    elif type == 6:
        dnf.KeyUpChar(key_str)
    dnf.Delay(time)
def dl(dnf, pic_path, qq_number, password):
    i = True   
    while i == True:
        hwnd = dnf.FindWindow("","地下城与勇士登录程序") 
        if hwnd > 0:
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            ret = dnf.GetWindowRect(hwnd, x1, y1, x2, y2)
            dnf.SetWindowState(hwnd, 8)
            print("DNF启动成功")
            dnf.Delay(1000)
            while i == True:
                if find_picture(dnf, ret[1], ret[2], ret[3], ret[4], pic_path + 'zt.bmp') >= 0:
                    dnf.Delay(1000)
                    mou_mv_click(dnf, ret[1] + 835, ret[2] + 498, 500)
                    while i == True:
                        if find_str(dnf, ret[1] + 937, ret[2] + 313, ret[1] + 1153, ret[2] + 389, "gb", "dad7b7-000000") >= 0:
                            dnf.Delay(1000)
                            mou_mv_click(dnf, ret[1] + 1116, ret[2] + 325, 500)
                            n = 11
                            while n >= 1:
                                key_type(dnf, 1, 8, time = 50)
                                n = n - 1
                            key_type(dnf, 5, key_str = qq_number, time = 50)
                            dnf.Delay(1000)
                            key_type(dnf, 1, 9, time = 50)
                            dnf.Delay(1000)
                            dnf.SetSimMode(2)
                            dnf.Delay(500)
                            key_type(dnf, 5, key_str = password, time = 50)
                            dnf.Delay(500)
                            mou_mv_click(dnf, ret[1] + 1049, ret[2] + 500, 500)
                            i = False
def dqandpath(dnf, qq_id):
    if dnf.CheckFontSmooth() == 1:
        dnf.DisableFontSmooth()
        print("程序关闭系统平滑")
    path = os.path.abspath("DNF青龙黄龙.py")
    pic_path = path.split(sep = "DNF青龙黄龙.py", maxsplit = 1)[0] + 'Picture\\'
    dnf.SetDict(0, path.split(sep = "DNF青龙黄龙.py", maxsplit = 1)[0] + '配置\\dnf.txt')
    dnf_path = dnf.ReadIni("DNF路径","路径", path.split(sep = "DNF青龙黄龙.py", maxsplit = 1)[0] + '配置\\配置.ini')
    qq_path = dnf.ReadIni("账号密码",qq_id, path.split(sep = "DNF青龙黄龙.py", maxsplit = 1)[0] + '配置\\配置.ini')
    qq_number = qq_path.split(sep = "|", maxsplit = 2)[0]
    password = qq_path.split(sep = "|", maxsplit = 2)[1]
    dq = qq_path.split(sep = "|", maxsplit = 2)[2]
    dq_path = dnf_path.split(sep = "Client.exe", maxsplit = 1)[0] + 'config\\LoginQ.dat'
    if dq == "广东1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "1", dq_path)
    elif  dq ==  "广东2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "15", dq_path)
    elif  dq ==  "广东3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "22", dq_path)
    elif  dq ==  "广东4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "45", dq_path)   
    elif  dq ==  "广东5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "52", dq_path)
    elif  dq ==  "广东6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "65", dq_path) 
    elif  dq ==  "广东7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "71", dq_path)
    elif  dq ==  "广东8区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "81", dq_path)
    elif  dq ==  "广东9区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "89", dq_path)   
    elif  dq ==  "广东10区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "98", dq_path)    
    elif  dq ==  "广东11区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "105", dq_path)    
    elif  dq ==  "广东12区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "126", dq_path)   
    elif  dq ==  "广东13区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "134", dq_path)    
    elif  dq ==  "广州1/2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "34", dq_path)    
    elif  dq ==  "广西1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "28", dq_path)    
    elif  dq ==  "广西2/4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "64", dq_path)   
    elif  dq ==  "广西3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "88", dq_path)   
    elif  dq ==  "广西5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "133", dq_path)   
    elif  dq ==  "湖南1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "5", dq_path)    
    elif  dq ==  "湖南2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "25", dq_path)    
    elif  dq ==  "湖南3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "50", dq_path)   
    elif  dq ==  "湖南4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "66", dq_path)   
    elif  dq ==  "湖南5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "74", dq_path)   
    elif  dq ==  "湖南6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "85", dq_path)   
    elif  dq ==  "湖南7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "117", dq_path)    
    elif  dq ==  "湖北1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "9", dq_path)    
    elif  dq ==  "湖北2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "24", dq_path)   
    elif  dq ==  "湖北3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "48", dq_path)   
    elif  dq ==  "湖北4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "68", dq_path)    
    elif  dq ==  "湖北5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "76", dq_path)    
    elif  dq ==  "湖北6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "94", dq_path)    
    elif  dq ==  "湖北7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "115", dq_path)    
    elif  dq ==  "湖北8区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "127", dq_path)    
    elif  dq ==  "上海1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "3", dq_path)    
    elif  dq ==  "上海2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "16", dq_path)    
    elif  dq ==  "上海3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "36", dq_path)    
    elif  dq ==  "上海4/5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "93", dq_path)    
    elif  dq ==  "江苏1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "7", dq_path)    
    elif  dq ==  "江苏2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "20", dq_path)    
    elif  dq ==  "江苏3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "41", dq_path)    
    elif  dq ==  "江苏4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "53", dq_path)   
    elif  dq ==  "江苏5/7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "79", dq_path)   
    elif  dq ==  "江苏6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "90", dq_path)   
    elif  dq ==  "江苏8区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "109", dq_path)   
    elif  dq ==  "浙江1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "11", dq_path)   
    elif  dq ==  "浙江2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "21", dq_path)    
    elif  dq ==  "浙江3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "55", dq_path)   
    elif  dq ==  "浙江4/5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "84", dq_path)  
    elif  dq ==  "浙江6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "116", dq_path)   
    elif  dq ==  "浙江7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "129", dq_path)  
    elif  dq ==  "安徽1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "30", dq_path)   
    elif  dq ==  "安徽2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "58", dq_path)   
    elif  dq ==  "安徽3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "10", dq_path)   
    elif  dq ==  "福建1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "14", dq_path)  
    elif  dq ==  "福建2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "44", dq_path)  
    elif  dq ==  "福建3/4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "80", dq_path)  
    elif  dq ==  "江西1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "29", dq_path)   
    elif  dq ==  "江西2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "62", dq_path)    
    elif  dq ==  "江西3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "96", dq_path)   
    elif  dq ==  "西北1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "12", dq_path)
    elif  dq ==  "西北2/3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "46", dq_path)   
    elif  dq ==  "西南1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "17", dq_path)
    elif  dq ==  "西南2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "49", dq_path)    
    elif  dq ==  "西南3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "92", dq_path)   
    elif  dq ==  "陕西1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "33", dq_path)    
    elif  dq ==  "陕西2/3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "63", dq_path)   
    elif  dq ==  "云贵1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "124", dq_path)    
    elif  dq ==  "云南1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "120", dq_path)    
    elif  dq ==  "贵州1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "122", dq_path)    
    elif  dq ==  "四川1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "4", dq_path)   
    elif  dq ==  "四川2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "26", dq_path)   
    elif  dq ==  "四川3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "56", dq_path)    
    elif  dq ==  "四川4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "70", dq_path)   
    elif  dq ==  "四川5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "82", dq_path)    
    elif  dq ==  "四川6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "107", dq_path)   
    elif  dq ==  "重庆1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "39", dq_path)    
    elif  dq ==  "重庆2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "73", dq_path)   
    elif  dq ==  "新疆1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "123", dq_path)   
    elif  dq ==  "华北1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "10", dq_path)    
    elif  dq ==  "华北2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "19", dq_path)   
    elif  dq ==  "华北3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "54", dq_path)    
    elif  dq ==  "华北4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "87", dq_path)   
    elif  dq ==  "河北1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "38", dq_path)    
    elif  dq ==  "河北2/3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "67", dq_path)    
    elif  dq ==  "河北4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "118", dq_path)    
    elif  dq ==  "河北5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "132", dq_path)  
    elif  dq ==  "天津1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "121", dq_path)    
    elif  dq ==  "东北1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "13", dq_path)    
    elif  dq ==  "东北2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "18", dq_path)    
    elif  dq ==  "东北3/7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "23", dq_path)    
    elif  dq ==  "东北4/5/6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "83", dq_path)   
    elif  dq ==  "北京1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "2", dq_path)   
    elif  dq ==  "北京2/4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "35", dq_path)
    elif  dq ==  "北京3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "72", dq_path) 
    elif  dq ==  "内蒙古1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "25", dq_path)
    elif  dq ==  "辽宁1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "31", dq_path)
    elif  dq ==  "辽宁2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "47", dq_path) 
    elif  dq ==  "辽宁3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "61", dq_path) 
    elif  dq ==  "吉林1/2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "42", dq_path)
    elif  dq ==  "黑龙江1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "40", dq_path)
    elif  dq ==  "黑龙江2/3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "51", dq_path)  
    elif  dq ==  "河南1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "27", dq_path)    
    elif  dq ==  "河南2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "43", dq_path)    
    elif  dq ==  "河南3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "57", dq_path)    
    elif  dq ==  "河南4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "69", dq_path)
    elif  dq ==  "河南5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "77", dq_path)
    elif  dq ==  "河南6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "103", dq_path) 
    elif  dq ==  "河南7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "135", dq_path)   
    elif  dq ==  "山东1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "6", dq_path)   
    elif  dq ==  "山东2/7区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "37", dq_path)    
    elif  dq ==  "山东3区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "59", dq_path)    
    elif  dq ==  "山东4区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "75", dq_path)    
    elif  dq ==  "山东5区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "78", dq_path)   
    elif  dq ==  "山东6区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "106", dq_path)   
    elif  dq ==  "山西1区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "32", dq_path)
    elif  dq ==  "山西2区":
        dnf.WriteIni("NoLoginUserRecord", "LastLogin", "95", dq_path)
    dnf.RunApp(dnf_path, 0)
    dnf.EnableRealMouse(1,20,30)
    dl(dnf, pic_path, qq_number, password)
