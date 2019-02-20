# python_learn
学习[廖雪峰的python3](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)过程中做的练习,以及总结一些要点。

## 要点
1. 数据类型检查可以用内置函数 `isinstance()`
   
   `isinstance(x, (int, float))`
   
2. 判断一个变量是否是`None`
   
   `a is None`
   
3. 利用切片复制一个`list`/`tuple`/`string`
   
   `[:]`
   
4. 判断一个对象是否是可迭代对象，使用`collection`模块的`Iterable`
   
   ```python
      from collection import Iterable
      isinstance("abc", Iterable)
   ```
