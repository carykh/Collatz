LIMIT = 9000

for num in range(27, 28):

    
    cursor = num
    seen = []
    itera = 0
    stri = ""
    max_seen = num

    while cursor not in seen:
        if cursor >= LIMIT:
            stri += "["+str(cursor)+"]"+" -> "
        else:
            stri += str(cursor)+" -> "
        seen.append(cursor)
        max_seen = max(max_seen, cursor)
        if cursor%2 == 0:
            cursor = cursor//2
        else:
            cursor = cursor*3+1
        itera += 1
        
    stri += str(cursor)+" ("+str(itera)+" steps)"

    if max_seen >= LIMIT:
        print(stri)
        print("")
        exit()
        
    #if num%10000 == 0:
    #    print(f"Done with {num}")