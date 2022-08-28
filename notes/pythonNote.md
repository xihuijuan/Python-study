 # 一、数据类型
>> ## 整数 integers
>> - 所有的整数
>> ## 浮点数
```python
//示例：
0.1+0.2 = 0.300000000004
```
>>- 存储存在误差
>>    - 解决误差：decimal模块
>>    - 通过一下代码块解决误差

```python
    import decimal
    a = decimal.Decimal('0.1')
    b = decimal.Decimal('0.2')
    print(a+b)//结果为0.3而不是0.30000004
```

>> ## 复数
>>- 实部和虚部
>>
  ```python  
  //示例，1为实部,2j为虚部均以浮点数形>>式存在
    1+2j
    将x = 1 + 2j
    x.real//获取实部的数值1.0
    x.imag//获取虚部的数值2.0
  ```
>> ## 数值之间的运算
>> - 双斜杠//运算符（地板除：取比目标结果小的最大整数，向下取整）
```python
3//2   结果为1
-3//2  结果为-2
```
>> - %运算符

```python
3%2 结果为1
6%2 结果为0
```
>> - 函数divmod(x,y)
>>    - 由上述两个符号得出结论x == (x//y)*y +(x%y)，故引出一个函数divmod(x,y),函数返回值为(x//y,x%y),即同时求出地板除和取模的结果
```python
divmod(3,2)  结果为：(1,1)
divmod(-3,2) 结果为：(-2,1)
```
>> - abs(x)绝对值

```python
abs(-1)  结果为1
abs(1)   结果为1
复数没有绝对值，故abs()传入复数返回值为复数的模
abs(1+2j)  结果为：2.23606797749979
```

>> - int()取整数

```python
int(3.14)  结果为3
int(9.99)  结果为9，只取整，不进行四舍五入
```
>> - float(x)转换浮点数，complex(x)转换为复数

```python
float('3.14')   结果为：3.14
float('520')    结果为：520.0
complex('1+2j') 结果为：1+2j
```

>> - pow(x,y)计算x的y次方，x**y计算x的y次方

```python
pow(x,y)  结果为：8
x**y      结果为：8
上述两个值得情况下，返回值相同
但pow()还有第三个参数，当有第三个参数时，两个计算的返回值则不同
pow(2,3,5)   结果为：3，即 2 ** 3 % 5
```
>> ## 布尔类型
>>- bool()
>>      - 除了bool("")、bool(False)和bool(0)等（见下图）的返回值为false，其他情况返回值均为true
![01布尔为false的情况](../notes/imgs/01%E5%B8%83%E5%B0%94%E4%B8%BAfalse%E7%9A%84%E6%83%85%E5%86%B5.png)

```python
定义为False的对象：None和False
值为0的数字类型：0,0.0,0j,Decimal(0),Fraction(0,1)
空的序列集合：'',(),[],{},set(),range(0)
```

 # 二、逻辑运算符
>> ## and
>>   - 左边和右边同时为Ttue，结果为True
>> ## or
>>   - 左边或者右边的其中之一为True，结果为True
>> ## not
>>   - 如果操作数为True，结果为False
>>   - 如果操作数为False，结果为True
>> ## 真值测试
>>   - python中任何对象都等直接进行真值测试（测试该对象的布尔类型值为True或者False），用于if或者while语句的条件判断，也可以作为布尔逻辑运算符的操作数

```python
3 and 4 结果为：4，逻辑运算符结果不一定都是true和false
"FishC" and "Love" 结果为：Love，如果and或者or两边是字符串返回值也是字符串，如果是数字即返回为数字
```
>> ## 短路逻辑和运算符优先级
>> - 短路逻辑
```python
//为什么思考下列结果为4？
(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 0)
//因为and和or遵循短路逻辑
//从左往右，只有当第一个操作数的值无法确定逻辑运算的结果时，才对第二个操作数进行求值
3 and 4   结果：3
3 or 4    结果：4
0 and 3   结果：0
0 or 3    结果：3
==>(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
==>False or 0 or 4 or 6 or 9
==>4

```
>>   - 运算符优先级
```python
==>not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
==>4  //4以后的都不参与对比了
```
>>      - 先乘除后加减==>大于小于==>not==>and==>or
```python
not 1<2           结果：False，先比较1<2，在not
0 or 1 and not 2  结果：False
```
 # 三、分支和循环
>> ## 分支结构
>>  - 单条件判断
```python
if 1>0:
  print()
else:
  print()
```
>>  - 多条件判断

```python
if condition1:
  statement(s)
elif condition2:
  statement(2)
elif condition3:
  statement(2) 
```

>>  - 条件表达式

```python 
age = 16
if age <18:
  print('抱歉，未满十八禁止入内')
else:
  print('欢迎访问')

、、替换为条件表达式为
print('抱歉，未满十八禁止入内') if age <18 else print('欢迎访问')

//比较两个数的大小，并将较小的数赋值给一个叫做small的变量
a = 3
b = 5
samll = a if a < b else small = b

score = 66
level = ('D' if 0 <= score < 60 else
        'C' if 60 <= score <80 else
        'B' if 80 <= score <90 else
        'A' if 90 <= score <100 else
        'S' if score == 100 else
        "请输入0~100的整数")
print(level)   结果为'C'
```

>>  - 分支结构的嵌套
>>    - 多条件嵌套
>>  ## 循环结构
>>  - while循环
```python
love = 'yes'
while love == 'yes':
  love = input('今天你还爱我吗')

//计算1 - 1万的和
i = 1
sum = 0
while i<= 10000:
  sum+=i
  i+=1
print(sum)
```
>>  - break退出整个循环

```python
while True:
  answer = input('可以退出循环了吗')
  if answer == '可以':
    break
  print('好累')
```
>>  - continue只跳出本轮循环

```python
i= 0
while i < 10:
  i+=1
  if i % 2 ==0:
    continue
  print(i)  //结果为：1,3,5,7,9
```
>> - else当循环条件不为真时被执行
```python
//无break语句的情况下
i = 1
while i < 3:
  print("循环结构内，i的值为："+ i)
  i+=1
else:
  print("循环结构外，i的值为：" + i)
//结果为：循环结构内，i的值为： 0
         循环结构内，i的值为： 1
         循环结构内，i的值为： 2
         循环结构外，i的值为： 3
```

```python
//break语句跳出循环，则else不会被执行
i = 1
while i < 3:
  print("循环结构内，i的值为："+ i)
  if i == 2:
    bleak
  i+=1
else:
  print("循环结构外，i的值为：" + i)
//结果为：循环结构内，i的值为： 0
         循环结构内，i的值为： 1
         循环结构内，i的值为： 2
```

>> 思考：while  else的设计有什么实质上的作用吗？
>>> - 非常容易的检测到循环的退出情况

```python
day = 1
while day <=7:
    answer = input('今天有好好学习吗？')
    if answer != "有":
        print('非常遗憾，你没有打卡7天，只打卡',day,'天')
        break
    day += 1
else:
    print('非常棒，已经坚持打卡7天！')
//如果'非常棒，已经坚持打卡7天！'没有打印，则说明循环异常跳出
```
>> - 循环嵌套

```python
//99乘法表
//自己写的
i = 1
while i <= 9:
    j = i
    while j <= 9:
        print(i,' * ',j,' = ',i*j)
        j+=1
    i+=1
//老师写的,外层i负责行，内层j负责列
i = 1
while i<=9:
    j = 1
    while j<=i:
        print(j,' * ',i,' = ',i*j,end=" ")
        j+=1
    print()
    i+=1
```
>> break，continue只作用于一层循环体
```python
//每天学习，坚持到一小时放弃，一周可以7小时
day = 1
hour = 1
while day <= 7:
  while hour <= 8:
    print('今天要学习8小时')
    hour+=1
    if hour > 1:
      break
  day+=1

//自己改良以后的
day = 1
counts = 0
while day <= 7:
  hour = 0
  while hour <= 8:
    hour+=1
    if hour >= 2:
      print('第',day,'天，学习',hour,'小时,可以出去玩啦')
      break
  counts = counts + hour - 1
  day+=1
print('本周只学习了',counts,'小时')
```
>> - for循环
>>   - 语法

```python
 for 变量 in 可迭代对象:
  statement(s)
```
>>   - 示例

```python
for each in 'FishC':
  print(each)
//结果为：f   i   s  h  C
```

>>   - range() 示例

```python
range(10)//获取 0-10 (不包含10) 的数字
range(5,10)//获取从5开始到10（不包含10）的数字
range(5,10,2)//跨度为2，取值为 5,7,9
range(10,5,-2)//取值为 10,8,6
```

>>   - for和range（）组合，实现10000以内的数字相加

```python
sum = 0
for i in range(10001):
  sum += i
print(sum)
```

>>   - 找出10以内的所有素数

```python
for n in range(2,10):
  for x in range(2,10):
    if n % x == 0:
      print(n ,'=',x,'*',n//x)
    else:
      print(n,'是一个素数')
```

 # 四、列表
>> ## 创建列表
>> - [1,2,3,4,5]列表可以容纳不同类型的数据
