#!/usr/bin/env python3.7

import requests, sys  #网络请求

#Cookies = "LIVE_BUVID=AUTO3715382739921424; buvid3=71AC02C7-EF25-46A5-9A2F-DB1CB10744F71607infoc; rpdid=oopmqlpqkmdoskqimpwww; stardustvideo=1; CURRENT_FNVAL=16; dssid=8aabde0ff0f7f1621; dsess=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiFWRlMGZmMGY3ZjE2MjE3MWMGOwBG%0ASSIJY3NyZgY7AEZJIiUxYTM3YTg4MTY2NzZhNWZkNjYyODAyOWQwODk1NTlh%0AMgY7AEZJIg10cmFja2luZwY7AEZ7B0kiFEhUVFBfVVNFUl9BR0VOVAY7AFRJ%0AIi1lZjFkZjRjZTdiMWE2Y2JkZmQyZjRkMzA2OGYyMGI0NzhjYjU1OGEzBjsA%0ARkkiGUhUVFBfQUNDRVBUX0xBTkdVQUdFBjsAVEkiLWRkMDY1ZWQyNjNjNjdk%0ANzk5Zjk0M2FiNmMzOWI1NWM1ZTAwOGNiYjUGOwBGSSIKY3RpbWUGOwBGbCsH%0Aj3a9W0kiCGNpcAY7AEYiEjY4LjEwNy4xMjQuNTM%3D%0A--b5b62086b230a085ae65aee9304d7f14ca8a07ad; fts=1539143396; CURRENT_QUALITY=64; _uuid=547F11BE-9B64-40CC-37DE-6B95B010429C05405infoc; INTVER=1; sid=9onpe38s; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=d1486084%2C1576633926%2Ca277c9b1; bili_jct=b29db4670b4f9967fb2921a0fc878950; UM_distinctid=16e7c3622401e-01fbe0ab154c45-76256753-1fa400-16e7c362241181; laboratory=1-1"

MSG = sys.argv[1]

Cookies =  "LIVE_BUVID=AUTO9515807899133696; _uuid=B8B67CEF-6E2D-E430-06A0-FD7C4094942515464infoc; buvid3=1A07C860-1A13-4D29-A1A5-DC2FB2513D8353933infoc; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1580789916,1581786522; CURRENT_FNVAL=16; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=a2d7123b%2C1583382291%2C282aec21; bili_jct=550b04e5aaa502036c0de72f1657b7a9; _dfcaptcha=4789a18938c95d49b63ad418a5354b35; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1581786522"
#Cookies = "LIVE_BUVID=AUTO3715382739921424; buvid3=71AC02C7-EF25-46A5-9A2F-DB1CB10744F71607infoc; rpdid=oopmqlpqkmdoskqimpwww; stardustvideo=1; CURRENT_FNVAL=16; fts=1539143396; CURRENT_QUALITY=64; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1574043734; _uuid=547F11BE-9B64-40CC-37DE-6B95B010429C05405infoc; INTVER=1; sid=9onpe38s; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=d1486084%2C1576633926%2Ca277c9b1; bili_jct=b29db4670b4f9967fb2921a0fc878950; UM_distinctid=16e7c3622401e-01fbe0ab154c45-76256753-1fa400-16e7c362241181; laboratory=1-1; _dfcaptcha=62d61ad85c189bf042630c7aa72eb8d5; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1574043734"
cookie = {'Cookie': Cookies}


data = {
'color':'16777215',
'fontsize':'25',
'mode':'1',
'msg':MSG,
'rnd':'1581786516',
'roomid':'21154895',
'bubble':'0',
'aid':'56737027',
'csrf_token':'550b04e5aaa502036c0de72f1657b7a9',
'csrf':'550b04e5aaa502036c0de72f1657b7a9'
}


res = requests.post('https://api.live.bilibili.com/msg/send', cookies=cookie, data=data)
#senddanmu.sendDM(data) #<Response [200]> 200是状态码 表示pass










'''
data = {
'type':'1',
'oid':'99115737',
'msg':'hello',
'aid':'56737027',
'progress':'134',
'color':'16777215',
'fontsize':'25',
'pool':'0',
'mode':'1',
'rnd':'1574042956475779',
'plat':'1',
'csrf':'b29db4670b4f9967fb2921a0fc878950'
}
'''
