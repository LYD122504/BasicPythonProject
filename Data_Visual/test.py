from pathlib import Path
import json
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
# son.dumps()函数接受⼀个实参,即要转换为JSON格式的数据
# 函数返回⼀个字符串
contents = json.dumps(numbers)
path.write_text(contents)

path=Path('numbers.json')
contents=path.read_text()
numbers=json.loads(contents)
print(numbers)