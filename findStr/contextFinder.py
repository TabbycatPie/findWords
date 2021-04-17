import findWords2
import codecs
import chardet
import os
import re

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
    try:
        temp = time.replace("time:","").replace(" ","").replace(",",".").split("-->")
    except:
        print("time syntax error\n!")
        temp=["00:00:00.00","00:00:00.00"]
    return temp[0],temp[1]

#把时间字符按需求转换
# @time :格式化的时间字符串 ep:00:56:52.12
# @min_60:需要减去的时间(60分钟以内，可正可负，输入70会变成+10，输入时间超过极限会直接归零)
def getTimeStringWithAddition(time,min_60):
    #注意时间min_60只能在0~60内，跨度太大会被忽略
    _list = time.split(":")
    overflow = 0 #进位标识
    if(len(_list)==3):
        h = int(_list[0]) #小时
        m = int(_list[1]) #分钟
    else:
        print("time syntax error!\n")
    if(min_60>0):
        min_60 = min_60 % 60
    else:
        min_60 = -((-min_60)%60)
    if(m+min_60>59):
        overflow = 1
        m = (m+min_60)%60
    elif(m+min_60<0):
        overflow = -1
        if(h-1<0):
            h = 1
            m = 0
        else:
            m = (m+min_60)%60
    else:
        m = m + min_60      
    h = h + overflow   
    h_out="00"
    m_out="00" 
    if(h<10):
        h_out = "0"+str(h)
    else:
        h_out = str(h)
    if(m<10):
        m_out = "0"+str(m)
    else:
        m_out = str(m)


    return h_out+":"+m_out+":"+_list[2]

#获取ass字幕的时间字符串
def assGettime(sub_str):
   parts = sub_str.split(",")
   if(len(parts)<10):
      print("This line do not has content!\n")
      return "00:00:00.00","00:00:00.00"
   else:
      t1 = parts[1]
      t2 = parts[2]
      if(findWords2.isTime(t1) and findWords2.isTime(t1)):
         #两个时间格式正常
         return "0"+t1.replace(",","."),"0"+t2.replace(",",".")
      else:
         return "00:00:00.00","00:00:00.00"
#合并字符串list(被split之后的)
def mergeStringList(Stringmlist,spiliter):
    result = ""
    for _str in Stringmlist:
        result = result +spiliter+ _str
    return result

#此函数处理list[index]之后的所有行 到"/r/n"空行为止
def srtGetContent(index,lines):
    temp = list()
    while(lines[index]!="\r\n" and index < len(lines)):
        temp.append(lines[index])
        index = index + 1
    return mergeStringList(temp,"").replace("\r\n","\n")

def assGetContent(sub):
   parts = sub.split(",")
   if(len(parts)<10):
      print("Syntax Error!\n")
      return ""
   else: 
      return re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", mergeStringList(parts[9:],"")).replace("\\N","\n")



    

def main():
    exit_flag = False
    while(not exit_flag):
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
        if(findWords2.isTime(time)):
            time1,time2 = getTime(time)
        else:
            time1 = "00:00:00.00"
            time2 = "00:00:00.00"
    
        try:
            #获取文件
            FileObj = open(file_name,'rb')
            data = FileObj.read(100)
            result = chardet.detect(data)
            FileObj = codecs.open(file_name,'r',result['encoding'])
            lines = FileObj.readlines()
        except Exception as e:
            print(e)
            print("Can not open file!\n")
            os.system("pause")
            continue
        
        content = list()
        #分情况处理srt和ass
        if(findWords2.getFiletype(file_name)=="srt"):  
            #找到1分钟之前的行
            cur = num - 1
            while (cur>0):
                if(findWords2.isTime(lines[cur])):
                    t1,t2 = getTime(lines[cur])
                    if(t1<getTimeStringWithAddition(time1,-1)):
                        break
                    else:
                        content.append(srtGetContent(cur+1,lines)) #将搜索到的字幕 入栈
                cur = cur - 1
            content.reverse() #反转
            #找到1分钟之后的行
            cur = num 
            while (cur<len(lines)):
                if(findWords2.isTime(lines[cur])):
                    t1,t2 = getTime(lines[cur])
                    if(t1>getTimeStringWithAddition(time1,1)):
                        break
                    else:
                        content.append(srtGetContent(cur+1,lines)) #入队列
                cur = cur + 1
        else:
            #ass文件
            #获取前1分钟的字幕
            cur = num - 1
            while(cur>0):
                sub = lines[cur]
                t1,t2 = assGettime(sub)
                if(t1 < getTimeStringWithAddition(time1,-1)):
                    #时间超界
                    break
                else:
                    content.append(assGetContent(sub))
                cur = cur - 1

            content.reverse()

            #获取后1分钟的字幕
            cur = num
            while(cur<len(lines)):
                sub = lines[cur]
                t1,t2 = assGettime(sub)
                if(t2 > getTimeStringWithAddition(time1,1)):
                    #时间超界
                    break
                else:
                    content.append(assGetContent(sub))
                cur = cur + 1

        #显示上下文
        for con in content:
            print(con)
        char = input("Exit?('y' to exit):")
        if(char.upper == "Y"):
            break
    
   
if __name__ == '__main__':
    main()
