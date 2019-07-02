def maxSequence(arr):
	# ... 
    if len(arr) == 0:
        return 0
    max_ending = max_current = arr[0]
    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)

    return 0 if max_current < 0 else max_current
