# CSS偏移雪碧图反爬

目标网站：http://gz.ziroom.com/z/

##### 任务概述：目标网站的房租金额使用了雪碧图CSS偏移反爬技术。

![image-20200811121314508](C:\Users\pc_gulang\AppData\Roaming\Typora\typora-user-images\image-20200811121314508.png)

##### ![image-20200811121230939](C:\Users\pc_gulang\AppData\Roaming\Typora\typora-user-images\image-20200811121230939.png)

如上图，网站定位到1390的时候，elements显示的是图片链接，不同的数字对应不同的偏移量，如-85.6px，下载其中一个图片，

![image-20200811121534680](C:\Users\pc_gulang\AppData\Roaming\Typora\typora-user-images\image-20200811121534680.png)

根据逻辑可以推测出，px就是偏移量，经过推理后可以计算出每格21.4就跳过一个格，所以通过px值可以定位到不同的数。

分析网站可以知道，网站每次刷新得到的数字图片是不一样的，所以每次get数字图片都得下载和分析一次数字图片。

这里可以使用某些方法识别图片数字，然后讲数字和对应的px偏移量做成对照字典，便可以通过偏移量得到具体的数字了，如 -'85.6'： '2'

这里使用muggle_ocr包进行数字图像识别。

### 知识点1 spilt()切割url

获取数字图片url，并且使用url最后一段作为名字。

```python
photo_url = 'http:' + re.findall('<span class="num" style="background-image: url\((.*?)\)', html)[0]
photo_name = photo_url.split('/')[-1]
```

split('/')[-1]： -1 ：全切 0 ：不切 1：切一刀 （每一块都保留）[-1]:将最后一块切割出来  [-2]：将倒数第二块切割出来 （只保留切出来的一块）



### 知识点2 读取xpath对象的数据

```
result = etree.tostring(one_data, encoding='utf-8')
```



### 重要知识点 使用muggle-orc包对数字图片进行分析

参考链接:https://blog.csdn.net/kerlomz/article/details/106467876

最开始是使用pytesseract进行数字图片识别，效果很差，muggle-orc包完美的解决了问题，就是包的环境配置比较麻烦，比如tensorflow numpy等都需要更改版本。

```
import muggle_ocr
```

```python
# 初始化
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
with open(photo_name, "rb") as f:
    b = f.read()
    text = sdk.predict(image_bytes=b)
```

十分简单，text返回一个str类型，很简单就能处理了。



### 知识点3 两个列表组合成字典

```python
for k, v in zip(self.html_offsets, list_nums):
    self.real_nums[k] = v
```

k是key，v是value，通过这个方法使两个列表组成字典，在这组成了偏移量和数字的对照表



### 知识点4 format保留小数

```
 b = format(b, '.1f')  # 保留小数一位
```

### 

### 知识点5 判断文件是否存在

```
os.path.exists(file)
```



### 知识点6 json

loads： 是将string转换为dict
dumps： 是将dict转换为string
load： 是将里json格式字符串转化为dict，**读取文件**
dump： 是将dict类型转换为json格式字符串，**存入文件**

为了加快爬取速度，如果每一页都对其的数字图片进行识别和下载，势必会降低爬取速度，

这里选择讲偏移对照字典存入json中，在通过判断字典是否存在来判断是识别图片。

例子

```python
with open(file, 'w') as f:
    json.dump(dict_test, f)  # 写入
with open(file, 'r') as f:
    a = json.load(f)  # 读取
```



### 知识点7 简短的语句去除列表中的空元素和空格

```
tag = list(map(lambda x: x.strip(), tag))
tag = [i for i in tag if i != '']
```

map返回的是一个list，需要用list将其转换为列表