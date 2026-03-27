import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 从文件中获取日期,最高气温和最低气温
filename='./data/death_valley_2021_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    highs,dates,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[2],'%Y-%m-%d')
            high=int(row[3])
            low=int(row[4])
        except ValueError as e:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(highs)
# 根据数据绘制图像
fig=plt.figure(dpi=128,figsize=(10,6))
# alpha的作用则是指定颜色的透明度,alpha为0表示完全透明,1是默认设置,表示完全不透明
# fill_between的作用是接受x值系列和两个y值系列,并填充两个y值系列之间的空间
# facecolor指定了区域填充的颜色
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置图形的格式
plt.title('Daily high and low temperatures - 2021\nDeath Valley',fontsize=24)
plt.xlabel('',fontsize=16)
# 调用autofmt_xdate来绘制倾斜的日期标签,避免彼此重叠
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()