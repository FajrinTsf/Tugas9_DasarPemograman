# List of friends
friends = []


def tambah_nama():
    name = input("Masukkan nama teman: ")
    friends.append(name)
    print(f"{name} telah ditambahkan ke daftar teman!")


def hapus_nama():
    name = input("Masukkan nama teman yang ingin dihapus: ")
    if name in friends:
        friends.remove(name)
        print(f"{name} telah dihapus dari daftar teman!")
    else:
        print(f"{name} tidak ditemukan di daftar teman!")


def tampilkan_nama():
    if friends:
        print("Daftar Teman:")
        for i, friend in enumerate(friends, 1):
            print(f"{i}. {friend}")
    else:
        print("Daftar teman masih kosong!")


while True:
    print("\nMenu:")
    print("1. Tambahkan nama")
    print("2. Hapus nama")
    print("3. Tampilkan nama")
    print("4. Exit")
    choice = input("Pilih menu: ")

    if choice == "1":
        tambah_nama()
    elif choice == "2":
        hapus_nama()
    elif choice == "3":
        tampilkan_nama()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Menu tidak valid. Silakan coba lagi!")
