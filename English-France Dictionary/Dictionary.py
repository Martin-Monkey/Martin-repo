#Anglicko-Francouzký slovník


dictionary = {}

while True:
    print("\n--- Anglicko/Francouzky Slovník ---")
    print("1. Přidat slovo")
    print("2. Vyhledat slovo")
    print("3. Smazat slovo")
    print("4. Opravit překlad")
    print("5. Zobrazit celý slovník")
    print("6. Konec")

    inp_choose = input("Vyberte možnost: " )

    if inp_choose == "1":
        english_word = input("Zadej anglické slovo: ")
        french_trans = input("Zadej francouzký překlad: ")
        dictionary[english_word] = french_trans
        print(f"Slovo '{english_word}' bylo přidáno.")

    elif inp_choose == "2":
        english_word = input("Zadej slovo na vyhledání: ")
        print(f"Překlad slova '{english_word}': {dictionary.get(english_word, 'Slovo nenalezeno.')}")

    elif inp_choose == "3":
        english_word = input("Zadej slovo, které chceš smazat: ")
        if english_word in dictionary:
            del dictionary[english_word]
            print(f"Slovo '{english_word}' bylo smazáno.")

        else:
            print(f"Slovo '{english_word}' nebylo nalezeno.")

    elif inp_choose == "4":
        english_word = input("Zadej slovo na opravu překladu: ")
        if english_word in dictionary:
            new_trans = input("Zadej nový francouzký překlad: ")
            dictionary[english_word] = new_trans
            print(f"Překlad slova '{english_word}' byl nahrazen.")
        else:
            print(f"Slovo '{english_word}' nebylo nalezeno.")

    elif inp_choose == "5":
        if dictionary:
            for english_word, french_trans in dictionary.items():
                print(f"{english_word} -> {french_trans}")

        else:
            print("Slovník je prázdný.")

    elif inp_choose == "6":
        print("Konec programu")
        break

    else:
        print("Neplatná volba.")
