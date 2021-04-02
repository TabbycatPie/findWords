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
    print("\nCurrent pocession:"+str(round((current/total)*100,2))+"%")
    return info+"\nCurrent pocession:"+str(round((current/total)*100,2))+"%"

def loadConfig(config_name):
    line_num = 1
    try:
        FileObj = codecs.open(config_file, 'a')
        config = FileObj.readline()
        while config:
            para=config_file.split(":")
            if para[0] == config_name:
                return para[1]
            line_num = line_num + 1
        return "NULL"
    except Exception:
        print("READ CONFIG FAILED!")
        logError("READ CONFIG FAILED!",line_num,config_file)
        return "ERROR"

def modifyConfig(config_name,config_val):
    con_val = loadConfig(config_name)
    if (con_val != "ERROR"):
        f= codecs.open(config_file, 'r+')
        #修改参数
        open(config_file, 'w').write(re.sub(config_name+":"+con_val, config_val, f.read()))
    if (con_val == "NULL"):
        open(config_file,'a').write(config_name+":"+con_val)


def convertFilenameToMoviename(filename):
    t_list = filename.split("/")
    #返回文件名（不带后缀）
    return t_list[len(t_list)-1]

def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]


def outPut(time,text,filename,word):
    filetype = getFiletype(filename)
    logFound(word,filename,"\ntime:"+time + "content:"+ text + "\n")
    
def outPut(time,text,line_num,filename,word):
    filetype = getFiletype(filename)
    logFound(word,convertFilenameToMoviename(filename),"\nline number:"+str(line_num)+"\ntime:"+time + "content:"+ text + "\n")

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