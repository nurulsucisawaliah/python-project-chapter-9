#menggunakan looping for
def ubahHuruf(teks,a, b):
    listnya = list(teks)
    j = ""
    for x in listnya:
        if (x == a):
            x = b
        j =''.join([j,x])
    return j

print(ubahHuruf("MATEMATIKA","T","S"))
    
#menggunakan replace
def ubahHuruf(teks,a,b):
    return teks.replace(a,b)

print(ubahHuruf("MATEMATIKA","T","S"))
