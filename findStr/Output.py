import os
import time
import codecs
import findWords

output_path=r'./Output/'
logfile_path=r'./Log/'

def outPut(time,text,filename,word):
    filetype = findWords.getFiletype(filename)
    logFound(word,filename,"\ntime:"+time + "content:"+ text + "\n")

def logFound(word,movie,content):
    FileObj = codecs.open(output_path + word +"_Found.txt", 'a')
    try:
        FileObj.write("movie:"+movie + content)
    except Exception:
        FileObj.write("movie:"+movie + word,'utf-8')

def logError(error_str):
    #获取时间
    localtime = time.asctime( time.localtime(time.time()))
    #追加模式打开文件
    FileObj = codecs.open(logfile_path+"Error_log.txt", 'a')
    #print(logfile_path+"Error_log.txt")
    #追加日志
    try:
        FileObj.write("Time:"+localtime+"\nError:"+error_str+"\n")
    except Exception:
        FileObj.write("Time:"+localtime+"\nError: error_str is not gbk!\n")