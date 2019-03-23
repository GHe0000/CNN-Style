# 2019年科技文化艺术节 初1704 Guotao He

# CNN-Style：基于TensorFlow-Slim的图片风格迁移（单Eval）
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

## 使用
- CMD切换到CNN-Style根目录
- 使用命令：python eval.py --model_file 模型路径 --image_file 图片路径 例如
```
python eval.py --model_file wave.ckpt-done --image_file test.jpg
```
- Enjoy！

## 3：备注
- 在img里可以找到训练好的模型的训练图，text.jpg为测试用图
- 感谢Google Colab提供免费GPU服务器（训练模型用）
- 在我家电脑（CPU:Intel Celeron E3400（PS:某宝最低包邮5元一个）无GPU加速）上使用训练好的模型进行测试只需26.812510秒
