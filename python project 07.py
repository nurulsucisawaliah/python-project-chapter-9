mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
listnya = []

print('=' * 65)
print('NIM'.center(4), 'NAMA MAHASISWA'.center(20), 'TGL LAHIR'.center(20), 'TEMPAT LAHIR'.center(10))
print('-' * 65)


for x in range(len(mhs)) :
    mi = mhs[x].split(':')
    listnya.append(mi)
    ls = listnya[x][2].split('-')
    ls.reverse()
    lsJoined = '/'.join(ls)
    listnya[x][2] = lsJoined

for j in range(len(listnya)) :
    print(listnya[j][0].center(4), listnya[j][1].center(20), listnya[j][2].center(20), listnya[j][3].ljust(10),)
print('-' * 65)
