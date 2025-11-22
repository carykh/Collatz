f = open("27.txt","w+")

val = 27
while val != 1:
    f.write(str(val)+"\n")
    if val%2 == 0:
        val = int(val/2)
    else:
        val = int(val*3+1)
f.write(str(val)+"\n")
f.flush()
f.close()