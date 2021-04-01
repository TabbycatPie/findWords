

import codecs
#FileName = r'c:\ls\1'
#KeyStr = input("the key string: ")
#KeyStr = '<dd class="info"><span>执业证号：'

def outPut(preline,curline,filename):
    filetype = getFiletype(filename)
    if(filetype == "srt"):
        print("movie:"+filename+"\ntime:"+preline + "content:"+ curline + "\n")
    else:
        print("movie:"+filename+"\ncontent:"+curline)

def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]

def findKeyStringInFile(KeyStr,FileName):
    FoundFlag = False
    #用utf-8格式打开文件
    FileObj = codecs.open(FileName, 'r','utf-8')
    try:
        LineTemp = FileObj.readline()
        NextLine = FileObj.readline()
    except Exception as e:
       # print("file format error!\nfileName:"+FileName)
        LineTemp=""
        NextLine=""
    PreLine = ""
    
    #print("finding "+ KeyStr +" in "+FileName)
    while NextLine:
        if(LineTemp.upper().find(KeyStr.upper()) > 0):
            FoundFlag = True
            outPut(PreLine,LineTemp,FileName)
        PreLine=LineTemp
        LineTemp = NextLine
        try:
            NextLine = FileObj.readline()
        except Exception as e:
            NextLine =""
    FileObj.close()
        
   # if FoundFlag == False:
        #print("Not found")