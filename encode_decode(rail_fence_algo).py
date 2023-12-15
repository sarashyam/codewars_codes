##------------------------ encoding ----------------
def encodestring(text, key):
    #I took the reference from geeks for geeks
    # # This code is contributed  
    # # by Pratik Somwanshi --

    rail = [['\n' for i in range(len(text))]
                    for j in range(key)]
    print(rail)
    dir_down = False
    row,col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == (key -1)):
            dir_down = not dir_down

        rail[row][col] = text[i]
        
        col += 1
        
        if dir_down :
            row += 1
        else :
            row -= 1
    result = []
    for k in range(key):
        for t in range(len(text)):
            if rail[k][t] != "\n":
                result.append(rail[k][t])
    s = "".join(result)
    print(s)

# #--------------------------------------------------------

#--------------------decoding --------------------------------
def decodestring(stri,n):



    rail = [["\n" for i in range(len(stri))] for j in range(n)]
    dir_down = None
    row , col = 0 ,0

    for i in range(len(stri)):
        if row == 0:
            dir_down = True
        if row == (n -1):
            dir_down = False
        
        rail[row][col] = "*"
        col +=1
        
        if dir_down:
            row +=1
        else:
            row -=1

    index = 0
    for s in range(n):
        for j in range(len(stri)):
            if (rail[s][j] == "*") and ( index<len(stri) ):
                    rail[s][j] = stri[index]
                    index +=1

    res = []
    row , col = 0,0
    for i in range(len(stri)):
        if row==0:
            dir_down = True
        if row == (n-1):
            dir_down = False
        if (rail[row][col] != "*"):
            res.append(rail[row][col])
            col +=1
        if dir_down :
            row += 1
        else:
            row -=1
    cip = "".join(res)
    print(cip)
         

#---------------------------------------------------------------
encodestring("adskjfhajfhasjdf",5)
decodestring("akjdfhaofidfifjaf",3)