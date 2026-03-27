from pathlib import Path
import json

# 将数据作为字符串读取并转换为Python对象
# geojson文件适合于存储基于位置的数据,数据存储在一个于键feature相关的列表
path=Path('./data/eq_data_30_day_m1.geojson')
# 如果读取错误就是编码方式有错
try:
    contents=path.read_text()
except:
    contents=path.read_text(encoding='utf-8')
# json.loads方法将文件的字符串表示转换为Python对象
all_eq_data=json.loads(contents)
print(type(all_eq_data))
# 将数据文件转换为更易于阅读的版本
path=Path('./data/readable_eq_data.geojson')
# indent用于指定数据结构中嵌套元素的缩进量
readable_contents=json.dumps(all_eq_data,indent=4)
path.write_text(readable_contents)

# 查看数据集中的所有地震
all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))
mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])