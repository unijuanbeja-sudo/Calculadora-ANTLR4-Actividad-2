import sys
import math
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor

# Evaluador Semantico usando el patron Visitor
class EvaluadorSemantico(CalculadoraVisitor):
    def __init__(self):
        # Tabla de simbolos para guardar las variables declaradas
        self.memoria = {}

    def visitAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memoria[nombre_var] = valor
        print(f"Asignacion semantica: {nombre_var} = {valor}")
        return valor

    def visitImpresion(self, ctx):
        valor = self.visit(ctx.expresion())
        print(f"Resultado de evaluacion: {valor}")
        return valor

    def visitExpresion(self, ctx):
        res = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2 * i - 1).getText()
            siguiente = self.visit(ctx.termino(i))
            if op == '+':
                res += siguiente
            elif op == '-':
                res -= siguiente
        return res

    def visitTermino(self, ctx):
        res = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            siguiente = self.visit(ctx.factor(i))
            if op == '*':
                res *= siguiente
            elif op == '/':
                if siguiente == 0:
                    raise ValueError("Error semantico: Division por cero detectada.")
                res /= siguiente
            elif op == '%':
                res %= siguiente
        return res

    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            if nombre in self.memoria:
                return self.memoria[nombre]
            else:
                raise NameError(f"Error semantico: La variable '{nombre}' no ha sido definida.")
        elif ctx.getChild(0).getText() == 'abs':
            return abs(self.visit(ctx.expresion()))
        elif ctx.getChild(0).getText() == 'Sin':
            return math.sin(self.visit(ctx.expresion()))
        elif ctx.getChild(0).getText() == 'Cos':
            return math.cos(self.visit(ctx.expresion()))
        elif ctx.getChild(0).getText() == 'Tan':
            return math.tan(self.visit(ctx.expresion()))
        elif ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expresion())

def main():
    codigo_prueba = """
    x = 10 + 5 * 2;
    y = Sin(0) + abs(-15);
    z = y % 4;
    z;
    """
    print("--- INICIANDO ANALISIS LEXICO Y SINTACTICO ---")
    input_stream = InputStream(codigo_prueba)
    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)
    tree = parser.programa()

    print("\n--- INICIANDO EVALUACION SEMANTICA ---")
    evaluador = EvaluadorSemantico()
    evaluador.visit(tree)

if __name__ == '__main__':
    main()
