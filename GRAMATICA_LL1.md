# Taller: Diseño e Implementación de Gramática LL(1)
**Calculadora con Operaciones Aritméticas, Funciones Trigonométricas, Abs y Variables**

---

## Alcance y Especificación del Lenguaje

El lenguaje soporta:
- **Operaciones Aritméticas**: Adición (`+`), Sustracción (`-`), Multiplicación (`*`), División (`/`), Módulo (`%`).
- **Operador Unario**: Negativo (`-`) y Positivo (`+`).
- **Funciones Matemáticas**: Seno (`sin`), Coseno (`cos`), Tangente (`tan`), Valor Absoluto (`abs`).
- **Asignación y uso de variables**: Identificadores alfanuméricos (`ID = Expresión ;`).
- **Uso de paréntesis**: Agrupación y precedencia de expresiones `( ... )`.
- **Estructura de sentencias**: Secuencias de sentencias finalizadas con punto y coma (`;`).

---

## Gramática Formal LL(1)

Para evitar la ambigüedad y permitir análisis determinista con 1 token de anticipación ($k=1$), se aplicaron dos transformaciones clásicas:
1. **Eliminación de Recursión Izquierda**: Para establecer la precedencia usual de operadores (aditivos y multiplicativos).
2. **Factorización por la Izquierda de Sentencias**: Permite discernir entre una asignación (`x = 5;`) y una expresión que inicia con una variable (`x + 5;`) mediante un solo token de lookahead.

### Símbolos Terminales ($V_T$)
`NUMERO`, `ID`, `ASIGNAR` (`=`), `SUMA` (`+`), `RESTA` (`-`), `MULT` (`*`), `DIV` (`/`), `MOD` (`%`), `PAREN_I` (`(`), `PAREN_D` (`)`), `SIN` (`sin`), `COS` (`cos`), `TAN` (`tan`), `ABS` (`abs`), `PUNTOCOMA` (`;`), `$` (Fin de entrada / EOF).

### Símbolos No Terminales ($V_N$)
- $P$: Programa principal
- $L$: Lista de sentencias
- $S$: Sentencia
- $R$: Sentencia resto (luego de consumir un `ID`)
- $E$: Expresión
- $E'$: Expresión prima
- $T$: Término
- $T'$: Término prima
- $F$: Factor
- $F_{no\_id}$: Factor que no empieza con identificador
- $Fn$: Nombre de función matemática

### Reglas de Producción
1. $P \to L\ \$$
2. $L \to S\ L$
3. $L \to \varepsilon$
4. $S \to \text{ID}\ R$
5. $S \to F_{no\_id}\ T'\ E'\ ;$
6. $R \to =\ E\ ;$
7. $R \to T'\ E'\ ;$
8. $E \to T\ E'$
9. $E' \to +\ T\ E'$
10. $E' \to -\ T\ E'$
11. $E' \to \varepsilon$
12. $T \to F\ T'$
13. $T' \to *\ F\ T'$
14. $T' \to /\ F\ T'$
15. $T' \to \%\ F\ T'$
16. $T' \to \varepsilon$
17. $F \to \text{ID}$
18. $F \to F_{no\_id}$
19. $F_{no\_id} \to \text{NUMERO}$
20. $F_{no\_id} \to (\ E\ )$
21. $F_{no\_id} \to Fn\ (\ E\ )$
22. $F_{no\_id} \to -\ F$
23. $F_{no\_id} \to +\ F$
24. $Fn \to \text{sin}$
25. $Fn \to \text{cos}$
26. $Fn \to \text{tan}$
27. $Fn \to \text{abs}$

---

## Conjuntos PRIMEROS y SIGUIENTES

### Definiciones
- **$PRIMEROS(\alpha)$**: Conjunto de terminales que pueden aparecer al inicio de una cadena derivada de $\alpha$. Contiene $\varepsilon$ si $\alpha \Rightarrow^* \varepsilon$.
- **$SIGUIENTES(A)$**: Conjunto de terminales que pueden aparecer inmediatamente a la derecha de $A$ en alguna forma sentencial. Incluye $\$$ en el símbolo inicial. $\varepsilon$ **nunca** pertenece a SIGUIENTES.

### Tabla de PRIMEROS y SIGUIENTES
| No Terminal | PRIMEROS | SIGUIENTES |
| :--- | :--- | :--- |
| **$P$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, +, $ }` | `{ $ }` |
| **$L$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, +, ε }` | `{ $ }` |
| **$S$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` | `{ ID, NUMERO, (, sin, cos, tan, abs, -, +, $ }` |
| **$R$** | `{ =, *, /, %, +, -, ; }` | `{ ID, NUMERO, (, sin, cos, tan, abs, -, +, $ }` |
| **$E$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` | `{ ;, ) }` |
| **$E'$** | `{ +, -, ε }` | `{ ;, ) }` |
| **$T$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` | `{ +, -, ;, ) }` |
| **$T'$** | `{ *, /, %, ε }` | `{ +, -, ;, ) }` |
| **$F$** | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` | `{ *, /, %, +, -, ;, ) }` |
| **$F_{no\_id}$** | `{ NUMERO, (, sin, cos, tan, abs, -, + }` | `{ *, /, %, +, -, ;, ) }` |
| **$Fn$** | `{ sin, cos, tan, abs }` | `{ ( }` |

---

## Conjuntos de PREDICCIÓN y Validación LL(1)

La regla formal de predicción para una producción $A \to \alpha$ es:
$$PRED(A \to \alpha) = \begin{cases} PRIMEROS(\alpha) & \text{si } \varepsilon \notin PRIMEROS(\alpha) \\ (PRIMEROS(\alpha) - \{\varepsilon\}) \cup SIGUIENTES(A) & \text{si } \varepsilon \in PRIMEROS(\alpha) \end{cases}$$

### Tabla de Predicciones por Regla
| N° | Regla | Cálculo | Conjunto de Predicción |
| :--- | :--- | :--- | :--- |
| 1 | $P \to L\ \$$ | $PRIMEROS(L\ \$)$ | `{ ID, NUMERO, (, sin, cos, tan, abs, -, +, $ }` |
| 2 | $L \to S\ L$ | $PRIMEROS(S)$ | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` |
| 3 | $L \to \varepsilon$ | $SIGUIENTES(L)$ | `{ $ }` |
| 4 | $S \to \text{ID}\ R$ | $PRIMEROS(\text{ID})$ | `{ ID }` |
| 5 | $S \to F_{no\_id}\ T'\ E'\ ;$ | $PRIMEROS(F_{no\_id})$ | `{ NUMERO, (, sin, cos, tan, abs, -, + }` |
| 6 | $R \to =\ E\ ;$ | $PRIMEROS(=)$ | `{ = }` |
| 7 | $R \to T'\ E'\ ;$ | $PRIMEROS(T'\ E'\ ;)$ | `{ *, /, %, +, -, ; }` |
| 8 | $E \to T\ E'$ | $PRIMEROS(T)$ | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` |
| 9 | $E' \to +\ T\ E'$ | $PRIMEROS(+)$ | `{ + }` |
| 10 | $E' \to -\ T\ E'$ | $PRIMEROS(-)$ | `{ - }` |
| 11 | $E' \to \varepsilon$ | $SIGUIENTES(E')$ | `{ ;, ) }` |
| 12 | $T \to F\ T'$ | $PRIMEROS(F)$ | `{ ID, NUMERO, (, sin, cos, tan, abs, -, + }` |
| 13 | $T' \to *\ F\ T'$ | $PRIMEROS(*)$ | `{ * }` |
| 14 | $T' \to /\ F\ T'$ | $PRIMEROS(/)$ | `{ / }` |
| 15 | $T' \to \%\ F\ T'$ | $PRIMEROS(\%)$ | `{ % }` |
| 16 | $T' \to \varepsilon$ | $SIGUIENTES(T')$ | `{ +, -, ;, ) }` |
| 17 | $F \to \text{ID}$ | $PRIMEROS(\text{ID})$ | `{ ID }` |
| 18 | $F \to F_{no\_id}$ | $PRIMEROS(F_{no\_id})$ | `{ NUMERO, (, sin, cos, tan, abs, -, + }` |
| 19 | $F_{no\_id} \to \text{NUMERO}$ | $PRIMEROS(\text{NUMERO})$ | `{ NUMERO }` |
| 20 | $F_{no\_id} \to (\ E\ )$ | $PRIMEROS(()$ | `{ ( }` |
| 21 | $F_{no\_id} \to Fn\ (\ E\ )$ | $PRIMEROS(Fn)$ | `{ sin, cos, tan, abs }` |
| 22 | $F_{no\_id} \to -\ F$ | $PRIMEROS(-)$ | `{ - }` |
| 23 | $F_{no\_id} \to +\ F$ | $PRIMEROS(+)$ | `{ + }` |
| 24 | $Fn \to \text{sin}$ | $PRIMEROS(\text{sin})$ | `{ sin }` |
| 25 | $Fn \to \text{cos}$ | $PRIMEROS(\text{cos})$ | `{ cos }` |
| 26 | $Fn \to \text{tan}$ | $PRIMEROS(\text{tan})$ | `{ tan }` |
| 27 | $Fn \to \text{abs}$ | $PRIMEROS(\text{abs})$ | `{ abs }` |

### Comprobación del Criterio LL(1)
Para cada no terminal con dos o más alternativas:
- **$L$**: $PRED(2) \cap PRED(3) = \{ \text{ID}, \dots \} \cap \{ \$ \} = \emptyset$ (Disjuntos)
- **$S$**: $PRED(4) \cap PRED(5) = \{ \text{ID} \} \cap \{ \text{NUMERO}, (, \dots \} = \emptyset$ (Disjuntos)
- **$R$**: $PRED(6) \cap PRED(7) = \{ = \} \cap \{ *, /, \%, +, -, ; \} = \emptyset$ (Disjuntos)
- **$E'$**: $PRED(9) \cap PRED(10) = \emptyset$, $PRED(9) \cap PRED(11) = \emptyset$, $PRED(10) \cap PRED(11) = \emptyset$ (Disjuntos dos a dos)
- **$T'$**: $PRED(13)$, $PRED(14)$, $PRED(15)$, $PRED(16)$ son `{ * }`, `{ / }`, `{ % }` y `{ +, -, ;, ) }`. Ninguno se solapa. (Disjuntos dos a dos)
- **$F$**: $PRED(17) \cap PRED(18) = \{ \text{ID} \} \cap \{ \text{NUMERO}, \dots \} = \emptyset$ (Disjuntos)
- **$F_{no\_id}$**: Las reglas 19, 20, 21, 22 y 23 predicen `{NUMERO}`, `{ ( }`, `{sin, cos, tan, abs}`, `{ - }` y `{ + }`. Ninguno se solapa. (Disjuntos dos a dos)
- **$Fn$**: Las reglas 24, 25, 26 y 27 predicen `{sin}`, `{cos}`, `{tan}`, `{abs}`. Ninguno se solapa. (Disjuntos dos a dos)

**Conclusión**: La gramática satisface estrictamente el criterio de determinismo LL(1).

---

## Garantía de Fases del Compilador

1. **Fase Léxica (`lexer.py`)**:
   - Escanea el texto y convierte la entrada en tokens tipados.
   - Detecta y reporta errores léxicos para cualquier símbolo no permitido con número de línea y columna.
2. **Fase Sintáctica (`parser_calc.py`)**:
   - Implementa un analizador sintáctico descendente recursivo dirigido por predicción.
   - Si un token en la entrada no pertenece al conjunto de predicción de la producción esperada, emite un error sintáctico descriptivo.
3. **Fase Semántica (`parser_calc.py`)**:
   - Administra el entorno de memoria / tabla de símbolos (`self.variables`).
   - Valida el uso de identificadores, impidiendo el uso de variables no inicializadas.
   - Detecta división entre cero (`/ 0`) y módulo entre cero (`% 0`).
   - Verifica dominios numéricos en funciones (ej. tangentes indeterminadas cuando el coseno es 0).

---

## Instrucciones de Ejecución

Para ejecutar un archivo de prueba:
```bash
python main.py pruebas/04_completo.txt
```

Para ver la verificación matemática y los conjuntos:
```bash
python mostrar_conjuntos.py
```

Para ejecutar la suite completa de pruebas:
```bash
python ejecutar_pruebas.py
```
