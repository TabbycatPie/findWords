
import os
import fileAnalysis





def main():
    a = "asdhasd.ashgdjasd.dahsd.txt"
    temp_list=a.split(".")
    sss = fileAnalysis.mergeStringList(temp_list)
    print(sss)

if __name__ == '__main__':
    main()
