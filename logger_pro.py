import datetime
import os

LOG_FILE = "sistema_alertas.log"

def registrar_evento(mensaje, nivel="INFO"):
    """
    Niveles: INFO, ADVERTENCIA, ERROR
    """
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha_hora}] [{nivel}] - {mensaje}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea)
    print(f"📝 Log: {mensaje}")

if __name__ == "__main__":
    registrar_evento("El sistema de logs ha sido inicializado correctamente.")
