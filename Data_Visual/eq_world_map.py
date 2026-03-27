import plotly.express as px
from eq_explore_data import *
import pandas as pd

data=pd.DataFrame(data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级'])
print(data.head())
fig=px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    # 设置渐变色
    color='震级',
    # 设置悬停说明文本
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()