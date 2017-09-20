#! /usr/bin/env python3  
#-*- coding=utf-8 -*-  
  
# ============================  
# Describe :    给平台提供的日志   
# Modify Date:     2017/08/10  
# ============================ 
"""
@author: shikinami
@software: PyCharm Community Edition
@file: t_c.py
@time: 17-9-18 下午4:55
"""
import socket
class Main(object):
    host = '127.0.0.1'
    port = 8080
    def __init__(self):
        self.t_c = socket.socket()
        self.ip_port = (self.host,self.port)
        self.t_c.connect(self.ip_port)
    def create_line(self):
        self.data = self.t_c.recv(1024)
        print(self.data)

if __name__ == '__main__':
    '''
    This is test template
    '''
    obj = Main()
    obj.create_line()