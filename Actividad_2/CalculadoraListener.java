// Generated from Calculadora.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalculadoraParser}.
 */
public interface CalculadoraListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(CalculadoraParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(CalculadoraParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Asignacion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(CalculadoraParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Asignacion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(CalculadoraParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Impresion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterImpresion(CalculadoraParser.ImpresionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Impresion}
	 * labeled alternative in {@link CalculadoraParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitImpresion(CalculadoraParser.ImpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(CalculadoraParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(CalculadoraParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(CalculadoraParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(CalculadoraParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CalculadoraParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CalculadoraParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalculadoraParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CalculadoraParser.FactorContext ctx);
}