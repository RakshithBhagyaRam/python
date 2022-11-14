while True:
	str=input('Enter something :  ')
	if str.isdecimal()  :
		print ('its a number(s)')
	elif str.isalpha():
		print ("it's an alphabet(s)")
	elif str.isalnum():
		print ("it's alphabet(s) and numbers(s)")
	elif str.istitle():
		print ("it's alphabet with first letter cap")
	else :
		if str=='':
			break
		else:
			print ("it's a special character")
