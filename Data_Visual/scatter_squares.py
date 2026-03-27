import matplotlib.pyplot as plt
# 自动计算值
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
# 默认为蓝色点和黑色轮廓,散点图包含的数据点不多的时候效果不好
# 可以用edgecolors='none'来删除数据点的轮廓
# c参数设置为要使用的颜色的名称,也可以使用RGB颜色模式设置为元组
# 他的数值接近于0,指定的数值越深,越接近于1则越浅
# pyplot内置了一组颜色映射,可以设置选择哪一组颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
# 设置图表标题,并给坐标轴加上标签
# title用于绘制图表的标题,fontsize表示
plt.title('Square Numbers',fontsize=24)
# xlabel和ylabel能够为每个轴设置标题
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
# 设置刻度标记的大小,这里的both表示会同时影响x和y轴的刻度
# which的major只修改主刻度,通常是带标签的长刻度线;minor则是只修改次刻度,次刻度通常位于主刻度之间;both表示同时修改
plt.tick_params(axis='both',which='major',labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
# plt.show()
# plt.savefig的第一个实参指定要以什么样的文件名保存图表;第二个参数指定将图表空白的区域删除,如果想保留可以忽略
plt.savefig('squares_plot.png',bbox_inches='tight')