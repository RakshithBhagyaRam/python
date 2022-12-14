import string
c=0
v=0
for letter in string.ascii_lowercase:
  print(letter)
  if i == 'a'or'e'or'i'or'o'or'u':
    v+=1
  else :
    c+=1
print(f'{vowel} vowels and {cons} consonants' )
