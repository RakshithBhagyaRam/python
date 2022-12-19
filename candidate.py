import csv
import numpy as np
with open('candidate.csv','r') as f:
    reads=csv.reader(f)
    tmp_lst=np.array(list(reads))
concept=np.array(tmp_lst[:,:-1])
target=np.array(tmp_lst[:,-1])
for i in range(len(target)):
    if(target[i]=='yes'):
        specific_h=concept[i]
        break
h=[]
generic_h=[['?' for i in range (len(specific_h))]for i in range (len(specific_h))]
print(type(generic_h))

for i in range(len(target)):
    if(target[i]=='yes'):
        for j in range (len(specific_h)):
            if(specific_h[j]!=concept[i][j]):
                specific_h[j]='?'
                generic_h[j][j]='?'
    else:
        for j in range(len(specific_h)):
            if(specific_h[j]!=concept[i][j]):
                generic_h[j][j]=specific_h[j]
            else:
                generic_h[j][j]='?'
    print("Step ",i+1)
    print("The most generic is : ",generic_h)
    print("The most specific is : ",specific_h)
