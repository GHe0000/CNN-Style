# CNN-P：图片风格转换器，基于CNN卷积神经网络
## 0.环境
- 64位系统（32位机装64位系统先，CPU不支持X64我也没办法......）
- Python3（建议使用Anaconda或Miniconda）
- TensorFlow（建议安装GPU版），Numpy，Scipy，PIL等库（只记得要装这几个库......）
## 1.下载和使用
- 下载CNN-P并解压缩
- [下载图片识别模型VGG-19](http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat)并复制到CNN-P的根目录（VGG-19模型太大上传不了......）
- CMD切换到CNN-P根目录
- 使用命令：python neural_style.py --content 输入图路径 --styles 风格图路径 --output 输出图路径
- Enjoy
<<<<<<< HEAD
## 3.��������
- ��neural_style.py
- ��26�У�ITERATIONS = ����������Ĭ��550��
## ��
- ����һ��59KB���ļ�����550�λ�������Сʱ��ȫ��CPU(E3400 ����E3400����һ������CPU��ĳ��5Ԫһ��......)ռ����100%(�˴�ռ���ʻ���)
- ������ѧ������ѧ ��1704 �ι��� �Ƽ����������
=======
## 3.参数更改
- 打开neural_style.py
- 第26行：ITERATIONS = 代迭次数（默认550）
## 附
- 本人一个59KB的文件代迭550次花了两个小时，全程CPU(E3400 附：E3400真是一个垃圾CPU，某宝5元一个......)占用率100%(运存占用率还好)
>>>>>>> a561f7310e9851480de87a5db51a4651ce835495
