'''age = int(input("Enter your age :- "))
if (age>=18):
	print("you can Vote \n Thank you")
else:
		print("You can not vote \n Bye Bye")'''
		
n=11
ascii=65
for i in range (n):
     print((n-i-1)*" ", end="")
     for j in range (0,i+1):
     	print(chr(ascii),end=" ")
     	ascii+=1
     print()
print(ascii)