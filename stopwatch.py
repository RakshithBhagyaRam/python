import re
import time

input('press enter to start stopwatch and space to stop')
try:
	for h in range(24):
		for m in range(60):
			for s in range(60):
				for ms in range(99):
					ms=ms+1
					print (h,':',m,':',s,':',ms)
					time.sleep(0.01)
					
					if s==' ':
						break
except keyboardinterrupt:
	exit(0)
'''
t=int(input('enter the number of seconds'))
while(t>0):
	print(t)
	t-=1
	time.sleep(1)'''
