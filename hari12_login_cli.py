import getpass
 
akun = {"alif;": "12345", "admin": "root"}

print("=== sistem login ===")

username = input("masukkan username: ")
password = getpass.getpass("masukkan password: ")

if username in akun and akun[username] == password:
    print(f"selamat datang, {username}!")
else:
    print("username atau password salah!")

