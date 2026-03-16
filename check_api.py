import requests

API_KEY = '910fc4baff822d77b6bfb7cba8b1b68a'
url = f'https://api.the-odds-api.com/v4/sports/?apiKey={API_KEY}'

print("🔍 Buscando deportes activos para tu API Key...")
response = requests.get(url)
data = response.json()

if isinstance(data, list):
    # Filtramos solo los que son de Tenis
    tenis_disponible = [s['key'] for s in data if 'tennis' in s['key']]
    print("\n✅ Deportes de tenis que puedes usar AHORA:")
    for t in tenis_disponible:
        print(f" -> {t}")
else:
    print(f"❌ Error real de la API: {data}")
