import os


admin_password = "admin"

users = {
    "user1": {
        "name": "Maja",
        "surname": "Majic",
        "password": "1234567890",
    },
    "user2": {
        "name": "Ivo",
        "surname": "Ivic",
        "password": "0123456789",
    },
}

def choose_action(min_value, max_value):
    """
    Funkcija koja omogućava administratoru da odabere akciju između min_value i max_value.
    """
    while True:
        try:
            action = int(input(f"Odaberite akciju ({min_value} - {max_value}): "))
            if action < min_value or action > max_value:
                print(f"Upozorenje: Odabir mora biti između {min_value} i {max_value}.")
            else:
                return action
        except ValueError:
            print("Upozorenje: Odabir mora biti cijeli broj.")






def try_login(target_password):
    login_success = False

    for _ in range(3):
        password = input("Lozinka: ")

        if password == target_password:
            login_success = True
            break

    return login_success


def press_enter(message):
    print(f"\n{message}\n"
          "  Pritisnite <Enter> za nastavak...")

    input()


def admin_screen():
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Pozdrav admin!\n")

    print("Molim odaberite akciju:\n\n"
          "  (1) Prikaz svih korisnika\n"
          "  (2) Dodaj novog korisnika\n"
          "  (3) Ukloni postojeceg korisnika\n"
          "  (4) Promjena lozinke\n"
          "\n  (0) Odjava\n")

    choice = choose_action(0,4)

    if choice == '0':
        logout_admin()
        login_screen()

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        change_password_screen()
    else:
        login_screen()

def remove_user(username):
    if username in users:
        del users[username]
        print(f"Korisnik {username} uspješno izbrisan!")
    else:
        print(f"Korisnik {username} ne postoji!")


def change_password_screen(username):
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    old_pass = input("Unesite trenutnu lozinku: ")
    new_pass = input("Unesite novu lozinku: ")
    new_pass_repeat = input("Ponovite novu lozinku: ")

    if old_pass != users[username]["password"]:
        print("Neispravna trenutna lozinka!")
        user_screen(username)
    elif new_pass != new_pass_repeat:
        print("Unesene nove lozinke se ne podudaraju!")
        user_screen(username)
    elif len(new_pass) < 10:
        print("Lozinka mora imati najmanje 10 znakova!")
        user_screen(username)
    else:
        users[username]["password"] = new_pass
        print("Lozinka uspješno promijenjena!")
        press_enter()
        user_screen(username)


    global admin_password 


    #problem jer je admin passwor na globalnoj razini, ali kada smo ga promjenili na lokalnoj razini u ovoj funkciji, lokalna funkcija nije više vidjela koji je admin pass na globalnoj razini. ovime se dohvaća nazad. nisam stigao cijeli kod pretipkati tako da treba vidjeti rješenje od 4.10.2023. iz seminar_2 foldera (predavanje 10-04)


    if old_pass!= admin_password:
        message("Neispravna trenutna lozinka!: " )
        admin_screen()
    elif new_pass!= new_pass_repeat:
        message("Unesene nove lozinke se ne podudaraju!: " )
        admin_screen()
    elif new_pass < 10:
        message("Lozinka mora imati najmanje 10 znakova!: " )
        admin_screen()
    else:
        admin_password = new_pass
        message("Lozinka uspješno promijenjena!" )


    print(old_pass, new_pass, new_pass_repeat)

    name = users[username]["name"]
    surname = users[username]["surname"]

    print(f"Pozdrav {name} {surname}!\n")

    print("Molim odaberite akciju:\n\n"
          "  (1) Promjena lozinke\n"
          "\n  (0) Odjava\n")
    
    ###########   G R E Š K A   ############

    choice = input("Odaberite akciju: ")

    if choice == '1':
        new_password = input("Unesite novu lozinku: ")
        users[username]["password"] = new_password
        print("Lozinka uspješno promijenjena!")
        press_enter()
        user_screen(username)

    elif choice == '0':
        login_screen()

    else:
        print("Pogrešan odabir. Molim pokušajte ponovno.")
        press_enter()
        change_password_screen(username)


def user_screen(username):
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    name = users[username]["name"]
    surname = users[username]["surname"]

    print(f"Pozdrav {name} {surname}!\n")

    print("Molim odaberite akciju:\n\n"
          "  (1) Promjena lozinke\n"
          "\n  (0) Odjava\n")
    
    choice = input("Odaberite akciju: ")

    if choice == '0':
        logout_user()
        login_screen()


def login_admin():
    """
    Ekran koji omogucava log-in administratora.
    To se postize tako da se tri puta pita unos
    lozinke administratora.

    Ako lozinka bude dobro unesena u ta tri pokusaja,
    otvara se `admin_screen`, a inace se korisnik
    vraca na `login_screen`.
    """
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Prijava administratora...\n")

    login_success = try_login(admin_password)

    if login_success:
        admin_screen()
    else:
        press_enter("Neuspjesna prijava administratora!")

        login_screen()


def logout_admin():
    """
    Ekran koji omogucava odjavu administratora.
    """
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Odjava administratora...\n")

    # Implementacija funkcije za odjavu korisnika



def login_user():
    """
    Ekran koji omogucava log-in korisnika.
    To se postize tako da se trazi unos korisnickog
    imena dokle god to korisnicko ime ne postoji
    ili dok se ne unese nis znakova "STOP".
    Ako se unese "STOP", program prikazuje `login_screen`.

    Nakon toga, trazi se unos lozinke. Unos lozinke trazi
    se 3 puta, kao i kod ekrana za prijavu administratora.

    Ako lozinka bude dobro unesena u ta tri pokusaja,
    otvara se `user_screen`, a inace se korisnik
    vraca na `login_screen`.
    """
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Prijava korisnika...\n")

    username = input("Korisnicko ime (STOP za prekid): ")
    while username != "STOP" and username not in users:
        username = input(
            f"Korisnik {username} ne postoji! Molim unesite ponovno.\n"
            "Korisnicko ime (STOP za prekid): "
        )

    if username == "STOP":
        press_enter("Povratak na ekran za prijavu!")

        login_screen()
        return

    login_success = try_login(users[username]['password'])

    if login_success:
        user_screen(username)
    else:
        press_enter("Neuspjesna prijava korisnika!")

        login_screen()


def logout_user():
    """
    Ekran koji omogucava odjavu korisnika.
    """
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Odjava korisnika...\n")

    # Implementacija funkcije za odjavu korisnika



def login_screen():
    # ocisti ekran prije prikaza novog ekrana
    os.system("cls" if os.name == "nt" else "clear")

    print('*'*30)
    print("Identity Manager\n")

    print("Molim odaberite akciju:\n\n"
          "  (1) Prijava administratora\n"
          "  (2) Promjena lozinke\n"
          "  (3) Prijava korisnika\n"
          "\n  (0) Izlaz\n")

    choice = int(input("Akcija: "))
    while choice < 0 or choice > 3:
        choice = int(input("Molim odaberite samo broj ispred zeljene akcije!\n"
                           "Akcija: "))

    if choice == 1:
        login_admin()
    elif choice == 2:
        username = input("Unesite korisničko ime: ")
        change_password_screen(username)
    elif choice == 3:
        login_user()



login_screen()
