# CNN-P������TensorFlow-Slim��ͼƬ���Ǩ��
## 0������
- 64λϵͳ��TensorFlowֻ֧��64λ��
- Python 3��������Anaconda��Miniconda��
- ��װTensorFlow >= 1.0�����鰲װGPU�汾��
```
pip install tensorFlow>=1.0
```
- ��װPyyaml
```
pip install pyyaml
```

## 1��ʹ��ѵ���õ�ģ��
- CMD�л���CNN-P��Ŀ¼
- ʹ�����python eval.py --model_file ģ��·�� --image_file ͼƬ·�� ����
```
python eval.py --model_file models/wave.ckpt-done --image_file img/test.jpg
```
- Enjoy��

## 2.ѵ���Լ���ģ��

### 2.1��׼��
- ����[VGG16ģ��](http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz)����ѹ
- ��CNN-P��Ŀ¼���½�һ���ļ���pretrained������vgg16.ckpt���Ƶ�pretrained���ļ�����
- ����[COCO���ݼ�](http://msvocds.blob.core.windows.net/coco2014/train2014.zip)����ѹ��CNN-P��Ŀ¼
- ��conf/wave.yml,���临��һ�ݣ����޸�Ϊ<ģ������>.yml
- ���������޸ģ���style_image��img/wave.jpg�޸�Ϊ����ȡ���ͼƬ·����name:"wave"�޸�Ϊ<ģ������>

### 2.2��ѵ��
- CMD�л���CNN-P��Ŀ¼
- ʹ�����python train.py -c conf/<ģ������>.yml
- ����ѡ��ʹ����������ݿ��ӻ�Tensorboard��tensorboard --logdir models/<ģ������>/

### 2.3������ѵ��
- ���ѵ��1���κ�
- Ctrl + Cֹͣѵ��
- ��models/<ģ������>�ҵ�ѵ���õ�ģ��

## 3����ע
- ��img������ҵ�ѵ���õ�ģ�͵�ѵ��ͼ��text.jpgΪ������ͼ
- ��лGoogle Colab�ṩ���GPU��������ѵ��ģ���ã�
- ���Ҽҵ��ԣ�CPU:Intel Celeron E3400��PS:ĳ����Ͱ���5Ԫһ������GPU���٣���ʹ��ѵ���õ�ģ�ͽ��в���ֻ��26.812510��