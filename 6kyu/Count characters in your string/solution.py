def count(string):
    # The function code should be here
    print(string)
    x={}
    for i in string:
        x.update({i:string.count(i)})
        
    
    return x
