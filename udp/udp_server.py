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
@time: 17-9-14 下午4:35
"""
import socket
class Main(object):
    def __init__(self,port):
        self.port = port
    def func_server(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # 从指定的端口,从任何发送者,接收UDP数据
        s.bind(('',self.port))
        print('正在等待接入...')
        while True:
            #接收一个数据
            data,addr = s.recvfrom(1024)         #UDP专用,接收数据,返回数据远端的IP地址和端口
            print("Received:",data,'from',addr)
        

if __name__ == '__main__':
    '''
    This is test template
    '''
    port = 8081
    u_s = Main(port)
    u_s.func_server()
