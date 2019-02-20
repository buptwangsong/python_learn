#task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	"""docstring for QueueManager"""
	# def __init__(self, arg):
	# 	super(QueueManager, self).__init__()
	# 	self.arg = arg
	pass

#get Queue API from network
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#connect to server
server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)

m = QueueManager(address = (server_addr, 5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

#get task from task queue, and write result into result queue
for i in range(10):
	try:
		n = task.get(timeout = 1)
		print('run task %d * %d...' % (n,n))
		r = '%d * %d' % (n,n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty')

print('worker exit')