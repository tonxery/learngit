
#! /usr/bin/env python3
#-*- coding=utf-8 -*-  
  
# ============================  
# Describe :    给平台提供的日志   
# Modify Date:     2017/08/10  
# ============================ 
"""
@author: shikinami
@software: PyCharm Community Edition
@file: tcp_server.py
@time: 17-9-15 下午2:06
"""
from socket import *
from time import ctime
from time import localtime
import time

class Main(object):
    def __init__(self,host,port,bufsiz):
        self.host = host
        self.port = port #监听端口
        self.bufsiz = bufsiz
        self.addr = (self.host,self.port)

    def func_server(self):
        sock = socket(AF_INET,SOCK_STREAM) #创建socket实例
        sock.bind(self.addr)               #绑定socket本地地址和端口,通常服务端调用
        sock.listen(5)                     #TCP专用开启监听模式
        STOP_CHAT = False                  #设置退出条件
        while not STOP_CHAT:
            print('waiting for connection,listen port %d'%(self.port)) #等等连接端口号为***
            tcpClientSock,addr=sock.accept() #TCP专用,服务器等待客户端连接,一般是阻塞状态.
            print('接受连接，客户地址，connect from：',addr)
            while True:
                try:
                    data = tcpClientSock.recv(self.bufsiz) #TCP专用接收数据
                except:
                    print(e)
                    tcpClientSock.close()
                    break
                if not data:
                    break
                #python3使用bytes,所以要进行编码
                #对日期进行格式化
                ISOTIMEFORMAT='%Y-%m-%d %X'
                stime=time.strftime(ISOTIMEFORMAT,localtime())
                s = 'Hi,you send me :[%s] %s'%(ctime(),data.decode('utf8'))
                tcpClientSock.send(s.encode('utf8'))  #TCP专用发送数据
                print([ctime()],':',data.decode('utf8'))
                #如果输入quit(忽略大小),则退出程序
                STOP_CHAT=(data.decode('utf8').upper()=="QUIT")
                if STOP_CHAT:
                    break
            tcpClientSock.close()
            sock.close()  #关闭socket实例




if __name__ == '__main__':
    '''
    This is test template
    '''
    obj = Main('',12345,1024)
    obj.func_server()