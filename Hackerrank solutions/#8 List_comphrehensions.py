if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i1 = [_ for _  in range(x+1)]
    j1 = [_ for _  in range(y+1)]
    k1 = [_ for _  in range(z+1)]
    
    l=[]
    for i in i1:
        for j in j1:
            for k in k1:
                if(i+j+k !=n):
                   l.append([i,j,k])
    print(l)