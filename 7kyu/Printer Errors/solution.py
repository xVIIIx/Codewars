def printer_error(s):
    # your code
    count=0
    char = 'nopqrstuvwxyz'
    for i in s:
        if i in char:
            count=count+1
            
    return str(count)+'/'+str(len(s))
