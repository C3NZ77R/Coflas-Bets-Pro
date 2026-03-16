import os
import requests
import pandas as pd
from dotenv import load_dotenv

# 1. Configuración inicial
load_dotenv()
API_KEY = os.getenv("910fc4baff822d77b6bfb7cba8b1b68a")
ARCHIVO_EXCEL = "partidos.xlsx"

def obtener_deporte_activo():
    """Busca automáticamente el torneo de tenis que tenga cuotas hoy."""
    print("🔍 Buscando torneos de tenis activos...")
    url_sports = f"https://api.the-odds-api.com/v4/sports/?apiKey={910fc4baff822d77b6bfb7cba8b1b68a}"
    
    try:
        response = requests.get(url_sports)
        sports = response.json()
        
        # Filtramos los que sean de tenis y estén activos
        tenis_activos = [s['key'] for s in sports if "tennis" in s['key'] and s['active']]
        
        if not tenis_activos:
            print("⚠️ No se encontraron torneos de tenis con cuotas activas hoy.")
            return None
        
        # Retornamos el primero (ej: 'tennis_wta_miami_open')
        print(f"🎾 Torneo detectado: {tenis_activos[0]}")
        return tenis_activos[0]
        
    except Exception as e:
        print(f"❌ Error al consultar deportes: {e}")
        return None

def recolectar_cuotas():
    deporte = obtener_deporte_activo()
    if not deporte:
        return

    print(f"📡 Descargando cuotas para {deporte}...")
    url_odds = f"https://api.the-odds-api.com/v4/sports/{deporte}/odds/"
    params = {
        'apiKey': API_KEY,
        'regions': 'us', # 'us' suele ser más estable, puedes probar 'eu'
        'markets': 'h2h',
        'oddsFormat': 'decimal'
    }

    try:
        response = requests.get(url_odds, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ Error {response.status_code}: {data}")
            return

        partidos_list = []
        for event in data:
            home_team = event['home_team']
            away_team = event['away_team']
            
            # Buscamos cuotas en el primer bookmaker disponible
            if event['bookmakers']:
                # Tomamos la primera casa de apuestas (ej: DraftKings, BetRivers, etc.)
                cuotas = event['bookmakers'][0]['markets'][0]['outcomes']
                
                try:
                    price_1 = next(item['price'] for item in cuotas if item['name'] == home_team)
                    price_2 = next(item['price'] for item in cuotas if item['name'] == away_team)
                    
                    partidos_list.append({
                        'Fecha': event['commence_time'],
                        'Torneo': event['sport_title'],
                        'Jugador_1': home_team,
                        'Jugador_2': away_team,
                        'Cuota_1': price_1,
                        'Cuota_2': price_2,
                        'Casa_Apuestas': event['bookmakers'][0]['title']
                    })
                except StopIteration:
                    continue

        # 2. Guardar en Excel
        if partidos_list:
            df = pd.DataFrame(partidos_list)
            df.to_excel(ARCHIVO_EXCEL, index=False)
            print(f"✅ ¡Éxito! {len(partidos_list)} partidos guardados en {ARCHIVO_EXCEL}")
        else:
            print("📭 No se encontraron cuotas disponibles para los partidos de hoy.")

    except Exception as e:
        print(f"❌ Error en la recolección: {e}")

if __name__ == "__main__":
    recolectar_cuotas()
