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


