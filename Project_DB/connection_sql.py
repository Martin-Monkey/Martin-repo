import psycopg2
from contextlib import closing
from config import db_params

jmeno = 'Bam'
prijmeni = 'Margera'
vek = 25
telefon = '123456789'

try:
    # Použití WITH pro automatické uzavření spojení
    with closing(psycopg2.connect(**db_params)) as conn:
        # print("✅ Připojení k databázi bylo úspěšné.")

        # Vytvoření tabulky student
        with conn.cursor() as cur:
            try:
                # Použití parametrizovaného dotazu správně (bez f-stringu)
                sql = "INSERT INTO Student (jmeno, prijmeni, vek, telefon) VALUES (%s, %s, %s, %s);"
                values = (jmeno, prijmeni, vek, telefon)

                print("SQL dotaz:", sql)
                print("Hodnoty:", values)

                # Parametry se předávají jako tuple, což je bezpečné proti SQL injekci
                cur.execute(sql, values)
                conn.commit()
                print("✅ Data byla vložena.")

            except psycopg2.errors.DuplicateTable:
                print("⚠️ Tabulka 'Student' už existuje, pokračuji dál.")
                conn.rollback()  # Vrátí změny, pokud příkaz selže

            except psycopg2.Error as e:
                print(f"❌ Chyba v SQL příkazu: {e}")
                conn.rollback()  # Vrátí databázové změny

except psycopg2.Error as e:
    print(f"❌ Chyba při připojení k DB: {e}")

# Po skončení bloku WITH je spojení automaticky uzavřeno
print("✅ Spojení bylo automaticky uzavřeno.")
