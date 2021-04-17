#用于测试 contextfinder中内部函数是否正常
import contextFinder
import findWords2
import re

def main():
   sub="Dialogue:0,0:22:29.33,0:22:32.98,Default,NTP,0000,0000,0000,,我说了真相与观察角度有关\\N{\\fn微软雅黑\\fs14\\c&H4bc2ef&}I told you truth is a matter of perspective."
   print(assGetContent(sub))

def assGetContent(sub):
   parts = sub.split(",")
   if(len(parts)<10):
      print("Syntax Error!\n")
      return ""
   else: 
      return re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", contextFinder.mergeStringList(parts[9:],"")).replace("\\N","\n")

   
if __name__ == '__main__':
    main()
