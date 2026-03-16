import json
import os

DB_FILE = 'jugadores_db.json'

def cargar_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def guardar_jugador(nombre, srvw, trnw):
    db = cargar_db()
    db[nombre] = {'SrvW': srvw, 'TrnW': trnw}
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)
    print(f"💾 Datos de {nombre} guardados en la base de datos.")

def obtener_stats(nombre):
    db = cargar_db()
    if nombre in db:
        print(f"🧠 Usando memoria para: {nombre}")
        return db[nombre]
    return None
