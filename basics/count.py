import string
consonant =0
vowel =0
for letter in string.ascii_lowercase:
  print(letter, end=" ")
  if letter in ('a','e','i','o','u'):
    vowel +=1
  else :
    consonant +=1
print(f'{vowel} vowels and {consonant} consonants' )
