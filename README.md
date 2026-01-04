# SSH Bruteforce Testing Tool (CLI)

## Deskripsi
SSH Bruteforce Testing Tool adalah tools berbasis **Python (CLI)** yang digunakan untuk melakukan **uji keamanan brute force SSH** secara **realtime**.  
Tools ini **HANYA untuk self-testing / authorized testing** pada server milik sendiri.

> ⚠️ Segala penyalahgunaan di luar izin pemilik sistem **bukan tanggung jawab developer**.

---

## Fitur
- Realtime SSH brute force testing
- Output berwarna (Merah = Attack / Failed, Hijau = Success)
- ASCII Banner
- Developer tag **@yogagymn**
- Delay antar percobaan (anti flood)
- CLI sederhana & ringan

---

---

## Requirement
- Python 3.x
- Library Paramiko

Install dependency:
```bash
pip install paramiko

## Cara Penggunaan
Masuk ke folder python lalu jalankan perintah berikut:

pip install paramiko
cd ssh_bruteforce/python
python ssh_bruteforce.py 134.199.164.95 2024 ../users.txt ../passwords.txt

## Catatan Keamanan
1. Gunakan hanya pada server milik sendiri
2. Disarankan aktifkan fail2ban
3. Jangan gunakan untuk aktivitas ilegal

Cocok untuk:
1. Penelitian
2. Skripsi
3. Lab keamanan

## Developer
@yogagymn
Cyber Security Research & Pentester
