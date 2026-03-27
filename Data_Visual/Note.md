# Data Visual(数据可视化项目)


<a id="org172fba6"></a>

## matplotlib.pyplot(静态绘图)

常用的导入这个包的指令是

```python
import matplotlib.pyplot as plt
```

plt.figure的作用是创建一个新的绘图窗口,其中figsize接受一个元组(width,height);dpi则表示图像的分辨率,默认参数为80像素每英寸.

```python
plt.figure(figsize=(width,height),dpi=128)
```

plt.plot的作用则是绘制线图,前面两个参数表示x轴数据和y轴数据,linewidth控制线条的粗细,alpha的作用则是指定颜色的透明度,alpha为0表示完全透明,1是默认设置,表示完全不透明.

```python
plt.plot(input_values,output_values,linewidth=5,aplha=0.5)
```

plt.scatter的作用则是绘制散点图.前两个的参数表示x轴数据和y轴数据,参数s的作用则是控制散点的大小,可以用固定的浮点数控制,也可以用数值列表的方式控制大小关系.参数c的作用则是控制散点的颜色,可以是颜色字符串,也可以是一个数值列表映射到cmap.cmap是一个颜色映射,如plt.cm.Blues,数值越大颜色越深.edgecolors表示点的轮廓颜色,设置为'none'可使得密集散点更具整体感.

```python
plt.scatter(x,y,s=40,c=y,cmap=plt.cm.Blues,edgecolors='none')
```

plt.fill\_between的作用是在两条曲线内填充阴影,常用于表示误差区间或气温范围.他的基本参数需要输入一个x值序列和两个y值序列,用于定位两条曲线.facecolor指定采用的填充颜色,alpha则是设置透明度(0-1之间).

```python
plt.fillbetween(x,y1,y2,facecolor='blue',alpha=0.1)
```

如果我们希望隐藏所绘制图像的坐标轴,如果我们直接使用

```python
plt.axes().get_xaxis().set_visible(False)
```

会覆盖原来的图,所以我们需要先用plt.gca()来获取原来的图像的坐标轴对象,再将其设置为不可见,代码如下所示,

```python
ax = plt.gca() 
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
```


<a id="org248a462"></a>

## plotly.express(交互式绘图)

常用的导入这个包的指令是

```python
import plotly.express as px
```

px.bar的作用是生成交互式条形图.我们可以直接输入x对应的数据和y对应的数据,也可以输入dataframe对象,并在x中指定所需要的列名,y中指定所需要的列名.title用于传入一个标题字符串,labels接受一个字典,用于指定x和y轴的名称.hover\_name指定悬停在数据条上时显示的标题字段.

```python
px.bar(dataframe,x,y,title,labels,hover_name
```

px.scatter的作用是生成交互式散点图.基本都是一样的,size和color与前面提到x,y一样可以关联到DataFrame的列名,实现根据额外数据自动调整散点大小和颜色深浅.

```python
px.scatter(dataframe,x,y,size,color,hover_name)
```

fig.update\_layout的作用是更新图表的布局.xaxis\_dtick设置坐标轴刻度的步长(如设置为1,那么每个整数刻度都会显示).

```python
fig.update_layout(xaxis_dtick=1)
```

fig.update\_traces可以用于定制图像呈现的数据.中 marker\_打头的参数都会影响图形上的标记,maker\_color是将每个标记的颜色都设定成某个颜色,marker\_opacity设置不透明度.

```python
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
```


<a id="org0b83c0a"></a>

## 数据处理和网络请求

我们先介绍json模块,其调用方式为

```python
import json
```

json.loads的作用是将JSON格式的字符串转换为Python对象,通常是字典或者列表

```python
json.loads(contents)
```

json.dumps的作用是将Python对象转化为JSON字符串,indent的作用是一个美化输出,指定嵌套层级的缩进空格数.

```python
json.dumps(obj,indent=4)
```

其次是requests模块,其调用方式为

```python
import requests
```

requests.get的作用是向服务器发送HTTP GET请求,参数headers字段常用于设置接受的数据格式,例如Github API要求指定vnd.github.v3+json

```python
# 显式的指定Github API的版本同时要求返回JSON格式
headers={"Accept":"application/vnd.github.v3+json"}
# requests调用API
r=requests.get(url,headers=headers)
```

r.statuscode返回响应状态码,200表示请求成功,可以继续处理数据,

```python
r.status_code
```

r.json直接将API返回的响应体解析为Python字典/列表

```python
r.json()
```