import os
import time
import codecs
import findWords

output_path=r'./Output/'
logfile_path=r'./Log/'

def outPut(preline,curline,filename,word):
    filetype = findWords.getFiletype(filename)
    if(filetype == "srt"):
        #print("movie:"+filename+"\ntime:"+preline + "content:"+ curline + "\n")
        logFound(word,filename,"\ntime:"+preline + "\ncontent:"+ curline + "\n")
    else:
        #print("movie:"+filename+"\ncontent:"+curline)
        logFound(word,filename,"content:"+ curline + "\n")

def logFound(word,movie,content):
    FileObj = codecs.open(output_path + word +"_Found.txt", 'a')
    FileObj.write("movie:"+movie + content)

def logError(error_str):
    #获取时间
    localtime = time.asctime( time.localtime(time.time()))
    #追加模式打开文件
    FileObj = codecs.open(logfile_path+"Error_log.txt", 'a')
    #print(logfile_path+"Error_log.txt")
    #追加日志
    try:
        FileObj.write("Time:"+localtime+"\nError:"+error_str+"\n")
    except Exception as e:
        FileObj.write("Time:"+localtime+"\nError:error_str is not gbk!\n")