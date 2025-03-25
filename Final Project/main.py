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


def update_contact(full_name, new_phone):
    contacts = load_contacts_json()
    if full_name in contacts:
        contacts[full_name]["Telefon"] = new_phone
        save_contacts_json(contacts)
        save_contacts_pickle(contacts)
        print(f"Kontakt {full_name} byl aktualizován.")
    else:
        print("Kontakt nenalezen.")


def search_contact(full_name):
    contacts = load_contacts_json()
    return contacts.get(full_name, "Kontakt nenalezen.")


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
            full_name = input("Zadej celé jméno pro vyhledání: ")
            print(search_contact(full_name))
        elif choice == "4":
            full_name = input("Zadej celé jméno kontaktu k úpravě: ")
            new_phone = input("Zadej nové telefonní číslo: ")
            update_contact(full_name, new_phone)
        elif choice == "5":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()
