# task_master.py
import random, time, queue
from multiprocessing.managers import BaseManager

#create task_sender queue
task_queue = queue.Queue()

#create result_receiver queue
result_queue = queue.Queue()

#
class QueueManager(BaseManager):
	"""docstring for QueueManager"""
	# def __init__(self, arg):
	# 	super(QueueManager, self).__init__()
	# 	self.arg = arg
	pass

#register Queues into network, parameter 'callable' is Queue object
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

#set port=5000, authkey='abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')

#start Queue
manager.start()

#get Queue object from network
task = manager.get_task_queue()
result = manager.get_result_queue()

#put task into task queue
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)

#get result from result queue
print('Try get results...')
for i in range(10):
	r = result.get(timeout = 10)
	print('Result: %s' % r)

#shutdown
manager.shutdown()
print('master exit.')