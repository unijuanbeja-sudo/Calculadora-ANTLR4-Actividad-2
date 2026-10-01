import os
import glob
import sys
from main import procesar_archivo

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    directorio_pruebas = os.path.join(os.path.dirname(__file__), 'pruebas')
    archivos = sorted(glob.glob(os.path.join(directorio_pruebas, '*.txt')))

    print("=" * 60)
    print("      EJECUCION DE BATERIA DE PRUEBAS LL(1)")
    print("=" * 60)

    for ruta in archivos:
        nombre = os.path.basename(ruta)
        print(f"\n>>> PRUEBA: {nombre}")
        procesar_archivo(ruta)
        print("-" * 60)

if __name__ == '__main__':
    main()
