import os
import chardet
import codecs

#正式库
lib_path=r'./subtitlelib/'
#测试库
#lib_path=r'./testlib/'

#直接得到文件名
def getFileName(movie_name):
    temp = movie_name.replace("movie:","")
    return lib_path+temp

#得到行号，如果异常返回-1
def getLineNumber(line_num):
    temp = line_num.replace("line number:","")
    try:
        num = int(temp)
    except:
        return -1
    return num

#获取时间字符串
def getTime(time):
    temp = time.replace("time:","").replace(" ","").replace(",",".").split("-->")
    return temp[0],temp[1]

def Getbefore(time,min):
    _list = time.split(":")
    if(len(_list)==3):
        m = int(_list[1]) #分钟
    else:
        print("time syntax error!\n")
    return _list[0]+str(m-min)+_list[2]

#合并字符串list(被split之后的)
def mergeStringList(Stringmlist):
    result = ""
    for _str in Stringmlist:
        result = result + _str
    return result

    

def main():
    movie = input("Paste your output here:\n")
    while(movie==""):
        movie = input()
    line_num = input()
    time = input()
    #抵消剩下行
    temp = input()
    while temp!="":
        temp = input()
    
    file_name = getFileName(movie)
    num = getLineNumber(line_num)
    time1,time2 = getTime(time)

    #获取文件
    FileObj = open(file_name,'rb')
    data = FileObj.read(100)
    result = chardet.detect(data)
    FileObj = codecs.open(file_name,'r',result['encoding'])
    try:
        lines = FileObj.readlines()
    except:
        print("Can not open file!\n")

    print(lines[line_num])
    os.system("pause")
   
if __name__ == '__main__':
    main()
