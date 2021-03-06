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
5. 将`list`变成索引-元素对，可以使用python内置的`enumerate`
   
   `enumerate([1,2,3,4])`
   
6. 凡是可以用`for`循环的对象都是`Iterable`类型
   
   `isinstance([],Iterable)`
   
   凡是可作用域`next()`函数的对象都是`Iterator`
   
   `isinstance({},Iterator)`
   
   可以使用`iter()`将函数`iterable`变为`iterable`

7. `assert n!=0, 'n is zero'`
   
   `assert`

8. 用正则表达式分割字符串

   `re.split(r'[\s\,\;]+', 'a,b;; c  d')` \\['a', 'b', 'c', 'd']

9. OrderDict 实现一个FIFO的dict
   ```
   from collections import OrderedDict

   class LastUpdatedOrderedDict(OrderedDict):
      """docstring for LastUpdatedOrderedDict"""
      def __init__(self, capacity):
         super(LastUpdatedOrderedDict, self).__init__()
         self._capacity = capacity

      def __setitem__(self, key, value):
         containKey = 1 if key in self else 0
         if len(self) - containKey >= self._capacity:
            last = self.popitem(last = False)
            print('remove:', last)
         if containKey:
            del  self[key]
            print('set:', (key, value))
         else:
            print('add:',(key, value))
         OrderedDict.__setitem__(self, key, value)

   ```