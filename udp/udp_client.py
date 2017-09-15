#! /usr/bin/env python3  
#-*- coding=utf-8 -*-  
  
# ============================  
# Describe :    给平台提供的日志   
# Modify Date:     2017/08/10  
# ============================ 
"""
@author: shikinami
@software: PyCharm Community Edition
@file: udp_client.py
@time: 17-9-14 下午4:39
"""
import socket
class Main(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def func_client(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.sendto(b'hello, this is a class test info !',(self.host,self.port)) #UDP专用,发送数据到指定的IP地址和端口
if __name__ == '__main__':
    '''
    This is test template
    '''
    host = 'localhost'
    port = 8081
    u_c = Main(host,port)
    u_c.func_client()