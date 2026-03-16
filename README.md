# Coflas Bets Pro: Análisis Estadístico de Mercados ATP/WTA

![Status](https://img.shields.io/badge/Status-Development-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ADSO](https://img.shields.io/badge/Program-SENA%20ADSO-orange)

Coflas Bets Pro es una solución de software diseñada para el monitoreo y análisis técnico de mercados deportivos en tiempo real. El sistema aplica modelos matemáticos sobre cuotas decimales para identificar ineficiencias en el mercado de **Over 8.5 juegos en el primer set**, facilitando la toma de decisiones basada en datos estadísticos.

## Arquitectura del Sistema

La solución implementa un pipeline de datos estructurado en tres capas funcionales:

1. **Capa de Ingesta:** Consumo asíncrono de datos dinámicos mediante el SDK de `The Odds API`, permitiendo la captura de mercados globales (ATP, WTA y Challengers).
2. **Capa de Procesamiento:** Módulo de lógica de negocio desarrollado en Python que ejecuta el cálculo de paridad competitiva. El sistema normaliza las cuotas para derivar un índice de probabilidad propia.
3. **Capa de Presentación:** Interfaz de línea de comandos (CLI) optimizada para entornos móviles y terminales Linux (Termux), con gestión de estados y refresco de datos automatizado.

## Fundamentación Matemática (Estrategia Over 8.5)

El núcleo algorítmico del proyecto evalúa la paridad de los competidores mediante la siguiente fórmula:

$$Indice = \frac{1}{|Cuota_{L} - Cuota_{V}| + 0.1}$$

Donde:
* **$Cuota_{L}$:** Precio decimal asignado al competidor local.
* **$Cuota_{V}$:** Precio decimal asignado al competidor visitante.

Un índice resultante superior a **2.0** denota una alta convergencia competitiva. Desde una perspectiva estadística, esta paridad reduce la desviación estándar en la densidad de juegos por set, aumentando significativamente la probabilidad de superar el umbral de 8.5 juegos (resultados de 6-3, 6-4, 7-5 o 7-6).

## Instalación y Configuración (Termux / Linux)

1. **Clonación del Repositorio:**
   ```bash
   git clone [https://github.com/C3NZ77R/Coflas-Bets-Pro.git](https://github.com/C3NZ77R/Coflas-Bets-Pro.git)
   cd Coflas-Bets-Pro

 * Gestión de Dependencias:
   pip install pandas requests openpyxl

 * Despliegue del Sistema:
   * Ejecución del servicio de datos: python recolector_api.py
   * Lanzamiento del dashboard de monitoreo: python coflas_terminal.py
Roadmap de Desarrollo
 * [x] Integración dinámica de endpoints (Auto-Discovery de Torneos).
 * [x] Gestión de persistencia de datos en formato Excel/OpenPyXL.
 * [ ] Implementación de Webhook para notificaciones automáticas mediante API de Telegram.
 * [ ] Migración de almacenamiento local a base de datos relacional (SQLite) para análisis histórico.
Desarrollado por: Camilo Rios
Perfil: Analista y Desarrollador de Software (ADSO) - SENA

---

### 🛠️ Bonus: Crear el archivo `requirements.txt`
Para que tu repositorio sea 100% profesional, deberías tener un archivo que liste las librerías. Ejecuta esto en tu terminal:

```bash
echo "pandas" > requirements.txt
echo "requests" >> requirements.txt
echo "openpyxl" >> requirements.txt

Luego sube todo a GitHub:
git add README.md requirements.txt
git commit -m "docs: version profesional del readme y requisitos"
git push origin master
