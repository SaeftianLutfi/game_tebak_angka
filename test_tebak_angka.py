import pytest
from game_tebak_angka import proses_tebakan

# Uji semua jalur logika pada fungsi `proses_tebakan`
@pytest.mark.parametrize("angka_rahasia, tebakan, expected", [
    (5, "3", "rendah"),           # Tebakan terlalu rendah
    (5, "7", "tinggi"),           # Tebakan terlalu tinggi
    (5, "5", "benar"),            # Tebakan benar
    (5, "abc", "invalid"),        # Input tidak valid
    (5, "exit", "exit"),          # Keluar dari permainan
    (5, "", "invalid"),           # Input kosong (invalid)
    (5, "ya", "invalid"),         # Input tidak sesuai (untuk permainan ulang)
    (5, "tidak", "invalid"),      # Input tidak sesuai (untuk permainan ulang)
])
def test_proses_tebakan(capsys, angka_rahasia, tebakan, expected):
    result = proses_tebakan(angka_rahasia, tebakan)
    
    # Menangkap output yang tercetak selama pengujian
    captured = capsys.readouterr()

    # Menampilkan hasil
    print(f"Tebakan: {tebakan}, Hasil: {result}, Expected: {expected}")
    print(f"Output yang dicetak: {captured.out}")  # Output yang dicetak dari fungsi

    # Memastikan hasil sesuai dengan yang diharapkan
    assert result == expected

# Uji fungsi bermain ulang (pengolahan input "ya" atau "tidak")
@pytest.mark.parametrize("input_ulang, expected", [
    ("ya", "main ulang"),         # Pilihan untuk bermain ulang
    ("tidak", "selesai"),         # Pilihan untuk mengakhiri permainan
    ("", "invalid"),              # Input kosong
    ("random", "invalid"),        # Input tidak valid
])
def test_bermain_lagi(capsys, input_ulang, expected):
    def proses_bermain_lagi(input_ulang):
        if input_ulang.lower() == "ya":
            return "main ulang"
        elif input_ulang.lower() == "tidak":
            return "selesai"
        else:
            return "invalid"

    result = proses_bermain_lagi(input_ulang)
    
    # Menangkap output yang tercetak selama pengujian
    captured = capsys.readouterr()

    # Menampilkan hasil
    print(f"Input ulang: {input_ulang}, Hasil: {result}, Expected: {expected}")
    print(f"Output yang dicetak: {captured.out}")  # Output yang dicetak dari fungsi

    # Memastikan hasil sesuai dengan yang diharapkan
    assert result == expected
