# menggunakan rumus barisan aritmatika
def bintang(n):
    for i in range(n + 1):
        a = 1
        b = 2
        bintang = (a +(i - 1)* b) * '*'
        print(bintang.center(20))

bintang(4)
