import os
import numpy as np
from os.path import join
from glob import glob
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array
from matplotlib import pyplot as plt
from tensorflow.python.keras.utils import to_categorical
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.layers import Conv2D,MaxPooling2D,Dropout,Flatten,Dense

def make_dataset(txt):
    X=[]
    Y=[]
    with open(txt,"r") as f:
        images=f.read().splitlines()
        for i in range(len(images)):
            #img_square(images[i][:-2]) #正方形に加工しない場合はコメントアウト
            img=load_img(images[i][:-2],target_size=(img_h,img_w))
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
  
              
def CNN(unit):
    model=Sequential()
    #畳み込み層
    model.add(
        Conv2D(
            filters=32,input_shape=(img_h,img_w,3),
            kernel_size=(3,3),strides=(1,1),
            padding='same',activation='relu'))
    model.add(
        Conv2D(
            filters=32,
            kernel_size=(3,3),strides=(1,1),
            padding='same',activation='relu'))

    #プーリング層
    model.add(MaxPooling2D(pool_size=(2,2)))
    #畳み込み層
    model.add(
        Conv2D(
            filters=64,kernel_size=(3,3),strides=(1,1),
            padding='same',activation='relu'))
    #プーリング層
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    #全結合層
    model.add(Dense(units=unit,activation='relu')) 
    model.add(Dropout(0.5))
    model.add(Dense(units=unit//3,activation='relu')) 
    model.add(Dropout(0.5))
    #出力層
    model.add(Dense(units=9,activation='softmax')) 
    
    model.compile(
        optimizer='Adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'])
    
    return model

#トレーニングデータ学習
def model_train(X,Y):
    model=CNN(256)
    (X_tr,X_val,Y_tr,Y_val) = train_test_split(X,Y,test_size=0.2,random_state=0)
    es=EarlyStopping(monitor='val_loss',patience=10,verbose=1)
    history=model.fit(X_tr,Y_tr,batch_size=64,epochs=50,
                      validation_data=(X_val,Y_val),callbacks=[es])
    
    return model,history

#テストデータ検証   
def model_evaluate(model,X,Y):
    score=model.evaluate(X,Y)
    print('test score')
    print('loss=',score[0])
    print('acc=',score[1])

#グラフ描画用
def graph_plot(history):
    plt.plot(history.history['accuracy'],color='red', marker='.', label='acc')
    plt.title('model accuracy')
    plt.grid()
    plt.plot(history.history['val_accuracy'], marker='.', label='val_acc')
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
    
#メイン関数
def main():
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
    model,history=model_train(X_train,Y_train)
    #学習結果のグラフ描画
    graph_plot(history)
    #テストデータの検証結果の表示
    model_evaluate(model,X_test,Y_test)
       
    #学習モデル・重みの保存
    model.save('./model/model.h5')
    
    #for i in range(7):
       # print(acc[i],loss[i])
    

if __name__=="__main__":
    #グローバル変数の設定
    classes={'hasimoto':'0','inoue':'1','iwaizono':'2','kajioka':'3','kanetou':'4','kariya':'5','shoji':'6','sono':'7','suzuki':'8'}
    txts=["tr_list.txt","ts_list.txt"]
    img_w=224
    img_h=224

    main()
