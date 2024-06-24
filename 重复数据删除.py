import platform,os,shutil

file = ("./")
path_list = os.listdir(file)
file_list = []

for i in path_list:
    if (os.path.isfile(i)):
        file_list.append(i)
#遍历当前路径下的所有文件，储存到 "file_list"

repeat_list = []
screen_list = []

def Read (repeat_list): #读取文件内容用以检测文件是否重复
    global screen_list
    
    for i in repeat_list:
        #fl为文件内容（二进制数据）
        print(i)
        file_open = open(file+i,"rb")
        fl = file_open.read()
        file_open.close()
        
        
        for j in repeat_list:
            if (i!=j and os.path.getsize(i)==os.path.getsize(j)): #只读相同字节的文件
                file_open2 = open(file+j,"rb")
                fl2 = file_open2.read()
                file_open2.close()
                
                if (fl==fl2):
                    if(j not in screen_list ):
                        screen_list.append(j)
                    
            
for i in file_list: #查看文件大小，大小相同的文件记录到repeat_list
    repeat = os.path.getsize(file+i)
    for j in file_list:
        repeat2 = os.path.getsize(file+j)
        if (i!=j and repeat2==repeat):
            if (j not in repeat_list):#添加的元素不会与列表里的元素重复
                repeat_list.append(j)
        
Read(repeat_list)

#print(repeat_list) 字节（大小）相同的文件列表
#print(screen_list) 内容相同的文件列表
print("----------以下为相同内容的文件----------")
for i in screen_list:
    print(i)
print("------------------------------")

independent_list = []
other_list = []

s = input("请输入 y/n 来决定是否将内容相同的文件移动出来")
if s=="y" or s=="Y" or s=="yy" or s=="yyy" or s=="YY" or s=="YYY":
    print("----------正在执行操作----------")
    print("重复的文件会被移动到“重复文件”这个文件夹里")
    if( not os.path.exists("./重复文件")):
        print("创建文件夹。。。")
        os.mkdir("./重复文件")
    else :
        print("文件夹已存在")

    print("开始移动。。。")

     
    #将数分为两组
    for i in repeat_list:
        if (i not in independent_list and i not in other_list):
            #双列表里都没找到该元素，说明为新元素执行以下操作
            #添加该元素到一个列表中，并遍历后面的元素，将同样的元素放到另一个列表
            independent_list.append(i)
            for j in repeat_list: #元素名不同，但内容相同的元素放到other列表里
                if (j!=i and os.path.getsize(file+i)==os.path.getsize(file+j)):
                    file_open = open(file+i,"rb")
                    fl = file_open.read()
                    file_open.close()

                    file_open2 = open(file+j,"rb")
                    fl2 = file_open2.read()
                    file_open2.close()
                    if(fl==fl2):
                        other_list.append(j)

    for i in other_list:
        shutil.move(file+i,"./重复文件")
    
    print("这些文件保持不变")
    print(independent_list)
    print("这些文件放到文件夹里")
    print(other_list)
else: 
    print("操作已取消")