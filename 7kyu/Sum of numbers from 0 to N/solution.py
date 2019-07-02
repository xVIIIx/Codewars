def show_sequence(n):
    
    if n==0:
        return '0=0'
        
    return '+'.join(str(i) for i in range(0,n+1))+' = '+str(int((n*(n+1))/2)) if n>0 else str(n)+'<0'
