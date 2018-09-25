import os
expt = [".DS_Store", "Thumbs.db"]
dirCount = 0
def ren(path):
    global dirCount
    dirCount += 1
    lis = os.listdir(path)
    num = 0
    dirName = list(path.split('/'))[-1]
    lis = sorted(lis)
    print(dirName+" -> "+str(dirCount))
    for name in lis:
        if(name in expt):
            continue
        if('.' in name):
            fileType = name.split('.')[-1]
            num += 1
            os.rename(path+'/'+name,path+'/'+str(num)+'.'+fileType)
            print(path+str(num)+'.'+fileType)
        else:
            ren(path+'/'+name)
ren("img/")
