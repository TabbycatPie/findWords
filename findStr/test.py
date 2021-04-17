#用于测试 contextfinder中内部函数是否正常
import contextFinder

def main():
   str_time = contextFinder.getTimeStringWithAddition("00:46:39.12",50)
   print (str_time)
   
if __name__ == '__main__':
    main()
