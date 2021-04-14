import os
import re
import time
import codecs

output_path=r'./Output/'
logfile_path=r'./Log/'
config_file=r'./config.ini'

def printScreen(info,total,current):
    os.system("cls")
    #固定不变的东西
    print(info)
    print("\nCurrent progress :"+str(round((current/total)*100,2))+"%")

def loadConfig(config_name):
    line_num = 1
    try:
        FileObj = codecs.open(config_file, 'r+')
        config = FileObj.readline()
        while config:
            para=config.split(":")
            if para[0] == config_name:
                return para[1]
            config = FileObj.readline()
            line_num = line_num + 1
        return "NULL"
    except Exception:
        print("READ CONFIG FAILED!")
        logError("READ CONFIG FAILED!",line_num,config_file)
        return "ERROR"

def modifyConfig(config_name,config_val):
    f= codecs.open(config_file, 'w')
    f.write(config_name+":"+config_val)

def convertFilenameToMoviename(filename):
    t_list = filename.split("/")
    #返回文件名（不带后缀）
    return t_list[len(t_list)-1]

def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]


# def outPut(time,text,filename,word):
#     filetype = getFiletype(filename)
#     logFound(word,filename,"\ntime:"+time + "content:"+ text + "\n")
    
def outPut(time,text,line_num,filename,word):
    logFound(word,convertFilenameToMoviename(filename),"\nline number:"+str(line_num)+"\ntime:"+time + "content:"+ text + "\n")

def logFound(word,movie,content):
    FileObj = codecs.open(output_path + word +"_Found.txt", 'a','utf-8')
    try:
        FileObj.write("movie:"+movie + content)
    except Exception:
        FileObj.write("movie:"+movie + word)

# def logError(error_str):
#     #获取时间
#     localtime = time.asctime( time.localtime(time.time()))
#     #追加模式打开文件
#     FileObj = codecs.open(logfile_path+"Error_log.txt", 'a')
#     #print(logfile_path+"Error_log.txt")
#     #追加日志
#     try:
#         FileObj.write("Time:"+localtime+"\nError:"+error_str+"\n")
#     except Exception:
#         FileObj.write("Time:"+localtime+"\nError: error_str is not gbk!\n")
def log(log_str,at):
    #获取时间
    localtime = time.asctime( time.localtime(time.time()))
    #追加模式打开文件
    FileObj = codecs.open(logfile_path+"sys_log.txt", 'a')
    #追加日志
    try:
        FileObj.write("\nTime:"+localtime+"\nAT:"+at+"\nError:"+log_str+"\n")
    except Exception:
        print("LOG FAILED!")

def logError(error_str,line_num,at):
    #获取时间
    localtime = time.asctime( time.localtime(time.time()))
    #追加模式打开文件
    FileObj = codecs.open(logfile_path+"Error_log.txt", 'a')
    #print(logfile_path+"Error_log.txt")
    #追加日志
    try:
        FileObj.write("\nTime:"+localtime+"\nLineNumber:"+str(line_num)+"\nAT:"+at+"\nError:"+error_str+"\n")
    except Exception:
        FileObj.write("\nTime:"+localtime+"\nLineNumber:"+str(line_num)+"\nAT:"+at+"\nError: error_str is not gbk!\n")