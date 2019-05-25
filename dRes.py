from urllib.request import urlopen as html ,Request
from urllib.error import HTTPError,URLError
print('''\033[33;1m
 ___     ____ ____ ____ 
 |  \ __ |__/ |___ [__  
 |__/    |  \ |___ ___] 
\033[0m''')
print("\033[31;1m --::{ A http response status checker tool by 0xh7ml }::--")
print("\033[31;1mUsage : google.com\033[0m")
site = input("\033[36;1mEnter domain name / ip plz ~\033[0m")
try:
    tid = Request("http://www."+site)
    sie = html(tid)
    kis = sie.getcode()
except(ValueError,TypeError,HTTPError,URLError):
    pass
    print("\033[31;1mIt's 40* response or Plz check url again\033[0m")
else:
    print("\033[32;1mHttp Response status::")
    print(kis)