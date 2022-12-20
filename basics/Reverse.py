# Reversing a number using slicing 


n = int(input("Enter a number:"))
print(str(n)[::-1])               # integer can't do slicing so we convert integer to string by type conversion 


# Reversing a number using loop 

n = int(input("Enter a number:"))
reversed_number =0
while n!=0:
    num = n%10         # performing modulo ooperationto get the remainder of the number 
    reversed_number = reversed_number * 10 + num 
    n=n//10           # performing integer division to get the quotient of the number
print(reversed_number)

