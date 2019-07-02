def openOrSenior(data):
    # Hmmm.. Where to start?
    thislist = []
    for i in range(len(data)):
        
        if(data[i][0] >= 55 and  data[i][1] > 7):
            thislist.append('Senior')
        else:
            thislist.append('Open')
        
        
        
    return thislist
