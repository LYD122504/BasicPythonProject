from operator import itemgetter
import requests

# 执⾏ API 调⽤并查看响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:100]:
    # 对于每个文章都执行一次API调用
    url=f'https://hackernews.firebaseio.com/v0/item/{submission_id}.json'
    r=requests.get(url)
    print(f'id:{submission_id}\tstatus code:{r.status_code}')
    response_dict=r.json()