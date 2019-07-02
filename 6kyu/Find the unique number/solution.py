def find_uniq(arr):
    # your code here
    print(arr[:3])
    print(set(arr))
    x = arr[:3]
    if len(set(arr)) == 1:
        return set(arr)
    for i in x:
        if x.count(i)==1:
            return i 
        else:
            for j in set(arr):
                if j!= i:
                    return j
