import pandas as pd
import requests

TOKEN = "8533416944:AAGBAh8ShF4grU_DxMQLyQSCZyMWOaEy_jQ"
CHAT_ID = "7523136508"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"})

def procesar_y_enviar():
    df = pd.read_excel('PRONOSTICOS_EQUIDAD.xlsx')
    top_picks = df[df['Pronostico'].str.contains("TOP PICK", na=False)]

    if top_picks.empty:
        enviar_telegram("⚠️ *Coflas Bets:* Sin TOP PICKS claros ahora.")
        return

    msg = "🎾 *ALERTAS COFLAS BETS PRO*\n🎯 *Over 8.5 (Set 1)*\n━━━━━━━━━━━━━━\n\n"
    for _, r in top_picks.head(5).iterrows():
        msg += f"💎 *{r['Jugador_A']} vs {r['Jugador_B']}*\n📊 Score: `{r['Confianza']}`\n✅ {r['Pronostico']}\n━━━━━━━━━━━━━━\n"
    
    enviar_telegram(msg)
    print("🚀 Notificación enviada.")

if __name__ == "__main__":
    procesar_y_enviar()
