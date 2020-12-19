print("=" * 60)
print("NIM".center(10), "NAMA".center(15),  "N.MID".center(20),"N.UAS".center(20))
print("-" * 60)

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

for j in  nilai :
    print (j["nim"].center(10), j["nama"].center(15), str(j["mid"]).center(20),str(j["uas"]).center(20))
print("-" * 60)
