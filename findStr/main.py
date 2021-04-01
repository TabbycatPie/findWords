import findWords
import os

def getWordList():
    _input=input("Input words(split with ',' eg:hello,good):")
    words = _input.split(",")
    return words

def printScreen(info,total,current):
    os.system("cls")
    #固定不变的东西
    print(info)
    print("\nCurrent pocession:"+str((current/total)*100)+"%")

def main():

    #输入查找的单词
    words=getWordList()
    #获取字幕文件路径
    libpath=os.getcwd()+"\subtitlelib\\"
    #print(libpath)
    #获取文件名列表
    files = os.listdir(libpath)
    total=len(files)
    current=0
    for word in words :
        word_count=0
        for file in files :
            current = current + 1
            word_count= word_count + findWords.findKeyStringInFile(word,libpath+file)
            printScreen("Current Word:"+ word+"\nCurrent File:"+file+"\nFOUND:"+str(word_count),total,current)
    

    os.system("pause")

    #for word in words:
   #    findWords.findKeyStringInFile(word,r".\subtitlelib\\The.Bridge.2021.1080p.WEBRip.x264-RARBG.srt")


if __name__ == '__main__':
    main()


