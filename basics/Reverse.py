# Reversing a number using slicing 


n = int(input("Enter a number:"))
print(str(n)[::-1])


# Reversing a number using loop 

n = int(input("Enter a number:"))
reversed_number =0
while n!=0:
    num = n%10
    reversed_number = reversed_number * 10 + num 
    n=n//10
print(reversed_number, end='')

