#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
 author : ieyzz@pku.edu.cn
 date: 2018.03.20
 version: 0.1
"""
import os
import cv2
import shutil
def getHeightAndWidth(path='',img=''):#返回图像的高度和宽度
    path+'/'+img+'\n'
    getImg=cv2.imread(path+'/'+img)
    sp=getImg.shape
    return sp[0],sp[1]

def getGuessName(firstName=''):
    nameList=[]
    nameList.append(firstName+'.jpg')
    nameList.append(firstName+'-.jpg')
    nameList.append(firstName+'.png')    
    nameList.append(firstName+'(1).jpg')  
    nameList.append(firstName+'(2).jpg')  
    nameList.append(firstName+'(3).jpg')  
    nameList.append(firstName+'(4).jpg')  
    nameList.append(firstName+'(5).jpg')  
    nameList.append(firstName+'(6).jpg')  
    nameList.append(firstName+'(7).jpg')  
    nameList.append(firstName+'(8).jpg')  
    nameList.append(firstName+'(9).jpg')  
    nameList.append(firstName+'-1.jpg')  
    nameList.append(firstName+'-2.jpg')  
    nameList.append(firstName+'-3.jpg')  
    nameList.append(firstName+'-4.jpg')  
    nameList.append(firstName+'-5.jpg')
    return nameList 

def getOriAndSketch(path='',img1='',img2=''):#返回的是彩色图和线稿图
    getImg1=cv2.imread(path+'/'+img1)
    getImg2=cv2.imread(path+'/'+img2)
    k=0
    if os.path.exists(path+'/'+img1):
        img1Height,img1Width=getHeightAndWidth(path,img1)
        k=k+1
    if os.path.exists(path+'/'+img2):
        img2Height,img2Width=getHeightAndWidth(path,img2)
        k=k+1
    if k!=2:
        return
    bAll=0
    gAll=0
    rAll=0
    b1All=0
    g1All=0
    r1All=0 
    print img1,img2
    [b,g,r]=getImg1[int(img1Height)-1,int(img1Width)-1]
    for i in range(int(img1Width)-1):
        [b,g,r]=getImg1[(img1Height)/2,i]
        bAll=b+bAll
        gAll=g+gAll
        rAll=r+rAll
    for i in range(int(img2Width)-1):
        [b1,g1,r1]=getImg2[(img2Height)/2,i]
        b1All=b1+b1All
        g1All=g1+g1All
        r1All=r1+r1All
    b=bAll/(img1Width-1)
    g=gAll/(img1Width-1)
    r=rAll/(img1Width-1)
    b1=b1All/(img2Width-1)
    g1=g1All/(img2Width-1)
    r1=r1All/(img2Width-1)
    if (b==b1 and g==g1 and r==r1):
        return img1,img2,0
    if ((b>230 and g>230 and r>230) and (b1<250 or r1<250 or g1<250)):
        return img2,img1,1
    elif((b1>230 and g1>230 and r1>230) and (b<250 or r<250 or g<250)):
        return img1,img2,1
    else:
        return img1,img2,0   
   
def saveImg(path='',ori='',sketch=''):#需要创建两个文件夹，分别是ori文件夹和sketch文件夹
    oriFileNum=len(os.listdir('ori'))+1
    sketchFileNum=len(os.listdir('sketch'))+1
    getImg1=cv2.imread(path+'/'+ori)
    getImg2=cv2.imread(path+'/'+sketch)
    t=0
    if os.path.exists(path+'/'+ori):
        img1Height,img1Width=getHeightAndWidth(path,ori)
        t=t+1
    if os.path.exists(path+'/'+sketch):
        img2Height,img2Width=getHeightAndWidth(path,sketch)
        t=t+1
    if t!=2:
        return
    [b,g,r]=getImg1[int(img1Height/2),int(img1Width/2)]
    [b1,g1,r1]=getImg2[int(img2Height/2),int(img2Width/2)]
    if b1!=b and g!=g1 and r!=r1:
        shutil.copyfile(path+'/'+ori,'ori/'+str(oriFileNum)+'.'+ori.split('.')[1])
        shutil.copyfile(path+'/'+sketch,'sketch/'+str(sketchFileNum)+'.'+sketch.split('.')[1])
    if os.path.exists(path+'/'+ori):
        os.remove(path+'/'+ori)
    if os.path.exists(path+'/'+sketch):
        os.remove(path+'/'+sketch)


def processImages(path='',nameList=[]):
    findFile={}#一个嵌套字典
    nameL=[]
    for name in nameList:
        ind=nameList.index(name)
        print path,nameList[ind]
        if os.path.exists(path+'/'+nameList[ind]):
            height,width=getHeightAndWidth(path,nameList[ind])
            nameL.append(name)
            findFile.update({str(height)+'_'+str(width):nameL})#在键值对里增加'height_width:fileName这样的,大小相同的存储在一起'
        else:
            return
    for size in findFile:
        if os.path.exists(path+'/'+findFile[size][0]) and os.path.exists(path+'/'+findFile[size][1]):
            oriImg,sketchImg,trueOrFlase=getOriAndSketch(path,findFile[size][0],findFile[size][1])#返回彩色图和线稿图,以后再判断列表数量
            if trueOrFlase==1:
                saveImg(path,oriImg,sketchImg)
        else:
            return 
        if len(findFile[size])>2:#只管前两张，剩下全删
            for d in findFile[size]:
                if os.path.exists(path+'/'+d):
                    os.remove(path+'/'+d)
        
        
def splitName(filePath=''):#相对路径
    Files=os.listdir(filePath)
    for allFile in Files:
        name=allFile.split('.')[0]
        name=name.split('(')[0]
        nameLS=getGuessName(name)#取得猜想的名字列表 
        guessList=[]
        alreadyTest=[]
        if name not in alreadyTest:
            for guess in nameLS:
                for result in nameLS:
                    if os.path.exists(filePath+'/'+result) and result.split('.')[0].split('(')[0].split('-')[0] not in alreadyTest:#如果文件存在则猜想成功
                        guessList.append(result)#得到可能的数据
                if len(guessList)==2:#处理猜想的结果
                    print filePath,guessList[0],guessList[1]
                    if os.path.exists(filePath+'/'+guessList[0] and filePath+'/'+guessList[1]):
                        oriImg,sketchImg,trueOrFlase=getOriAndSketch(filePath,guessList[0],guessList[1])
                        if trueOrFlase==1:
                            saveImg(filePath,oriImg,sketchImg)
                elif len(guessList)>2:
                    #print guessList
                    processImages(filePath,guessList)
        guessList=[]
        alreadyTest.append(result.split('.')[0].split('(')[0].split('-')[0])


if __name__=='__main__':
    print '请将图片目录放入存放图片的文件夹，并且做好备份，运行会删除原文件'
    filePath=os.getcwd()
    Files=os.listdir(filePath)
    if os.path.exists('ori')==0:
        os.makedirs('ori') 
    if os.path.exists('sketch')==0:
        os.makedirs('sketch') 
    for allFile in Files:
        if os.path.isfile(allFile)==False:
            splitName(allFile)
            


        
