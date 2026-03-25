- 在for循环中,不应该从列表或编组中删除条目,因此最好是遍历副本的方式.如果直接对列表做删除条目,那么代码如下所示,

  ```python
  numbers = [1, 2, 2, 3]
  for n in numbers:
      if n == 2:
          numbers.remove(n)
  print(numbers)
  # 结果为[1,2,3]
  ```

这是因为当n读取到第一个2的时候,numbers会把他移除,同时将后续的项往前挪了一位,也就是将第2位的2移动到了第一位的2的地方,此时n则会继续向后移动,所以会保留一个2.

```python
numbers=[1,2,2,2,3]
for n in numbers.copy():
    if n==2:
        numbers.remove(n)
print(numbers)
# [1,3]
```

这是因为用了copy()获得了原来的副本,原来列表的删除不会影响副本,所以会将2删干净.

-   主循环包含尽可能少的代码,只需要看函数名字就知道处理的过程

-   round函数一般使用于精确到小数点后多少位,其中小数位数由第二个实参指定.如果将第二个实参设定为负数,那么round就会把他圆整到10,100,1000等整数倍.

    ```python
    round(number,-1)
    ```

python中的{:,}是一个比较常用的占位符,他的主要作用是给数字添加千分位分隔符.

```python
number = 1234567.8
# 使用 f-string (推荐)
print(f"{number:,}") 
# 输出: 1,234,567.89
# 使用 format() 函数
print("{:,}".format(10000))
# 输出: 10,000
```