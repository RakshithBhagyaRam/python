n=11
ascii=65
for i in range (n):
     print((n-i-1)*" ", end="")
     for j in range (0,i+1):
     	print(chr(ascii),end=" ")
     	ascii+=1
     print()
print("\n",ascii)
