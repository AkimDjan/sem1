l=input().replace('*',' ').split()
s=''
for i in range(0,len(l),2):
    s+=l[i]*int(l[i+1])
print(s)
    

    
