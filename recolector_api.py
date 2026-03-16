import requests
import pandas as pd

API_KEY = '910fc4baff822d77b6bfb7cba8b1b68a'

# Lista de torneos por orden de importancia
PRIORIDADES = [
    'tennis_atp_miami_open',
    'tennis_wta_miami_open',
    'tennis_atp_indian_wells',
    'tennis_wta_indian_wells',
    'tennis_atp_challenger_tour', # El comodín si no hay grandes
    'tennis_atp_french_open',
    'tennis_wta_french_open'
]

def obtener_partidos_inteligente():
    torneo_encontrado = None
    partidos = []

    print("📡 Iniciando búsqueda inteligente de torneos...")

    for torneo in PRIORIDADES:
        url = f'https://api.the-odds-api.com/v4/sports/{torneo}/odds/'
        params = {'apiKey': API_KEY, 'regions': 'us', 'markets': 'h2h'}
        
        try:
            response = requests.get(url, params=params)
            data = response.json()

            # Si la lista tiene partidos, nos quedamos con este torneo
            if isinstance(data, list) and len(data) > 0:
                torneo_encontrado = torneo
                for match in data:
                    partidos.append({
                        'Jugador_A': match['home_team'],
                        'Jugador_B': match['away_team'],
                        'Superficie': 'Hard', # Podríamos automatizar esto luego
                        'SrvW_A': 0, 'TrnW_A': 0, 'SrvW_B': 0, 'TrnW_B': 0
                    })
                break # Salimos del bucle porque ya encontramos el mejor torneo
        except:
            continue

    if partidos:
        pd.DataFrame(partidos).to_excel('partidos.xlsx', index=False)
        print(f"✅ ¡Torneo detectado!: {torneo_encontrado}")
        print(f"📊 {len(partidos)} partidos listos para analizar.")
        return torneo_encontrado
    else:
        print("❌ No se encontraron partidos en ninguna de las categorías hoy.")
        return None

if __name__ == "__main__":
    obtener_partidos_inteligente()
