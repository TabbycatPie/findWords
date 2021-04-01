

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
    FoundFlag = False
    #用utf-8格式打开文件
    FileObj = codecs.open(FileName, 'r','utf-8')
    try:
        LineTemp = FileObj.readline()
        NextLine = FileObj.readline()
    except Exception as e:
       # print("file format error!\nfileName:"+FileName)
        Output.logError("At "+ FileName+ ":file format error!" )
        LineTemp=""
        NextLine=""
    PreLine = ""
    
    #print("finding "+ KeyStr +" in "+FileName)
    while NextLine:
        if(LineTemp.upper().find(KeyStr.upper()) > 0):
            FoundFlag = True
            Output.outPut(PreLine,LineTemp,FileName,KeyStr)
            found_count = found_count + 1
        PreLine=LineTemp
        LineTemp = NextLine
        try:
            NextLine = FileObj.readline()
        except Exception as e:
            NextLine =""
    FileObj.close()
    #没有找到
    if FoundFlag == False:
        Output.logError("At "+ FileName +": Word -  "+KeyStr+ "  Can not found !" )
    return found_count
