#!/usr/bin/python
#coding=utf-8
import difflib
import sys
try:
    file1=sys.argv[1]           #第一个参数文件
    file2=sys.argv[2]           #第二个参数文件
except Exception,e:
    print "Error: %s"%str(e)
    sys.exit()
def readfile(filename):             #相对来说，可以考虑调用函数，因为需要处理两个文件
    try:                        #检测异常
        df=open(filename,"rb")              #打开文件
        text=df.read().splitlines()         #读取文件内容，并根据行进行分割
        df.close()                          #关闭文件
        return text                         #返回文件内容字符串
    except IOError,e:                           #抛出异常
        print "ERROR: %s"%str(e)
        sys.exit()
if file1=="" or file2=="":
    print "please input filename and filename"
    sys.exit()
file1_lines=readfile(file1)
file2_lines=readfile(file2)
diff=difflib.HtmlDiff()                #创建HtmlDiff类对象
print diff.make_file(file1_lines,file2_lines)
