try:    
    while True:
        q = int(input("Enter a prime Number = "))
        l = []
        l1 = []
        n = 1
        for i in range(1, q):
            for z in range(1, q):
                l1.append(z)
            for j in range(1, q):
                s = i**j % q
                l.append(s)
            l.sort()
            # print(l,end='\n')
            if l == l1:
                print(f"alpha = {i}")
                break
            l = []
            l1 = []
        print("\n")
except Exception:
    exit()
