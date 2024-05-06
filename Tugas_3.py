def pokok(jam_kerja):

    if jam_kerja <= 7:
        gaji_pokok = jam_kerja * 20000
    else:
        gaji_pokok = 7 * 20000 + (jam_kerja - 7) * 30000
    return gaji_pokok

def lembur(jam_kerja):

    if jam_kerja <= 7:
        gaji_lembur = 0
    else:
        gaji_lembur = (jam_kerja - 7) * 30000
    return gaji_lembur

def makan(jam_kerja):

    if jam_kerja >= 8:
        uang_makan = 5000
    else:
        uang_makan = 0
    return uang_makan

def jasa(jam_kerja):
    if jam_kerja >= 9:
        uang_jasa = 4000
    else:
        uang_jasa = 0
    return uang_jasa

def main():

    nip = input("| Masukkan NIP karyawan: ")
    nama = input("| Masukkan nama karyawan: ")
    jam_kerja = int(input("| Masukkan jumlah jam kerja: "))
    
    print("Laporan Gaji Karyawan")
    print("PT. XYZ")
    print("Bulan : April 2021")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("| NIP             | Nama            | Gaji Pokok         | Lembur             | Uang Makan         | Transport Lembur  |")
    print("------------------------------------------------------------------------------------------------------------------------")


    gaji_pokok_karyawan = pokok(jam_kerja)
    gaji_lembur_karyawan = lembur(jam_kerja)
    uang_makan_karyawan = makan(jam_kerja)
    uang_jasa_karyawan = jasa(jam_kerja)
    total_gaji_karyawan = gaji_pokok_karyawan + gaji_lembur_karyawan + uang_makan_karyawan + uang_jasa_karyawan

    print("| {:<16}| {:<16}| Rp {:<16,.2f}| Rp {:<16,.2f}| Rp {:<16,.2f}|Rp {:<16,.2f}|".format(nip, nama, gaji_pokok_karyawan, gaji_lembur_karyawan, uang_makan_karyawan, uang_jasa_karyawan))
    print("------------------------------------------------------------------------------------------------------------------------")
    print("| Jam Kerja       | {:<16}                                                                                   |".format(jam_kerja))
    print("------------------------------------------------------------------------------------------------------------------------")
    print("| Total Gaji      | Rp {:<16,.2f}                                                                                |".format(total_gaji_karyawan))
    print("------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
