def summer69(arr):
    total = 0
    add = True
    for i in arr:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total


print(summer69([1, 3, 5]))
