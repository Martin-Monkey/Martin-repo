import psycopg2
from contextlib import closing
from config import db_params

jmeno = "Robert"
prijmeni = "Klimek"
vek = 25
# telefon ="724445445"
telefon = "'); DROP TABLE student--"
try:
    # Použití WITH pro automatické uzavření spojení
    with closing(psycopg2.connect(**db_params)) as conn:

        with conn.cursor() as cur:
            try:
                sql = "INSERT INTO student (jmeno, prijmeni, vek, telefon) VALUES (%s, %s, %s, %s);"

                # values = (jmeno, prijmeni, vek, telefon)  # Parametry
                for _ in range(10):
                    jmeno = f'vaclav{_}'
                    prijmeni = f'novak{_}'
                    vek = f'{_}'
                    telefon = f'tel{_}'

                    values = (jmeno, prijmeni, vek, telefon)
                    cur.execute(sql, values)

                conn.commit()

                print("vlozeno.")



            except psycopg2.Error as e:
                print(f"❌ Chyba v SQL příkazu: {e}")
                conn.rollback()  # Vrátí databázové změny

except psycopg2.Error as e:
    print(f"❌ Chyba při připojení k DB: {e}")

# Po skončení bloku WITH je spojení automaticky uzavřeno
print("✅ Spojení bylo automaticky uzavřeno.")

# for _ in range(10):
#     jmeno = f'vaclav{_}'
#     prijmeni = f'novak{_}'
#     vek = f'{_}'
#     telefon = f'tel{_}'

#     cur.execute(sql, values)
#     cur.execute(sql, values)


# telefon = "'); DROP TABLE student--"


# jmeno = "Robert'); DROP TABLE student; --"