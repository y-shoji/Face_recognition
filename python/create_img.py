# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:30:51 2019

@author: shjyt
"""


import cv2

def from_avi_to_jpg(input_path,output_path,num_frames,name,j):
    #ビデオの読み込み
    video = cv2.VideoCapture(input_path)
    #ビデオをフレームに分ける
    for i in range(0,num_frames):
        ret,flame=video.read()
        cv2.imwrite(output_path+str(j)+'/'+name+str(i)+'.jpg',flame)
        
def capture_face(input_path,num,k):
   # cv_path=cv2.__path__
    #cascade_path = cv_path+"\\data\\haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    for i in range(num):
        img=cv2.imread(input_path+str(i)+'.jpg',cv2.IMREAD_GRAYSCALE)
        facerect = cascade.detectMultiScale(img,  scaleFactor=1.1, minNeighbors=3, minSize=(224, 224))
        for j,rect in enumerate(facerect):
            x=rect[0]
            y=rect[1]
            w=rect[2]
            h=rect[3]
            img2=img[y:y+h, x:x+w]
            if i<250:
                cv2.imwrite('train_img/'+str(k)+'/img'+str(i)+'.jpg',cv2.resize(img2,(224,224)))
            else:
                cv2.imwrite('test_img/'+str(k)+'/img'+str(i)+'.jpg',cv2.resize(img2,(224,224)))


def main():
    #for i in range(9):
        #from_avi_to_jpg('video/'+str(i)+'.avi','img/',300,'No'+str(i)+'_',i)
    for i in range(9):
        capture_face('img/'+str(i)+'/No'+str(i)+'_',300,i)

if __name__=="__main__":
    main()