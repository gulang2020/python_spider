# 					scrapy框架下的代理池使用

> 目标网站:http://www.glidedsky.com/level/crawler-ip-block-1

> #### 爬虫-IP屏蔽1**Passed**
>
> ------
>
> 大家说，页面做分页是因为单页内容太多。但分页还有一个不为人知的好处——用来反爬。
>
> 当一个爬虫尝试不断翻页爬取所有内容的时候，行为特征会非常容易识别。比如说，对高频率访问的IP进行封禁。
>
> 因为这是一个硬核的爬取攻防练习，常规高频封禁太弱了，所以这里的策略是：**你的每个IP，只能访问一次，之后就会被封禁。**
>
> 悄悄地告诉你，你之前用过的IP，已经被悄悄记录了~
>
> 这里有一个网站，分了1000页，求所有数字的和。



###### 任务目标:爬取1000页，每一页需要一个代理ip，代理ip不能重复，如果使用免费的代理池，会遇到数量较多的无用ip，无用ip的响应时间太长，十分影响效率，必须使用评分的代理池，我试过一些开源的代理池，不太理想，这里选择使用付费的代理。

### 

## 一.REDIS-代理池的实现

### 1.redis实现

```python
import redis
```

```python
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
```



## 二.使用scrapy中间件设置代理ip，从redis中获取ip

```
class ShieldipDownloaderMiddleware():
```

```
def process_request(self, request, spider):
```

```
def process_response(self, request, response, spider):
    if response.status == 403:
        print('进入403失败重连')
        return request
    return response
```

```
def process_exception(self, request, exception, spider):
    return request
```

通过以上三行实现代理池的重试

spider的scrapy.request里也要设置dont_filter=True

```python
yield scrapy.Request(full_url, dont_filter=True)
```



### 以上三个函数根据返回值的类型不同，处理的方式也会发生变化， 

### process_response()里返回request会使其重新加入下载调度器队列，

### process_exception()里返回request同理。



## 三.scrapy中cookies的导入

由于这个网站是登录后使用的，所以要插入cookies保持登录状态，

scrapy中使用cookies需要把cookies的类型转换成为字典类型，可以使用这段代码

```
b = '省略'
cookie = {}
for line in b.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value
print(cookie)
```



## 四.使用方式

同时运行![image-20200805215738910](C:\Users\pc_gulang\AppData\Roaming\Typora\typora-user-images\image-20200805215738910.png)和启动scrapy框架'pachong'