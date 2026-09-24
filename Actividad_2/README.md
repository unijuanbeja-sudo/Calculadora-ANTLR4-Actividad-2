# Actividad 2 - Calculadora con ANTLR4 y Python
Juan Bejarano, Alejandro Poveda, Sebastian Chaux
## Descripción

En esta actividad se implementa una calculadora utilizando **ANTLR4** para realizar el análisis léxico y sintáctico de expresiones, junto con Python para realizar la evaluación semántica mediante el patrón **Visitor**.

La calculadora permite trabajar con:

* Variables.
* Asignaciones.
* Suma `+`.
* Resta `-`.
* Multiplicación `*`.
* División `/`.
* Módulo `%`.
* Paréntesis.
* Valor absoluto `abs()`.
* Seno `Sin()`.
* Coseno `Cos()`.
* Tangente `Tan()`.
* Números enteros y decimales.

También se utiliza una tabla de símbolos para almacenar los valores de las variables definidas durante la ejecución.

---

## Archivos principales

### `Calculadora.g4`

Contiene la gramática utilizada por ANTLR4.

En ella se definen las reglas léxicas y sintácticas necesarias para reconocer las instrucciones y expresiones de la calculadora.

### `main.py`

Contiene el evaluador semántico de la calculadora.

Se utiliza el patrón **Visitor** para recorrer el árbol sintáctico generado por ANTLR y realizar las operaciones correspondientes.

La clase `EvaluadorSemantico` mantiene una tabla de símbolos llamada `memoria`, donde se almacenan las variables declaradas.

### `antlr-4.13.1-complete.jar`

Archivo de ANTLR4 utilizado para generar el lexer, parser y visitor a partir de la gramática.

---

# Generación del analizador

Para generar los archivos necesarios para Python se utiliza:

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Calculadora.g4
```

Después de ejecutar el comando deben generarse archivos como:

```text
CalculadoraLexer.py
CalculadoraParser.py
CalculadoraListener.py
CalculadoraVisitor.py
```

## Evidencia 1 - Generación de archivos ANTLR

En esta prueba se verifica que ANTLR4 procese correctamente la gramática `Calculadora.g4` y genere los archivos necesarios para utilizar el analizador desde Python.

Comandos utilizados:

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Calculadora.g4
ls
```

**Resultado esperado:** deben aparecer `CalculadoraLexer.py`, `CalculadoraParser.py` y `CalculadoraVisitor.py`.

<img width="637" height="545" alt="image" src="https://github.com/user-attachments/assets/c4275148-c428-433d-a356-be31a5b05808" />


---

# Prueba de ejecución general

El programa utiliza inicialmente las siguientes instrucciones:

```text
x = 10 + 5 * 2;
y = Sin(0) + abs(-15);
z = y % 4;
z;
```

Con esta prueba se comprueba el funcionamiento de las operaciones aritméticas, precedencia de operadores, funciones matemáticas, asignación de variables y recuperación de valores desde la tabla de símbolos.

Para ejecutar:

```bash
python3 main.py
```

Los resultados esperados son:

```text
Asignacion semantica: x = 20.0
Asignacion semantica: y = 15.0
Asignacion semantica: z = 3.0
Resultado de evaluacion: 3.0
```

## Evidencia 2 - Operaciones y precedencia

La expresión:

```text
x = 10 + 5 * 2;
```

permite comprobar la precedencia de operadores.

La multiplicación se evalúa primero:

```text
5 * 2 = 10
```

y posteriormente:

```text
10 + 10 = 20
```

Por lo tanto:

```text
x = 20
```

<img width="637" height="255" alt="image" src="https://github.com/user-attachments/assets/7fdb1348-ca0e-440f-82a7-bb235a6f9271" />

---

## Evidencia 3 - Funciones matemáticas

La instrucción:

```text
y = Sin(0) + abs(-15);
```

comprueba el funcionamiento de funciones matemáticas definidas en la gramática.

Se obtiene:

```text
Sin(0) = 0
abs(-15) = 15
```

Por lo tanto:

```text
y = 15
```

<img width="647" height="231" alt="image" src="https://github.com/user-attachments/assets/2c192f09-26a9-43d4-8376-1e6e020020df" />


---

## Evidencia 4 - Variables, tabla de símbolos y módulo

La instrucción:

```text
z = y % 4;
```

utiliza el valor previamente almacenado para `y`.

Como:

```text
y = 15
```

entonces:

```text
15 % 4 = 3
```

El resultado se almacena en la variable `z`.

Posteriormente:

```text
z;
```

recupera el valor desde la tabla de símbolos y muestra:

```text
Resultado de evaluacion: 3.0
```

Esta prueba demuestra que las variables permanecen almacenadas durante la ejecución.

<img width="632" height="132" alt="image" src="https://github.com/user-attachments/assets/254204b6-224a-4a82-bc39-4f7c4e20e2e4" />


---

# Manejo de errores semánticos

Además de evaluar operaciones correctas, el programa detecta algunos errores durante el análisis semántico.

## Evidencia 5 - División por cero

Se realiza una prueba con:

```text
10 / 0;
```

El evaluador detecta que el divisor es cero y genera el mensaje:

```text
Error semantico: Division por cero detectada.
```

Esto evita realizar una operación matemáticamente inválida.

> **CAPTURA EVIDENCIA 5 - Error de división por cero**

<img width="646" height="113" alt="image" src="https://github.com/user-attachments/assets/ecfc9c2c-dcaf-4d18-aac3-46ba469c9f4c" />


---

## Evidencia 6 - Variable no definida

Se realiza una prueba utilizando una variable que no ha sido declarada previamente:

```text
a + 5;
```

Como la variable `a` no se encuentra almacenada en la tabla de símbolos, el evaluador genera un error indicando que la variable no ha sido definida.

Resultado esperado:

```text
Error semantico: La variable 'a' no ha sido definida.
```

> **CAPTURA EVIDENCIA 6 - Variable no definida**

<img width="637" height="97" alt="image" src="https://github.com/user-attachments/assets/0c522694-e259-4409-9016-dcab8456f227" />


---

# Conclusiones

La implementación permite observar las diferentes etapas involucradas en el procesamiento de un lenguaje.

ANTLR4 utiliza la gramática definida en `Calculadora.g4` para generar el **Lexer** y el **Parser**.

El Lexer reconoce los componentes léxicos de la entrada y el Parser comprueba que estos elementos cumplan con la estructura definida por la gramática.

Posteriormente, el árbol sintáctico generado es recorrido mediante el patrón **Visitor**, donde se realiza la evaluación semántica de las expresiones.

La tabla de símbolos permite almacenar y recuperar variables durante la ejecución, mientras que las validaciones semánticas permiten detectar situaciones como una división por cero o el uso de variables que no han sido declaradas.

De esta manera se integran el análisis léxico, sintáctico y semántico dentro de una misma aplicación desarrollada con ANTLR4 y Python.
