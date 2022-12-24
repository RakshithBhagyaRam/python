n=11
ascii=65      #ascii value for A
for i in range (n):
     print((n-i-1)*" ", end="")  #creates a triangular shape
     for j in range (0,i+1):
     	print(chr(ascii),end=" ")
     	ascii+=1
     print()
print("\n",ascii)
