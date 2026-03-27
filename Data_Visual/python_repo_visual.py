import plotly.express as px
import requests

# 执行API调用并且查看响应
# 第一行是URL的主要部分
url='https://api.github.com/search/repositories'
# 第二行则是URL查询的字符串
url+='?q=language:python+sort:stars+stars:>10000'
# 显式的指定Github API的版本同时要求返回JSON格式
headers={"Accept":"application/vnd.github.v3+json"}
# requests调用API
r=requests.get(url,headers=headers)
# 状态码200表示请求成功,用以核查调用是否成功
print(f'Status code',r.status_code)
# 将响应转换为字典
response_dict=r.json()
# 处理结果
print(response_dict.keys())
print(f'Total repositories:{response_dict['total_count']}')
print(f'Complete results:{not response_dict['incomplete_results']}')
# 探索有关仓库的信息
repo_dicts=response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')
repo_links,stars,hover_texts=[],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    # 创建悬停文本
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)
# 可视化
title='Most-Starred Python Project on Github'
labels={'x':'Repository','y':'Stars'}
fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)
fig.show()