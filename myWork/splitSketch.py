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
    if os.path.exists(path+'/'+img):
        getImg=cv2.imread(path+'/'+img)
        if getImg is not None:
            sp=getImg.shape
            return sp[0],sp[1]
        else:
            return 0,0

def getOriAndSketch(path='',img1=''):#返回的是彩色图和线稿图
    getImg1=cv2.imread(path+'/'+img1)
    k=0
    if os.path.exists(path+'/'+img1):
        img1Height,img1Width=getHeightAndWidth(path+'/',img1)
    if img1Height==0:
        return

    bAll=0
    gAll=0
    rAll=0
    [b,g,r]=getImg1[int(img1Height)-1,int(img1Width)-1]
    for i in range(int(img1Width)-1):
        [b,g,r]=getImg1[(img1Height)/2,i]
        bAll=b+bAll
        gAll=g+gAll
        rAll=r+rAll
    b=bAll/(img1Width-1)
    g=gAll/(img1Width-1)
    r=rAll/(img1Width-1)
    if (b>245 and g>245 and r>245):
        shutil.copyfile(path+'/'+img1,'sketch/'+img1)
        return img1,1
    elif(b<200 or r<200 or g<200):
        shutil.copyfile(path+'/'+img1,'ori/'+img1)
        return img1,0
    else:
        return 2  
"""
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

"""

if __name__=='__main__':
    print '请将图片目录放入存放图片的文件夹，并且做好备份，运行会删除原文件'
    Files=os.listdir('test')
    for allFile in Files:
        print allFile
        getOriAndSketch(path='test',img1=allFile)

