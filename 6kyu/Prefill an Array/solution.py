def prefill(n,v=None):
    
    
        
    if str(n).isdigit():
        if int(n)==0 :
            return []
        return [v]*int(n) 
    else:
        return str(n)+' is invalid'
