print("Nilai akhir = (mid + 2(uas))/ 3")
print("=" * 80)
print("NIM".center(10), "NAMA".center(15),  "N.MID".center(20),"N.UAS".center(10),"N.AKHIR".center(10),"STATUS".center(5))
print("-" * 80)

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

for j in  nilai :
    nilai_akhir = (j['mid'] + (2 * j['uas'])) / 3
    nilai_akhir = int(nilai_akhir)
    if(nilai_akhir >= 60) :
        status = "LULUS"
    elif(nilai_akhir < 60) :
        status = "TIDAK LULUS"
   
    print (j["nim"].center(10), j["nama"].center(15), str(j["mid"]).center(20),str(j["uas"]).center(10),str(nilai_akhir).center(10),status.center(5))


print("-" * 80)
