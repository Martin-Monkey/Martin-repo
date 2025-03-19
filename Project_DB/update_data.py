import psycopg2
from contextlib import closing
from config import db_params

jmeno = "Bam"
prijmeni = "Margera"
vek = 25
telefon = "724445445"  # Bezpečná hodnota pro telefon
novy_vek = 99

try:
    # Použití WITH pro automatické uzavření spojení
    with closing(psycopg2.connect(**db_params)) as conn:

        with conn.cursor() as cur:
            try:
                # Aktualizace věku studenta
                sql_update = "UPDATE student SET vek = %s WHERE jmeno = %s AND prijmeni = %s;"
                values_update = (novy_vek, jmeno, prijmeni)  # Opraveno "prijemni" na "prijmeni"
                cur.execute(sql_update, values_update)
                conn.commit()

                print(f"✅ Věk studenta {jmeno} {prijmeni} byl aktualizován na {novy_vek}.")

            except psycopg2.Error as e:
                print(f"❌ Chyba v SQL příkazu: {e}")
                conn.rollback()  # Vrátí databázové změny

except psycopg2.Error as e:
    print(f"❌ Chyba při připojení k DB: {e}")

# Po skončení bloku WITH je spojení automaticky uzavřeno
print("✅ Spojení bylo automaticky uzavřeno.")
