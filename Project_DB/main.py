import psycopg2
from psycopg2 import extensions

db_params = {
    'dbname': 'martinsestak',
    'user': 'koyeb-adm',
    'password': 'XQc0HOTwa1Kl',
    'host':  'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}


try:
    # 1. Připojení k databázi
    conn = psycopg2.connect(**db_params)
    print("✅ Připojení k databázi bylo úspěšné.")

    # 2. Ověření připojení
    if conn.closed == 0:
        print("✅ Připojení je aktivní.")
    else:
        print("❌ Připojení je uzavřené.")

    if conn.status == extensions.STATUS_READY:
        print("✅ Připojení je připravené k použití.")
    else:
        print("⚠️ Připojení není ve stavu 'READY'.")

except psycopg2.Error as e:
    print(f"❌ Chyba při připojení k DB: {e}")

finally:
    # 3. Uzavření spojení, pokud bylo otevřeno
    if conn:
        conn.close()
        print("✅ Spojení bylo uzavřeno.")
