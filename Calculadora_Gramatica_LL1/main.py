import sys
from lexer import lexer
from parser_calc import Parser

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def procesar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()

        print(f"--- Analizando el código de: {ruta_archivo} ---")

        # 1. Fase Léxica
        tokens = lexer(codigo)

        # 2 y 3. Fase Sintáctica y Semántica
        analizador = Parser(tokens)
        resultado = analizador.parse_programa()

        print(f"Resultado final: {resultado}")
        if analizador.variables:
            print("Variables almacenadas:")
            for var, val in analizador.variables.items():
                print(f"  {var} = {val}")
        return resultado

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'. Revisa la ruta.")
    except Exception as e:
        print(f"Detenido por error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso correcto en terminal: python3 main.py <archivo.txt>")
    else:
        archivo_txt = sys.argv[1]
        procesar_archivo(archivo_txt)
