import os
from glob import glob
from os.path import join
#画像の名前を連番数字に
def rename_img(name):
    files=glob(join('test_img/'+name,"*.jpg"))
    i=0
    for file in files:
        os.rename(file,'test_img/'+name+'/'+name+str(i).zfill(4)+'.jpg')
        i+=1
        
def main():
    file_name=('hasimoto','inoue','iwaizono','kajioka','kanetou','kariya','shoji','sono','suzuki')    
    for name in file_name:
        rename_img(name)
        
        
if __name__=='__main__':
    main()