

import codecs
import Output
#FileName = r'c:\ls\1'
#KeyStr = input("the key string: ")
#KeyStr = '<dd class="info"><span>执业证号：'

def mergeStringList(Stringmlist):
    result = ""
    for _str in Stringmlist:
        result = result +","+ _str
    return result

def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]

def isTime(time_str):
    #发现时间特征
    return contains("0123456789",time_str) and contains(":",time_str)

#逐个对比字符，查看str_origin中是否含有str_key中的
def contains(str_key,str_origin):
    contained = False
    for key in str_key:
        for char in str_origin:
            if key == char:
                contained = True
                break
        if contained:
            break
    return contained


def findKeyStringInFile(KeyStr,FileName):
    found_count=0 #找到
    line_num = 1  #行号
    error_count =0#错误次数
    #FoundFlag = False
    #用utf-8格式打开文件

    FileObj = codecs.open(FileName, 'r','utf-8')
    try:
        LineTemp = FileObj.readline()
    except Exception:
        # print("file format error!\nfileName:"+FileName)
        #第一次读取出错较多,屏蔽日志输出
        #Output.logError("ENCODE ERROR!",line_num,FileName)
        LineTemp=""
    PreLine = ["","","",""]
    #print("finding "+ KeyStr +" in "+FileName)
    while LineTemp:
        if(LineTemp.upper().find(KeyStr.upper()) >= 0):
            time = "??\n"
            content = LineTemp
            #找到之后分析处理
            if(getFiletype(FileName)=='srt'):
                for line in PreLine:
                    if isTime(line):
                        time = line[0:-1] #去掉/n 
            else:
                #处理ass字幕文件
                temp_list=LineTemp.split(",")
                if temp_list[0] == "Dialogue: 0" and len(temp_list)>9:
                    time=temp_list[1]+"-->"+temp_list[2]+"\n"
                    content = mergeStringList(temp_list[9:]).replace("\n"," ") + "\n"
                else:
                    content = "SUBTITLE ERROR: "+content

            #输出到文件
            Output.outPut(time,content,line_num,FileName,KeyStr)
            found_count = found_count + 1
        #滑动窗口遍历
        #顺序如下
        #preline1 > preline2 > preline3 > preline4 > linetemp 
        PreLine=[PreLine[1],PreLine[2],PreLine[3],LineTemp]
        line_num = line_num + 1
        try:
            LineTemp = FileObj.readline()
        except Exception:
            Output.logError("ENCODE ERROR!",line_num,FileName)
            error_count = error_count + 1
            if(error_count > 50):
                Output.logError("TOO MANY ERRORS,BREAK!",line_num,FileName)
                break
            LineTemp = ""
    FileObj.close()
    return found_count
