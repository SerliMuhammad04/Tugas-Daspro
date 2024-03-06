hari_kerja = int(input("Masukan Jumlah Hari Kerja Karyawan : "))
hari_kerja_perbulan = int(input("Masukan Jumlah Hari Kerja Karyawan Dalam 1 Bulan : "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

gaji_pokok = 5000000
tarif_lembur_perjam = 100000


total_gaji_pokok = (hari_kerja / hari_kerja_perbulan)*gaji_pokok
total_gaji_lembur = jam_lembur * tarif_lembur_perjam

total_gaji = total_gaji_pokok + total_gaji_lembur
total_gaji = int(total_gaji)


def format_rupiah(angka):
    return "Rp. {:,}".format(angka).replace(',', '.')

print(hari_kerja, "Hari Bekerja")
print(jam_lembur, "jam")
print(hari_kerja_perbulan, " Hari Total Bekerja Selama 1 Bulan \n")
print("Total Gaji Karyawan selama 1 bulan : ", format_rupiah(total_gaji))
