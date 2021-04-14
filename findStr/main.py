import findWords2
import os
import Output

#正式库
lib_path=r'./subtitlelib/'
#测试库
#lib_path=r'./testlib/'

def getWordList():
    _input=input("Input words(split with ',' eg:hello,good):")
    words = _input.split(",")
    return words


def main():

    #输入查找的单词
    words=getWordList()
    #获取字幕文件路径
    #libpath=os.getcwd()+"\subtitlelib\\"
    #print(libpath)
    #获取文件名列表
    files = os.listdir(lib_path)
    current=0
    total=len(files)*len(words)
    info=""
    for word in words :
        word_count=0
        info_t="Current Word:"+ word+"\nFOUND:"
        for file in files :
            current = current + 1
            word_count= word_count + findWords2.findKeyStringInFile(word,lib_path+file)
            if(current%100==0):
                Output.printScreen(info + info_t+str(word_count)+"\nCurrent file:"+file,total,current)
        #所有地方都没找到
        if(word_count==0):
            Output.logFound(word,"Can not found ","in anywhere")
        info=info + info_t+str(word_count)+"\nCurrent file:"+file + "\nCurrent progress :100%\nTotal progress :"+str(current)+"/"+str(total) +"\n-----------------------\n"
    os.system("pause")

    #for word in words:
   #    findWords.findKeyStringInFile(word,r".\subtitlelib\\The.Bridge.2021.1080p.WEBRip.x264-RARBG.srt")


if __name__ == '__main__':
    main()


