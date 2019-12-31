i = 0.00

while i < 2:
    for j in [1, 2, 3]:
        j += i
        # print(i + 0.00000000000001) 
        
        i_f = "{:.2}".format(i)
        j_f = "{:.2}".format(j)

        if ".0" in i_f:
            i_f = i_f[0]
        
        if ".0" in j_f:
            j_f = j_f[0]
        
        print("I={} J={}".format(i_f, j_f) )

    i += 0.2


