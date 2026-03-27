from die import Die
import plotly.express as px

# 创建两个六面骰子 D6
die_1=Die()
die_2=Die(10)
# 掷几次骰子,并将结果存储在一个列表中
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
# 分析结果
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
# range不会包含最后一个位置,所以需要+1保证被纳入
poss_results=range(2,max_result+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

# title用于标示直方图的字符串
title='Results of rolling two D6 dice 1000 times'
# 设置两个坐标轴的标题
labels={'x':'Result','y':'Frequency of Result'}
# 对结果进行可视化
hist=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
# 进一步定制图形
hist.update_layout(xaxis_dtick=1)
hist.show()