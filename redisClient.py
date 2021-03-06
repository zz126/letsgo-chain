# -*- coding:utf8 -*-
import datetime

import redis
import json
import config
r = redis.Redis(host="localhost",password="11111", port=6379, db=0)

letgoDataKey = "letgo-data"

proxyIp = "proxy_ip"

#获取第三方验证码秘钥
def getCodeApi():
    apis = r.hgetall("apis")
    for appid, sign in apis.items():
        return  appid,sign

# 删除秘钥
def delApiKey(key):
    r.hdel("apis",key)


# 存储莱茨狗列表数据
def addLetsgoData(data):
    r.delete(letgoDataKey)
    for item in data:
        item['createtime']=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        r.lpush(letgoDataKey, json.dumps(item))


#获取列表数据
def getLetsgoData():
    length = r.llen(letgoDataKey)
    return r.lrange(letgoDataKey,0,length)



def getProxyData():
    return  r.hgetall("useful_proxy")

def deleteProxyData(key):
    r.hdel("useful_proxy",key)

#设置有效代理
def setPorxyIp(ip):
    r.lpush(proxyIp,ip)

def getProxyIp():
    ip = r.lpop(proxyIp)
    if(ip == None):
        return "127.0.0.1"
    else:
        return str(ip, "utf-8")

def setBuySuccess(msg):
    r.lpush("buy_success",msg)


def setImg(img):
    r.set(config.username+"_img",img)

def getImg():
   return r.get(config.username+"_img")


def setCode(code):
    r.set("code",code)

def getCode():
   return r.get("code")
def setSeed(seed):
    r.set("seed",seed)

def getSeed():
   return r.get("seed")


