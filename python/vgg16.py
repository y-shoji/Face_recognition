import os
import numpy as np
from glob import glob
from os.path import join
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

#tensorflow with keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.utils import to_categorical
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.applications.vgg16 import VGG16
from tensorflow.python.keras.layers import Dropout,Flatten,Input,Dense
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array


def make_dataset(txt):
    X=[]
    Y=[]
    with open(txt,"r") as f:
        images=f.read().splitlines()
        for i in range(len(images)):
            #img_square(images[i][:-2]) #正方形に加工しない場合はコメントアウト
            img=load_img(images[i][:-2],target_size=(224,224))
            x=img_to_array(img)
            X.append(x)
            Y.append(images[i][-1])

    X=np.array(X)
    Y=np.array(Y)
    return X,Y

#渡したpathの一覧を作成
def create_txt(txt,path):    
    #すでにテキストが存在する場合削除する
    if os.path.exists(txt):
        os.remove(txt)
    
    #txtファイルに書き込む
    with open(txt,"a") as f:
        for name,label in classes.items():
            images=glob(join(path+name, "*.jpg"))
            for image in images:
                f.write(image+","+label+"\n")
 
#コンパイルの設定
def model_compile(model,Optimizer,Loss):
     model.compile(optimizer = Optimizer,
              loss = Loss,
              metrics=['accuracy'])
     
     return model

#vgg16モデルの作成
def build_VGG16_model(vgg16):
    model=Sequential(vgg16.layers)
    for layer in model.layers[:15]:
        layer.trainable=False
    
    #出力層の作成
    model.add(Flatten())
    model.add(Dense(units = 256, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(units = 64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(units = 9, activation='softmax'))
     
    return model_compile(model,Optimizer,Loss)


#トレーニングデータ学習
def model_train(model,X,Y):
    (X_tr,X_val,Y_tr,Y_val) = train_test_split(X,Y,test_size=0.2,random_state=0)
    es=EarlyStopping(monitor='val_loss',patience=10,verbose=1)
    history=model.fit(X_tr,Y_tr,batch_size=32,epochs=100,
                      validation_data=(X_val,Y_val),callbacks=[es])
    
    return model,history

#グラフ描画用
def graph_plot(history):
    plt.plot(history.history['acc'],color='red', marker='.', label='acc')
    plt.title('model accuracy')
    plt.grid()
    plt.plot(history.history['val_acc'], marker='.', label='val_acc')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.show()
    
    plt.plot(history.history['loss'], marker='.', label='loss')
    plt.title('model loss')
    plt.grid()
    plt.plot(history.history['val_loss'], marker='.', label='val_loss')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(loc='best')
    plt.show()

def main():
    #VGGもでるの読みこみ
    input_tensor = Input(shape=(224, 224, 3))
    vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)
    model=build_VGG16_model(vgg16)
    model.summary()
   
    #データセットの作成    
    create_txt(txts[0],'train_img\\')
    create_txt(txts[1],'test_img\\')
    X_train,Y_train=make_dataset(txts[0])
    X_test,Y_test=make_dataset(txts[1])
    #前処理(正規化)
    X_train=X_train.astype(np.float)
    X_test=X_test.astype(np.float)
    X_train=X_train/255
    X_test=X_test/255
    Y_train=to_categorical(Y_train,9)
    Y_test=to_categorical(Y_test,9)
 
    #CNNによる学習
    model,history=model_train(model,X_train,Y_train)
    #学習結果のグラフ描画
    graph_plot(history)
    #テストデータの検証結果の表示
    model.evaluate(X_test,Y_test)
       
    #学習モデル・重みの保存
    model.save('./model/model.h5')
   
   
   

if __name__=="__main__":
#グローバル変数の設定
    Optimizer = 'sgd'
    Loss = 'categorical_crossentropy'
    classes={'hasimoto':'0','inoue':'1','iwaizono':'2','kajioka':'3','kanetou':'4','kariya':'5','shoji':'6','sono':'7','suzuki':'8'}
    txts=["tr_list.txt","ts_list.txt"]
    
    main() 