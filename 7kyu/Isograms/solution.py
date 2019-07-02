def is_isogram(string):
    #your code here
    for i in string.lower():
        if string.lower().count(i)>1:
            return False
        
    return True
