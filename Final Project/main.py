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
            print("Zadej Z pro návrat do hlavního menu kdykoli.")
            first_name = input("Zadej jméno: ")
            if first_name.upper() == "Z":
                continue
            last_name = input("Zadej příjmení: ")
            if last_name.upper() == "Z":
                continue
            phone = input("Zadej telefonní číslo: ")
            if phone.upper() == "Z":
                continue
            address = input("Zadej adresu (Enter pro přeskočení): ")
            if address.upper() == "Z":
                continue
            birth_date = input("Zadej datum narození (Enter pro přeskočení): ")
            if birth_date.upper() == "Z":
                continue
            passport_number = input("Zadej číslo cestovního dokladu (Enter pro přeskočení): ")
            if passport_number.upper() == "Z":
                continue
            nationality = input("Zadej národnost (Enter pro přeskočení): ")
            if nationality.upper() == "Z":
                continue
            add_contact(first_name, last_name, phone, address or None, birth_date or None, passport_number or None,
                        nationality or None)

        elif choice == "2":
            full_name = input("Zadej celé jméno pro smazání (nebo Z pro návrat): ")
            if full_name.upper() == "Z":
                continue
            delete_contact(full_name)

        elif choice == "3":
            full_name = input("Zadej celé jméno pro vyhledání (nebo Z pro návrat): ")
            if full_name.upper() == "Z":
                continue
            print(search_contact(full_name))

        elif choice == "4":
            full_name = input("Zadej celé jméno kontaktu k úpravě (nebo Z pro návrat): ")
            if full_name.upper() == "Z":
                continue
            new_phone = input("Zadej nové telefonní číslo (nebo Z pro návrat): ")
            if new_phone.upper() == "Z":
                continue
            update_contact(full_name, new_phone)

        elif choice == "5":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()
