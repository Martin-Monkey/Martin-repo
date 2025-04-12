import json
import pickle

CONTACTS_JSON = "contacts.json"
CONTACTS_PICKLE = "contacts.pkl"


def load_contacts_json():
    try:
        with open(CONTACTS_JSON, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts_json(contacts):
    with open(CONTACTS_JSON, "w") as file:
        json.dump(contacts, file, indent=4)


def load_contacts_pickle():
    try:
        with open(CONTACTS_PICKLE, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}


def save_contacts_pickle(contacts):
    with open(CONTACTS_PICKLE, "wb") as file:
        pickle.dump(contacts, file)


def add_contact(first_name, last_name, phone, address=None, birth_date=None, passport_number=None, nationality=None):
    contacts = load_contacts_json()
    full_name = f"{first_name} {last_name}"
    contacts[full_name] = {
        "Telefon": phone,
        "Adresa": address if address else "N/A",
        "Datum narození": birth_date if birth_date else "N/A",
        "Číslo pasu": passport_number if passport_number else "N/A",
        "Národnost": nationality if nationality else "N/A"
    }
    save_contacts_json(contacts)
    save_contacts_pickle(contacts)
    print(f"Kontakt {full_name} byl přidán.")


def delete_contact(full_name):
    contacts = load_contacts_json()
    if full_name in contacts:
        del contacts[full_name]
        save_contacts_json(contacts)
        save_contacts_pickle(contacts)
        print(f"Kontakt {full_name} byl smazán.")
    else:
        print("Kontakt nenalezen.")


def update_contact(full_name, field, new_value):
    contacts = load_contacts_json()
    if full_name in contacts:
        # Upravíme pole na správný formát pomocí capitalize()
        field = field.strip().capitalize()

        # Pokud uživatel chce změnit celé jméno (first_name a last_name)
        if field == "Jméno":
            first_name, last_name = new_value.split()
            new_full_name = f"{first_name} {last_name}"
            if new_full_name != full_name:
                contacts[new_full_name] = contacts.pop(full_name)  # Změna full_name
                full_name = new_full_name
                print(f"Jméno kontaktu bylo změněno na {new_full_name}.")

        # Kontrola, zda zadané pole existuje v kontaktu
        elif field in contacts[full_name]:
            contacts[full_name][field] = new_value
            print(f"Pole {field} bylo aktualizováno na {new_value}.")
        else:
            print(f"Požadované pole {field} nenalezeno.")

        save_contacts_json(contacts)
        save_contacts_pickle(contacts)
        print(f"Kontakt {full_name} byl aktualizován.")
    else:
        print("Kontakt nenalezen.")


def search_contact(search_term):
    contacts = load_contacts_json()
    results = []
    for full_name, info in contacts.items():
        if any(search_term.lower() in str(value).lower() for value in
               info.values()) or search_term.lower() in full_name.lower():
            results.append((full_name, info))
    return results


def display_all_contacts():
    contacts = load_contacts_json()
    print("\nSeznam všech kontaktů:")
    for full_name, info in contacts.items():
        print(f"{full_name}: ", end="")
        for key, value in info.items():
            print(f"{key}: {value}, ", end="")
        print()


def main():
    while True:
        print("\nSprávce kontaktů:")
        print("1. Přidat kontakt")
        print("2. Smazat kontakt")
        print("3. Vyhledat kontakt")
        print("4. Upravit kontakt")
        print("5. Ukončit")

        choice = input("Vyber možnost: ")

        if choice == "1":
            first_name = input("Zadej jméno: ")
            last_name = input("Zadej příjmení: ")
            phone = input("Zadej telefonní číslo: ")
            address = input("Zadej adresu (nepovinné, Enter pro přeskočení): ") or None
            birth_date = input("Zadej datum narození (nepovinné, Enter pro přeskočení): ") or None
            passport_number = input("Zadej číslo cestovního dokladu (nepovinné, Enter pro přeskočení): ") or None
            nationality = input("Zadej národnost (nepovinné, Enter pro přeskočení): ") or None
            add_contact(first_name, last_name, phone, address, birth_date, passport_number, nationality)
        elif choice == "2":
            full_name = input("Zadej celé jméno pro smazání: ")
            delete_contact(full_name)
        elif choice == "3":
            print("\n1. Zadej údaj z kontaktu")
            print("2. Zobraz všechny kontakty")
            search_choice = input("Vyber možnost pro vyhledání: ")

            if search_choice == "1":
                search_term = input("Zadej údaj pro vyhledání: ")
                results = search_contact(search_term)
                if results:
                    for full_name, info in results:
                        print(f"Kontakt nalezen: {full_name}, {info}")
                else:
                    print("Kontakt nenalezen.")
            elif search_choice == "2":
                display_all_contacts()
            else:
                print("Neplatná volba.")
        elif choice == "4":
            search_term = input("Zadej údaj pro vyhledání kontaktu: ")
            results = search_contact(search_term)

            if results:
                print("\nNalezené kontakty:")
                for i, (full_name, info) in enumerate(results, start=1):
                    print(f"{i}. {full_name}: {info}")

                contact_choice = int(input(f"Vyber číslo kontaktu k úpravě (1-{len(results)}): ")) - 1
                if 0 <= contact_choice < len(results):
                    full_name, info = results[contact_choice]
                    print(f"\nVybraný kontakt: {full_name}")
                    print("Možná pole k úpravy: Telefon, Adresa, Datum narození, Číslo pasu, Národnost, Jméno")
                    field = input("Zadej pole, které chceš upravit: ")
                    field = field.strip().capitalize()  # Použití capitalize() pro správný formát
                    if field.lower() in ['telefon', 'adresa', 'datum narození', 'číslo pasu', 'národnost', 'jméno']:
                        new_value = input(f"Zadej novou hodnotu pro {field}: ")
                        update_contact(full_name, field, new_value)
                    else:
                        print("Neplatné pole.")
                else:
                    print("Neplatný výběr.")
            else:
                print("Kontakt nenalezen.")
        elif choice == "5":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()
