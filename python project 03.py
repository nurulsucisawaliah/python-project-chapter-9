def bintang(n):
    star = int(n/2 + 1)
    for i in range(n + 1):
        a = 1
        b = 2
        bintang = (a +(i - 1)* b) * '*'
        print(bintang.center(20))
        if i== star:
            for i in range(star -1,0,-1):
                bintangnya = (a +(i - 1)* b) * '*'
                print(bintangnya.center(20))
            break

bintang(7)


    
