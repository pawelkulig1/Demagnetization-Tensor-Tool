#!/usr/bin/python3

import threading
import time

exitFlag = 0
#testTab = []



class myThread (threading.Thread):
	def __init__(self, threadID, msg):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.msg = msg
        
	def run(self):
		printer(self.msg)

def printer(txt):
	return txt


thread = []

suma = 0

for i in range(16000):
	thread.append(myThread(i, i))
	thread[i].start()

#print("123")


for i in range(16000):
	print(thread[i].join())


print (sum(testTab))
print (len(testTab))

print ("Exiting Main Thread")
