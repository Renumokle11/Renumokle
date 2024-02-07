def createList(r1, r2):
    if (r1 == r2):
        return r1

    else:
        res = []

    while(r1 < r2+1 ):
	
        res.append(r1)
        r1 += 1
        return res