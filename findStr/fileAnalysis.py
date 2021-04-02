import os

lib_path=r'./subtitlelib/'


def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]

def mergeStringList(Stringmlist):
    result = ""
    for _str in Stringmlist:
        result = result + _str
    return result

def getFileNameWithOutSuffix(filename):
    return mergeStringList(filename.split(".")[:-1])


#注意，参数filename需要含有后缀命
def fileCheck(filename):
    file_count = 0
    info = "File amount changed! start scanning?\n"
    files = os.listdir(lib_path)
    #数量检查
    file_num = int(Output.loadConfig("file_num"))
    if file_num!= len(files):
        Output.modifyConfig("file_num",str(len(files)))
        Output.printScreen(info)
        os.system("pause")
        #文件扫描
        info = "Scaning....."
        for file in files:
            file_count = file_count + 1
            Output.printScreen(info,)
            if (file!=filename):
                if(getFileNameWithOutSuffix(filename).find(getFileNameWithOutSuffix(file)>0):
                    print("Duplicate file found!")
                    print(file+" and "filename+" maybe the same,do you want to delet one of them?")

    