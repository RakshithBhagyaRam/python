import re
import time
'''
a = '10'
b='20'
c= 10+20
print(f'sum of {a} + {b} = {str(c)}')
''
def eggs(pa):
	pa.append('hello')
	print(l)
	
l=[1,2,3]
eggs(l)
print(l)
x=60
y=80
x,y,z=1,2,3
print(x,y,z)
msg=input('>')
words=msg.split(' ')
emoji={
":)":"😄",
":(":"🥺"
}
out=' '
for word in words:
	out+=emoji.get(word,word) + " "
print(out)


while True:
	str=input('Enter something :  ')
	if str.isdecimal()  :
		print ('its a number(s)')
	elif str.isalpha():
		print ("it's an alphabet(s)")
	elif str.isalnum():
		print ("it's alphabet(s) and numbers(s)")
	elif str.istitle():
		print ("it's alphabet with first letter cap")
	else :
		if str=='':
			break
		else:
			print ("it's a special character")

def unpack(p,q,r,s):
	print(p+s)
a=[2,3,4,5]
unpack(*a)
n=0
a=[""]
n=int(input('enter number of numbers '))
print("enter numbers ")
for i in range(0,n):
	a[i]=input()
#	a[i]+=ai]
print(a[i])
	

x=[1,2,3]
y=[1,2,3]
print(len(x)+len(y))
number_list = []
n = int(input("Enter the list size \n"))
print("enter the values")
for i in range(0, n):
    item=input().split(" ")
    number_list.append(item) the
print(number_list)
list1=['a',1]
list2=list1
list3=list2
list2.append('b')
print(list2,list3)

print(len(list2+list1))
t1=(1,2,3,4)
t2=(4,2,3,1)
print(t2>t1)

phRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
m=phRegex.findall('cell: 415-555-5432 home: 667-715-5555')
print(m)

i=1
while(i<4):
	i+=1
	if i==2:
		continue
	print(i)
'''
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