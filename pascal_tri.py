num_rows = 1
lis= []
if num_rows == 1:
    lis = [[1]]
    print(lis)
elif num_rows == 2:
    lis.append([1])
    lis.append([1,1])
    print(lis)
    
if num_rows > 2:
    lis= [[1],[1,1]]
    for _ in range(num_rows - 2):
        lis.append([])
    rang_lis = len(lis) -1
    for i in range(1,rang_lis):
        j= 0
        lis[i+1].append(lis[i][0])
        while (j<=i):
            if j == i:
                lis[i+1].append(lis[i][j]) 
                break
            print(lis[i+1])
            lis[i+1].append(lis[i][j] + lis[i][j+1])
            j+=1
    print(lis[i+1])       
            
            
        
    
    
print(lis)
