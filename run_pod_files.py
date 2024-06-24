import platform,os,shutil

file = (os.listdir("./"))
Current_path = os.path.abspath("./") #返回绝对路径

def select_document(File_list):
    #遍历列表，挑选出列表中的文件
    file_list = []

    for i in File_list:
        if (os.path.isfile(i)):
            file_list.append(i)
    return file_list

def select_path(File_list):
    #遍历列表，挑选出列表中的路径
    file_list =[]
    for i in File_list:
        if(os.path.isdir(i)):
            file_list.append(i)
    return file_list

#后续思路：分成路径和文件两个列表
