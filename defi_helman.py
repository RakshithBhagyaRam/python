while True:
  q=int(input("q= "))
  for i in range (1,q):
    for j in range (1,q):
      print(i**j%q,end=" ")
    print("\n")
      
