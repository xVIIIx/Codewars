def meeting(s):
    # your code
    a = s.split(';')
      
    x=[]
  
    for i in a:
           x.append(('('+i[i.index(':')+1:] + ', ' +i[:i.index(':')] + ')').upper())
           
    return ''.join(sorted(x))
