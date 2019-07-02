def namelist(names):
    #your code here
    if len(names) == 0:
        return ''
    
    print(', '.join(i['name'] for i in names)[:-(len(names[-1]['name'])+2)]+' & '+str(names[-1]['name']))
    """
    print(names[-1]['name'])
    
    x=''
    
    for i in range(len(names)):
        if names[i] == names[-1]:
            x+=names[i]['name']+', '
            
    print(x)
       """ 
    return ', '.join(i['name'] for i in names)[:-(len(names[-1]['name'])+2)]+' & '+str(names[-1]['name']) if len(names) != 1 else str(names[0]['name'])
