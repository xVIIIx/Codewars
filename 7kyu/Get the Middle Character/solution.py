def get_middle(s):
    #your code here
    if len(s)==1 or len(s)==2: return s
    elif len(s)%2: return s[len(s)/2]
    else: return s[len(s)/2-1:len(s)/2+1]
