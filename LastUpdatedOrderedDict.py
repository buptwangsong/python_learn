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


d = LastUpdatedOrderedDict(3)
d['a']=1
d['b']=2
d['c']=3
d['b']=5
print()