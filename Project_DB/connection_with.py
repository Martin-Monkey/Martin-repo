import psycopg2
from contextlib import closing
from config import db_params

try:
    # Použití WITH pro automatické uzavření spojení
    with closing(psycopg2.connect(**db_params)) as conn:
        # print("✅ Připojení k databázi bylo úspěšné.")

        # Vytvoření tabulky student
        with conn.cursor() as cur:
            try:
                create_table_query = """
                CREATE TABLE IF not exists student  (
                    id SERIAL PRIMARY KEY,
                    jmeno VARCHAR(50) NOT NULL,
                    prijmeni VARCHAR(50) NOT NULL,
                    vek INT CHECK (vek >= 0),
                    telefon VARCHAR(30)
                );
                """
                cur.execute(create_table_query)
                conn.commit()
                print("✅ Tabulka 'student' byla vytvořena.")

            except psycopg2.errors.DuplicateTable:
                print("⚠️ Tabulka 'student' už existuje, pokračuji dál.")
                conn.rollback()  # Vrátí změny, pokud příkaz selže

            except psycopg2.Error as e:
                print(f"❌ Chyba v SQL příkazu: {e}")
                conn.rollback()  # Vrátí databázové změny

except psycopg2.Error as e:
    print(f"❌ Chyba při připojení k DB: {e}")

# Po skončení bloku WITH je spojení automaticky uzavřeno
print("✅ Spojení bylo automaticky uzavřeno.")