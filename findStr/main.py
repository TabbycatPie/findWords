import findWords
import os

def getWordList():
    _input=input("Input words(split with ',' eg:hello,good):")
    words = _input.split(",")
    return words

def printScreen(info,total,current,pocess):
    os.system("cls")
    print(info)
    print("\nCurrent pocession:"+(current/total)*100+"%")

def main():

    #输入查找的单词
    words=getWordList()

    #获取字幕文件路径
    libpath=os.getcwd()+"\subtitlelib\\"
    #print(libpath)
    #获取文件名列表
    files = os.listdir(libpath)
    for word in words :
        for file in files :
            findWords.findKeyStringInFile(word,libpath+file)
    

    os.system("pause")

    #for word in words:
   #    findWords.findKeyStringInFile(word,r".\subtitlelib\\The.Bridge.2021.1080p.WEBRip.x264-RARBG.srt")


if __name__ == '__main__':
    main()


