import os
import Output

lib_path=r'./subtitlelib/'
#是否询问删除
asking = True


def getFiletype(filename):
    temp=filename.split(".")
    return temp[len(temp)-1]

def getInfo(file_name):
    #预处理
    pre = file_name
    str_key = ["简体",".chs", ".cn","&eng","&chs","&cht","简中","繁体","繁中" ,".cht","简英","英文",".en" ,"720p","1080p","H.264"]
    str_rep = ["#chi","#chi","#chi","#eng","#chi","#chi","#chi","#chi","#chi","#chi","#eng","#eng","#eng",   "",     "",     ""]
    count = 0
    for key in str_key:
        pre = pre.replace(key,str_rep[count])
        count = count + 1
    mlanguage = []  
    if pre.find("#chi")>=0:
        mlanguage.append("chi")
        pre = pre.replace("chi","")
    if pre.find("#eng")>=0:
        mlanguage.append("eng") 
        pre = pre.replace("eng","")
  
    return mlanguage,mergeStringList(pre.split(".")[:-1])


def mergeStringList(Stringmlist):
    result = ""
    for _str in Stringmlist:
        result = result + _str
    return result

def getFileNameWithOutSuffix(filename):
    return mergeStringList(filename.split(".")[:-1])


#删除字幕文件,外部请勿调用
def deleteFile(filename,files,reason):
    global asking
    todo = True
    if asking:
        print("Do you want to delete "+filename+"?")
        _input = input("\nPress Any Key To Continue...\nType \"NO\" not to delete\nType \"KILL\" to delete all file without asking\n")
        if _input == "KILL":
            asking = False
        if _input.upper() == "NO":
            todo = False
    if todo:
        try:
            os.remove(lib_path+filename)
            files.remove(filename)
            print(filename+"Deleted!\n")
            Output.log(reason,filename)
        except Exception:
            print("ERROR CAN NOT DELETE!\n")
            Output.logError("DELETE FILE FAILED!",0,"Deleting file "+filename)

#注意，参数filename需要含有后缀命
def fileCheck():
    files = os.listdir(lib_path)
    file_dup=0 #重复文件数量
    file_del=0 #删除文件数量
    #数量检查
    fnum = Output.loadConfig("file_num")
    if fnum in ["NULL","ERROR"]:
        fnum = 0
        print("fnum number error\n")
    file_num = int(fnum)
    need_scan = False
    if file_num!= len(files):
        print("File amount changed!\nRescan is needed")
        need_scan = True
    else:
        _input = input("File amount "+str(file_num)+" is correct!\ntype \"SCAN\" to force scan file\n")
        if _input == "SCAN":
            need_scan = True
    if need_scan:
        os.system("pause")
        #全文件扫描
        for mfile in files:
            #获取文件信息
            mf_language,mf_id_name = getInfo(mfile)
            #字幕没有英文文件判断
            if "eng" not in mf_language and len(mf_language)!=0:
                print("None English subtitle!\n")
                deleteFile(file,files,"Delete None English file")
                file_del = file_del + 1
            #相似文件扫描
            for file in files:
                f_language,f_id_name = getInfo(file)
                if (file!=mfile):#排除自身
                    if(mf_id_name.find(f_id_name)>=0):
                        #相似文件
                        print("Duplicate file found!")
                        print(file+"\n"+mfile+"\nmaybe the same\n")
                        deleteFile(file,files,"Delete duplicate file\nOriginal:"+mfile+"\nDeleted :"+file)
                        file_del = file_del + 1
                        file_dup = file_dup + 1
        print("\nScan finish!"+"\nRedundant Files:"+str(file_dup)+"\nDeleted Files:"+str(file_del))
        Output.modifyConfig("file_num",str(len(files)))
    else:
        print("Scan Abandoned!\n")
    os.system("pause")
