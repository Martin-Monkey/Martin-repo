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

def add_contact(name, phone):
    contacts = load_contacts_json()
    contacts[name] = phone
    save_contacts_json(contacts)
    save_contacts_pickle(contacts)
    print(f"Kontakt {name} byl přidán.")

def delete_contact(name):
    contacts = load_contacts_json()
    if name in contacts:
        del contacts[name]
        save_contacts_json(contacts)
        save_contacts_pickle(contacts)
        print(f"Kontakt {name} byl smazán.")
    else:
        print("Kontakt nenalezen.")

def update_contact(name, new_phone):
    contacts = load_contacts_json()
    if name in contacts:
        contacts[name] = new_phone
        save_contacts_json(contacts)
        save_contacts_pickle(contacts)
        print(f"Kontakt {name} byl aktualizován.")
    else:
        print("Kontakt nenalezen.")

def search_contact(name):
    contacts = load_contacts_json()
    return contacts.get(name, "Kontakt nenalezen.")


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
            name = input("Zadej jméno: ")
            phone = input("Zadej telefonní číslo: ")
            add_contact(name, phone)
        elif choice == "2":
            name = input("Zadej jméno pro smazání: ")
            delete_contact(name)
        elif choice == "3":
            name = input("Zadej jméno pro vyhledání: ")
            print(search_contact(name))
        elif choice == "4":
            name = input("Zadej jméno kontaktu k úpravě: ")
            new_phone = input("Zadej nové telefonní číslo: ")
            update_contact(name, new_phone)
        elif choice == "5":
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


if __name__ == "__main__":
    main()

