import pandas as pd

data = {
    'Jugador_A': ['Carlos Alcaraz', 'Novak Djokovic'],
    'Jugador_B': ['Jannik Sinner', 'Daniil Medvedev'],
    'Superficie': ['Hard', 'Hard'],
    'SrvW_A': [0, 0],
    'TrnW_A': [0, 0],
    'SrvW_B': [0, 0],
    'TrnW_B': [0, 0]
}

df = pd.DataFrame(data)
df.to_excel('partidos.xlsx', index=False)
print("✅ Archivo 'partidos.xlsx' creado correctamente con el formato exacto.")
