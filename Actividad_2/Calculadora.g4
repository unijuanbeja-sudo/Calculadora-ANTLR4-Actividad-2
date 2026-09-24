grammar Calculadora;

// --- REGLAS SINTÁCTICAS ---
programa : instruccion+ ;

instruccion : ID '=' expresion ';' # Asignacion
            | expresion ';'        # Impresion
            ;

expresion : termino (('+' | '-') termino)* ;

termino : factor (('*' | '/' | '%') factor)* ;

factor : 'abs' '(' expresion ')'
       | 'Sin' '(' expresion ')'
       | 'Cos' '(' expresion ')'
       | 'Tan' '(' expresion ')'
       | '(' expresion ')'
       | ID
       | NUMERO
       ;

// --- REGLAS LÉXICAS ---
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO : [0-9]+ ('.' [0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;
