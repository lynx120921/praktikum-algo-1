import random


welcome_message = "Welcome To My Monster Game!"
print("************************************")
print(f"*** {welcome_message} ***")
print("************************************")

nama_user = input("Masukkan Nama Anda: ")
print(f"Halo {nama_user}, Selamat Datang di Game Kami!")


lives = 3
level = 1
max_level = 5

def generate_board(level):
    num_boxes = level + 1
    print("\nCoba perhatikan Goa dibawah ini!")
    board = ""
    for i in range(1, num_boxes + 1):
        board += f"|_{i}_| "
    print(board)

while level <= max_level:
    print(f"\n=== Level {level} ===")
    generate_board(level)

    enemy_position = str(random.randint(1, level + 1))

    pilihan_user = input(f"Pada Nomor Berapa Monster Berada? [1-{level + 1}] ")
    
    if pilihan_user == enemy_position:
        print("Selamat Kamu Benar!")
        if level == max_level:
            print("\n=== SELAMAT! KAMU TELAH MENYELESAIKAN SEMUA LEVEL! ===")
            break
        else:
            level += 1
            print(f"=== Kamu Naik ke Level {level}! ===")
    else:
        lives -= 1
        print(f"Salah!, Monster berada di nomor {enemy_position}")
        print(f"Kamu memiliki {lives} kesempatan lagi.")

        if lives == 0:
            print("\n=== Game Over! ===")
            retry_choice = input("Ingin mencoba lagi? (1: Ulang dari awal, 2: Ulang dari level sebelumnya): ")
            if retry_choice == '1':
                level = 1
                lives = 3
                print("\nKamu memulai dari awal.")
            elif retry_choice == '2' and level > 1:
                level -= 1
                lives = 3
                print(f"\nKamu mengulang dari level {level}.")
            else:
                print("\nTidak valid. Permainan akan dimulai dari level awal.")
                level = 1
                lives = 3
