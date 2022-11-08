while True:
	n=int(input("Enter the number of people : "))
	for i in range(n+1) :
		p = pow(2,i)
		#print(i , "#" , p )
		if n==p:
			print (f"The {1}st person is servived")
			break
		elif p<n :
			s=((n-p)*2)+1
			if(s<=n):
				if(s>=n//2):
					if(s==3):
						print (f"The {s}rd person is servived")
					else:
						print (f"The {s}th person is servived")
					break
		else :
			print ("no value")
			break