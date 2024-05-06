def hitung_gaji_pokok(jumlah_jam):
    gaji_pokok_per_jam = 20000
    return jumlah_jam * gaji_pokok_per_jam

def hitung_gaji_lembur(jumlah_jam):
    if jumlah_jam > 7:
        gaji_pokok_per_jam = 20000
        gaji_lembur_per_jam = gaji_pokok_per_jam * 1.5
        return (jumlah_jam - 7) * gaji_lembur_per_jam
    else:
        return 0

def hitung_uang_makan(jumlah_jam):
    if jumlah_jam >= 8:
        return 5000
    else:
        return 0

def hitung_uang_transport_lembur(jumlah_jam):
    if jumlah_jam >= 9:
        return 4000
    else:
        return 0

def hitung_total_gaji(jumlah_jam):
    gaji_pokok = hitung_gaji_pokok(jumlah_jam)
    gaji_lembur = hitung_gaji_lembur(jumlah_jam)
    uang_makan = hitung_uang_makan(jumlah_jam)
    uang_transport_lembur = hitung_uang_transport_lembur(jumlah_jam)
    total_gaji = gaji_pokok + gaji_lembur + uang_makan + uang_transport_lembur
    return total_gaji

def main():
    print("LAPORAN GAJI KARYAWAN")
    print("PT. XYZ")
    print("Bulan : April 2011\n")
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("NIP", "Nama", "Gaji Pokok", "Lembur", "Uang Makan", "Transport Lembur"))
    print("===================================================================================")

    nip = input("Masukkan NIP: ")
    nama = input("Masukkan nama karyawan: ")
    jumlah_jam_kerja = float(input("Masukkan jumlah jam kerja: "))

    total_gaji = hitung_total_gaji(jumlah_jam_kerja)
    
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(nip, nama, hitung_gaji_pokok(jumlah_jam_kerja), hitung_gaji_lembur(jumlah_jam_kerja), hitung_uang_makan(jumlah_jam_kerja), hitung_uang_transport_lembur(jumlah_jam_kerja)))
    print("\nTotal Gaji:", total_gaji)

if __name__ == "__main__":
    main()

