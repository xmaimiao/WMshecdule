import requests
import json
import re

class Dohttp:
    def __init__(self):
        self.sessions = requests.sessions.Session()

    def dohttp(self,url=None,data=None,method=None,headers=None,json=None):
        method = method.lower()
        headers = eval(headers)
        if method == 'get':
            resp = self.sessions.request(url=url,method=method,params=data,headers=headers)
        elif method =='post':
            #要注意传入的data或json为空的情况，eval()就会出错
            if json :
                resp = self.sessions.request(json=eval(json),url=url,method=method,headers=headers)
            elif data:
                resp = self.sessions.request(data=eval(data),url=url,method=method,headers=headers)
            else:
                resp = self.sessions.request(data=None,json=None, url=url, method=method, headers=headers)
        else:
            resp=None
            print("出錯了！")
        return resp

    def close(self):
        self.sessions.close()