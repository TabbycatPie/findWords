

import codecs
import Output
#FileName = r'c:\ls\1'
#KeyStr = input("the key string: ")
#KeyStr = '<dd class="info"><span>执业证号：'

def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]

def findKeyStringInFile(KeyStr,FileName):
    found_count=0 #找到
    #FoundFlag = False
    #用utf-8格式打开文件
    FileObj = codecs.open(FileName, 'r','utf-8')
    try:
        LineTemp = FileObj.readline()
    except Exception:
       # print("file format error!\nfileName:"+FileName)
        Output.logError("At "+ FileName+ ":file format error!" )
        LineTemp=""
    PreLine1 = ""
    PreLine2 = ""
    PreLine3 = ""
    PreLine4 = ""
    #print("finding "+ KeyStr +" in "+FileName)
    while LineTemp:
        if(LineTemp.upper().find(KeyStr.upper()) > 0):
            #找到之后分析处理

            #输出到文件
            Output.outPut(PreLine,LineTemp,FileName,KeyStr)
            found_count = found_count + 1
        #滑动窗口遍历
        #顺序如下
        #preline1 > preline2 > preline3 > preline4 > linetemp 
        PreLine1 = PreLine2
        PreLine2 = PreLine3
        PreLine3 = PreLine4
        PreLine4 = LineTemp
        try:
            LineTemp = FileObj.readline()
        except Exception:
            LineTemp = ""
    FileObj.close()
    return found_count
