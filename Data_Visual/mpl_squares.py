import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
# linewidth用于控制线宽
plt.plot(input_values,squares,linewidth=5)
# 设置图表标题,并给坐标轴加上标签
# title用于绘制图表的标题,fontsize表示
plt.title('Square Numbers',fontsize=24)
# xlabel和ylabel能够为每个轴设置标题
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
# 设置刻度标记的大小,这里的both表示会同时影响x和y轴的刻度
plt.tick_params(axis='both',labelsize=14)
plt.show()