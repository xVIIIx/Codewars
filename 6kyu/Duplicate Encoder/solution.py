def duplicate_encode(word):
    #your code here
    #count = 0
    word = word.lower()
    print(word)
    
    if word.count(')') == 1 and word.count('(') == 1:
        word = word.replace(')','(')
    elif word.count('(') > 1 and word.count(')') > 1:
        word = word.replace('(',')')
    elif word.count(')') == 1 and word.count('(') > 1:
        x = word.index(')')
        word = word.replace('(',')')
        word = word[:x]+'('+word[x+1:]
    elif word.count(')') == 1:
        word = word.replace(')','(')
    elif word.count('(') > 1:
        word = word.replace('(',')')
    
        
        
    for i in word :
          if i != '('  :
              
              if word.count(i) == 1:
                  word = word.replace(i,'(')
                  print(word)
              else :
                  word = word.replace(i,')')
                  print(word)

    return word
