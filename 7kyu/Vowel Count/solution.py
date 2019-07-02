def getCount(inputStr):
    num_vowels = 0
    # your code here
    vow = 'aeiou'
    for i in inputStr:
        if i in vow:
            num_vowels=num_vowels+1
    
    return num_vowels
