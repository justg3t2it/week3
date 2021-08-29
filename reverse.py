import sys 

def reverseReverse(st):
    if st == "":
        return st 
    
    x = len(st)
    reversed = [0] * x
    

    for i in range(len(st)):
        if (st[i] != "," and st[i] != "."): 
            reversed[i] = st[i]
        else:
            reversed[i] = ""
            
    listStr = ''.join([str(elem) for elem in reversed])
    listStr = listStr[::-1]
    print(listStr)

    for x in range(len(st)):
        if (st[x] == ","):
            listStr = listStr[:x] + "," + listStr[x:] 
        if (st[x] == "."):
            listStr = listStr[:x] + "." + listStr[x:]
 
    return listStr



    

        
    
    
    

        
    





      










    



