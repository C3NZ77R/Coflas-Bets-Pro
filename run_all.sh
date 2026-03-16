
#!/bin/bash

clear
echo "=========================================="
echo "   🎾 SISTEMA PRO COFLAS BETS (API) 🎾    "
echo "=========================================="

# Registro de inicio
python -c "import logger_pro; logger_pro.registrar_evento('--- INICIANDO CICLO DE ANÁLISIS ---')"

echo "🌐 Conectando con la API..."
python recolector_api.py || python -c "import logger_pro; logger_pro.registrar_evento('ERROR en Recolector API', 'ERROR')"

echo "📊 Buscando estadísticas..."
python colector_auto.py || python -c "import logger_pro; logger_pro.registrar_evento('ERROR en Colector Estadísticas', 'ERROR')"

echo "🧠 Calculando probabilidades..."
python analizador_tenis.py || python -c "import logger_pro; logger_pro.registrar_evento('ERROR en Analizador IA', 'ERROR')"

echo "📲 Enviando alertas a Telegram..."
python notificador_bot.py && python -c "import logger_pro; logger_pro.registrar_evento('CICLO FINALIZADO: Alertas enviadas con éxito.')" || python -c "import logger_pro; logger_pro.registrar_evento('ERROR en Notificador Telegram', 'ERROR')"

echo "=========================================="
echo " ✅ PROCESO FINALIZADO CON ÉXITO"
echo "=========================================="
