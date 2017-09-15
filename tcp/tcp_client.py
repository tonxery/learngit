
#! /usr/bin/env python3
#-*- coding=utf-8 -*-  
  
# ============================  
# Describe :    给平台提供的日志   
# Modify Date:     2017/08/10  
# ============================ 
"""
@author: shikinami
@software: PyCharm Community Edition
@file: udp_server.py
@time: 17-9-15 下午2:06
"""
from socket import *

class Main(object):
    def __init__(self,host,port,bufsiz):
        self.host = host
        self.port = port
        self.bufsiz = bufsiz
        self.ADDR=(self.host,self.port)
    def func_client(self):
        client = socket(AF_INET,SOCK_STREAM) #创建socket实例
        client.connect(self.ADDR)           #TCP专用,客户端主动连接服务器
        while True:
            data = input('>')
            if not data:
                break
            #python3传递的是bytes,所以要编码
            client.send((data.encode('utf8')))  #TCP专用发送数据
            print('发送信息到%s : %s'%(self.host,data))
            if data.upper()=='QUIT':
                break
            data = client.recv(self.bufsiz)     #TCP专用接收数据
            if not data:
                break
            print(data.decode('utf8'))
            print('从%s收到信息: %s'%(self.host,data.decode('utf8')))
if __name__ == '__main__':
    '''
    This is test template
    '''
    host = '127.0.0.1' #测试，连接本机
    port = 12345        #设置侦听端口
    bufsiz = 1024
    obj = Main(host,port,bufsiz)
    obj.func_client()
