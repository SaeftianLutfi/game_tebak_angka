import random

def proses_tebakan(angka_rahasia, tebakan):
    """
    Fungsi ini memproses hasil tebakan dan mengembalikan status.
    """
    if tebakan.isdigit():
        tebakan = int(tebakan)
        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah.")  # Output dicetak
            return "rendah"
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi.")  # Output dicetak
            return "tinggi"
        else:
            print("Tebakan Anda benar!")  # Output dicetak
            return "benar"
    elif tebakan.lower() == 'exit':
        print("Keluar dari permainan.")  # Output dicetak
        return "exit"
    else:
        print("Input tidak valid.")  # Output dicetak
        return "invalid"

def tebak_angka():
    angka_rahasia = random.randint(1, 10)
    tertebak = False

    print("\nSelamat Datang Di Permainan Tebak Angka")
    print("Silahkan tebak angka dari angka 1 sampai 10!")
    print("Ketik 'exit' untuk keluar dari permainan.\n")

    while not tertebak:
        tebakan = input("Masukkan tebakan anda: ")
        hasil = proses_tebakan(angka_rahasia, tebakan)

        if hasil == "exit":
            print("Terima kasih telah bermain! Sampai jumpa.")
            return
        elif hasil == "rendah":
            print("Tebakan Anda terlalu rendah. Ayo coba lagi!\n")
        elif hasil == "tinggi":
            print("Tebakan Anda terlalu tinggi. Ayo coba lagi!\n")
        elif hasil == "benar":
            print("Selamat! Anda telah menebak angka yang benar:", angka_rahasia)
            tertebak = True
        else:
            print("Silahkan masukkan angka yang valid.\n")

    # Menawarkan untuk bermain lagi setelah selesai
    bermain_lagi = input("Apakah Anda ingin bermain lagi? (ya/tidak): ").lower()
    if bermain_lagi == 'ya':
        tebak_angka()
    else:
        print("Terima kasih telah bermain! Sampai jumpa.")

if __name__ == '__main__':
    tebak_angka()
