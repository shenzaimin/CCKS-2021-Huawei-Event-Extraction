# CCKS-2021-Huawei-Event-Extraction

# 华为面向通信领域的过程类事件抽取baseline方案及代码

## 环境安装
> 依赖文件路径code/conda.txt  和  code/pip.txt <br/>
> 1.conda创建python==3.8环境以及依赖包:  conda env create -f conda.txt <br/>
> 2.Pip安装依赖包： pip install -r pip.txt <br/>

## 硬件条件及耗时
> 硬件需求：GPU显存11G及以上（eg. Nivdia 2080Ti）<br/>
> 耗时（eg. Nvdia 2080Ti）：<br/>
> 分类模块:10-15 min <br/>
> 事件抽取模型（esemble）: 6-7 hour <br/>
## 1.执行分类模型：
训练集数据路径：CCKS-Cls/dataset/trans_train.json <br/>
测试集数据路径：CCKS-Cls/dataset/trans_test.json <br/>
> cd CCKS-Cls/ <br/>
> sh classification.sh <br/>
得到分类结果文件:CCKS-Cls/test_output/cls_out_single.csv <br/>

> 说明：chinese_roberta_wwm_large_ext_pytorch 预训练模型文件路径 code/CCKS-Cls/pretrained_model/Bert-wwm-ext/ <br/>
下载链接： <br/>
http://pan.iflytek.com/#/link/9B46A0ABA70C568AAAFCD004B9A2C773 <br/>
提取密码：43eH <br/>


## 2.执行事件抽取
训练集数据路径：data/train/trans_train.json <br/>
以及data/train/train_base.json(这个是A榜的训练集，需要加入进来，作为预训练模型的”权重学习资料”) <br/>
测试集数据路径：data/dev/trans_test.json <br/>

根目录得到结果文件 result.json  <br/>
### 事件抽取执行步骤
### 1.chinese_roberta_wwm_large_ext_pytorch 预训练模型文件路径 code/chinese_roberta_wwm_ext_pytorch/
> 下载链接： <br/>
http://pan.iflytek.com/#/link/9B46A0ABA70C568AAAFCD004B9A2C773 <br/>
提取密码：43eH <br/>


### 2.基础子模型训练：train_roberta_model_ensemble.py依据每个事件抽取框架会生成若干个基本模型


### 3.投票预测：采用投票基于上述esemble模型进行每个事件的集成预测，生成结果文件result.json(存放路径为result.json)

