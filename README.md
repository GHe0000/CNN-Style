# CNN-P：基于TensorFlow-Slim的图片风格迁移
## 0：环境
- 64位系统（TensorFlow只支持64位）
- Python 3（建议用Anaconda或Miniconda）
- 安装TensorFlow >= 1.0（建议安装GPU版本）
```
pip install tensorFlow>=1.0
```
- 安装Pyyaml
```
pip install pyyaml
```

## 1：使用训练好的模型
- CMD切换到CNN-P根目录
- 使用命令：python eval.py --model_file 模型路径 --image_file 图片路径 例如
```
python eval.py --model_file models/wave.ckpt-done --image_file img/test.jpg
```
- Enjoy！

## 2.训练自己的模型

### 2.1：准备
- 下载[VGG16模型](http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz)并解压
- 在CNN-P根目录下新建一个文件夹pretrained，并将vgg16.ckpt复制到pretrained的文件夹下
- 下载[COCO数据集](http://msvocds.blob.core.windows.net/coco2014/train2014.zip)并解压到CNN-P根目录
- 打开conf/wave.yml,将其复制一份，并修改为<模型名字>.yml
- 打开它进行修改，将style_image：img/wave.jpg修改为被提取风格图片路径，name:"wave"修改为<模型名字>

### 2.2：训练
- CMD切换到CNN-P根目录
- 使用命令：python train.py -c conf/<模型名字>.yml
- （可选）使用命令打开数据可视化Tensorboard：tensorboard --logdir models/<模型名字>/

### 2.3：结束训练
- 差不多训练1万多次后
- Ctrl + C停止训练
- 在models/<模型名字>找到训练好的模型

## 3：备注
- 在img里可以找到训练好的模型的训练图，text.jpg为测试用图
- 感谢Google Colab提供免费GPU服务器（训练模型用）
- 在我家电脑（CPU:Intel Celeron E3400（PS:某宝最低包邮5元一个）无GPU加速）上使用训练好的模型进行测试只需26.812510秒