from os.path import join
from glob import glob
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array,ImageDataGenerator

#水増し実行部 
def image_generate(image,name,directory):
    #画像をkerasの形式にする
    img=load_img(image)
    x=img_to_array(img)
    x=x.reshape((1,) + x.shape)
    g=datagen.flow(x,batch_size=1,save_to_dir=directory,save_format='jpg')
    
    #画像を水増し
    for i in range(5):
        batch=g.next()

#水増しmain関数
def iamge_augmentation_main():
    for name in classes.keys():
        directory="test_img\\"+name
        images=glob(join(directory, "*.jpg"))
        for image in images:
            image_generate(image,name,directory)
            
if __name__=="__main__":
    #グローバル変数の設定
    classes={"yui":"0","inori":"1","sumire":"2","marei":"3"}
    datagen=ImageDataGenerator(          
            rotation_range=20, # 画像をランダムに回転する回転範囲
            width_shift_range=2, # ランダムに水平シフトする範囲
            height_shift_range=3, # ランダムに垂直シフトする範囲
            shear_range=10, # シアー強度（反時計回りのシアー角度（ラジアン））
            horizontal_flip=True, # 水平方向に入力をランダムに反転
            brightness_range=[0.7, 1.0], #明度変換
            channel_shift_range=5., #gasotuikaa
    )
    iamge_augmentation_main()