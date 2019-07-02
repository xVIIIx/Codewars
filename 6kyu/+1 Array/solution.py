def up_array(arr):
    #your code here
    print(arr)
    if len(arr) < 1:
        return None
    
    for i in arr: 
        if i < 0 or i>9:
            return None
    x = []
    for i in str(int(''.join(str(x) for x in arr))+1):
        x.append(int(i))
        
    return x
