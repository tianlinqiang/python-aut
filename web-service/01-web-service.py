#coding=utf-8
import os,sys
import time
import pycurl


URL = raw_input("input your weburl:")
c = pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,1)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)

try:
    c.perform()
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

namelookup_time = c.getinfo(c.NAMELOOKUP_TIME)
connect_time = c.getinfo(c.CONNECT_TIME)
pretransfer_time = c.getinfo(c.PRETRANSFER_TIME)
starttransfer_time = c.getinfo(c.STARTTRANSFER_TIME)
total_time = c.getinfo(c.TOTAL_TIME)
http_code = c.getinfo(c.HTTP_CODE)
size_download = c.getinfo(c.SIZE_DOWNLOAD)
header_size = c.getinfo(c.HEADER_SIZE)
speed_download = c.getinfo(c.SPEED_DOWNLOAD)

print "HTTP 状态码: %s" %(http_code)
print "DNS解析时间: %.2f ms" %(namelookup_time*1000)
print "建立连接时间: %.2f ms" %(connect_time*1000)
print "准备传输时间: %.2f ms" %(pretransfer_time*1000)
print "传输开始时间: %.2f ms" %(starttransfer_time*1000)
print "传输结束总时间: %.2f ms" %(total_time*1000)
print "下载数据包大小: %d bytes/s" %(size_download)
print "HTTP头部大小: %d byte" %(header_size)
print "平均下载速度: %d bytes/s" %(speed_download)
indexfile.close()
c.close()

