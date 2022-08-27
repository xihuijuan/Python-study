> # 一、数据类型
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
>> - 双斜杠//运算符（地板除：取比目标结果小的最大整数）
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

> ## 二、逻辑运算符
>> - and
>>   - 左边和右边同时为Ttue，结果为True
>> - or
>>   - 左边或者右边的其中之一为True，结果为True
>> - not
>>   - 如果操作数为True，结果为False
>>   - 如果操作数为False，结果为True
>> - 真值测试
>>   - python中任何对象都等直接进行真值测试（测试该对象的布尔类型值为True或者False），用于if或者while语句的条件判断，也可以作为布尔逻辑运算符的操作数

```python
3 and 4 结果为：4，逻辑运算符结果不一定都是true和false
"FishC" and "Love" 结果为：Love，如果and或者or两边是字符串返回值也是字符串，如果是数字即返回为数字
```
>> - 短路逻辑和运算符优先级
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
>>
>>
>>
>>
>>
>>
