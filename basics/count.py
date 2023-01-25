import string 
consonant =0
vowel =0
for letter in string.ascii_lowercase:      #it consider on the lowercase characters 
  print(letter, end=" ")     #print every alphabet
  if letter in ('a','e','i','o','u'):     #check whether the perticular alphabet in this tuple
    vowel +=1      #if yes vowels increase by 1 count
  else : 
    consonant +=1      #else consonants increase by 1 count
print(f'{vowel} vowels and {consonant} consonants' )
