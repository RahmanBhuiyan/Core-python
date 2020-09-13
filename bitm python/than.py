def sumValues(a, b, *others):
    retValue = a + b
    # 'others' parameter like an array.
    for other in others :
        retValue = retValue + other
    return retValue