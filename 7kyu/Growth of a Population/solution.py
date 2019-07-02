def nb_year(p0, percent, aug, p):
    # your code
    x=0
    while p0 < p:
        print(p0,)
        
        p0 = p0*(1+percent/100) + aug
        print(p0,p)
        x=x+1
    print(x)
    
    return x
