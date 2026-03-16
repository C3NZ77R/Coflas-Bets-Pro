import pandas as pd
import os

def calcular_pronostico_set1_pro(row):
    try:
        hold_a = row['SrvW_A'] 
        hold_b = row['SrvW_B']
        
        # 1. CÁLCULO BASE (Estabilidad Combinada)
        indice_estabilidad = hold_a + hold_b
        
        # 2. REGLA DE EQUIDAD (Anti-Palizas)
        # Calculamos la diferencia absoluta entre ambos saques
        brecha = abs(hold_a - hold_b)
        
        # Si la brecha es muy grande (>15%), restamos puntos al score de confianza
        penalizacion = 0
        if brecha > 15:
            penalizacion = brecha * 0.5  # A mayor desigualdad, más resta
            
        # 3. AJUSTE POR SUPERFICIE
        superficie = str(row['Superficie']).lower()
        ajuste = 1.0
        if 'hard' in superficie: ajuste = 1.02
        elif 'grass' in superficie: ajuste = 1.08
        elif 'clay' in superficie: ajuste = 0.95
        
        # SCORE FINAL PRO
        score_final = (indice_estabilidad - penalizacion) * ajuste
        
        # NUEVOS UMBRALES CON FILTRO DE EQUIDAD
        if score_final > 128 and brecha <= 12:
            return "🔥 TOP PICK: OVER 8.5 (Equilibrio Perfecto)", round(score_final, 2)
        elif score_final > 120:
            return "✅ OVER 8.5 (Probable)", round(score_final, 2)
        elif brecha > 20:
            return "⚠️ RIESGO ALTO: Desigualdad (Posible 6-1)", round(score_final, 2)
        else:
            return "❄️ NEUTRO / BAJA ESTABILIDAD", round(score_final, 2)
            
    except:
        return "Error en datos", 0

def ejecutar():
    archivo_entrada = 'partidos_automatizados.xlsx'
    if not os.path.exists(archivo_entrada):
        print(f"❌ Error: No se encontró {archivo_entrada}")
        return

    df = pd.read_excel(archivo_entrada)
    
    # Aplicar la nueva lógica Pro con Equidad
    resultados = df.apply(lambda row: calcular_pronostico_set1_pro(row), axis=1)
    df['Pronostico'], df['Confianza'] = zip(*resultados)
    
    # Guardar resultados
    df.to_excel('PRONOSTICOS_EQUIDAD.xlsx', index=False)
    
    print("\n" + "="*55)
    print(" 🧠  COFLAS BETS V2.0 - FILTRO DE EQUIDAD (+8.5)  🧠 ")
    print("="*55)

    # --- TOP 5 SELECCIONADOS POR VALOR REAL ---
    print("\n💎 LAS 5 MEJORES ENTRADAS (Set 1) 💎")
    print("-" * 55)
    
    # Filtramos para que no nos muestre los de Riesgo en el Top 5 si es posible
    df_top = df.sort_values(by='Confianza', ascending=False).head(5)
    
    for i, r in df_top.iterrows():
        print(f"🎾 {r['Jugador_A']} vs {r['Jugador_B']}")
        print(f"   📊 Score con Equidad: {r['Confianza']}")
        print(f"   🎯 Veredicto: {r['Pronostico']}")
        print("-" * 55)

if __name__ == "__main__":
    ejecutar()
