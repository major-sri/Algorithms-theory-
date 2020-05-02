a=['a','b','a','c','d','d','c','b','e','f','e','g','h','h','g','f']

n=2
dit={}
cnt=0
arr=[]
for x in a:
    if x in dit.keys():
        if dit[x]==0:
            dit[x]=1
            n+=1
            if len(arr)!=0:
                dit[arr[0]]=0
                arr.remove(arr[0])

        elif dit[x]==-1:
            cnt+=1
            arr.remove(x)
    else:
        if n<=0:
            dit[x]=-1
            arr.append(x)
        else:
            dit[x]=0
            n-=1
print(cnt)


//output-> 2
