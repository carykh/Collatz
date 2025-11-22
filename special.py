special = [123, 171, 187, 259, 347]
special = [187, 347]

for s in special:
    stri = ""
    cursor = s
    itera = 0
    ups = 0
    
    while cursor != s or itera == 0:
        stri += str(cursor)+" -> "
        if cursor%2 == 0:
            cursor = cursor//2
        else:
            cursor = cursor*3+5
            ups += 1
        itera += 1
    stri += str(cursor)+" ("+str(itera)+" steps, "+str(ups)+" ups)"
        
        
    print(stri)
    print("")