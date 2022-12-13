vowel = 0
cons=0

for i in a-z:
  if i == 'a'or'e'or'i'or'o'or'u':
    vowel+=1
  else :
    cons+=1
print(f'{vowel} vowels and {cons} consonants' )
