// Generated from .\Smolang.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SmolangParser}.
 */
public interface SmolangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SmolangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(SmolangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(SmolangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(SmolangParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(SmolangParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#lastline}.
	 * @param ctx the parse tree
	 */
	void enterLastline(SmolangParser.LastlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#lastline}.
	 * @param ctx the parse tree
	 */
	void exitLastline(SmolangParser.LastlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#while_st}.
	 * @param ctx the parse tree
	 */
	void enterWhile_st(SmolangParser.While_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#while_st}.
	 * @param ctx the parse tree
	 */
	void exitWhile_st(SmolangParser.While_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#if_st}.
	 * @param ctx the parse tree
	 */
	void enterIf_st(SmolangParser.If_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#if_st}.
	 * @param ctx the parse tree
	 */
	void exitIf_st(SmolangParser.If_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#return_st}.
	 * @param ctx the parse tree
	 */
	void enterReturn_st(SmolangParser.Return_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#return_st}.
	 * @param ctx the parse tree
	 */
	void exitReturn_st(SmolangParser.Return_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(SmolangParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(SmolangParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(SmolangParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(SmolangParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#func_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunc_declaration(SmolangParser.Func_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#func_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunc_declaration(SmolangParser.Func_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#codeblock}.
	 * @param ctx the parse tree
	 */
	void enterCodeblock(SmolangParser.CodeblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#codeblock}.
	 * @param ctx the parse tree
	 */
	void exitCodeblock(SmolangParser.CodeblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#funcall}.
	 * @param ctx the parse tree
	 */
	void enterFuncall(SmolangParser.FuncallContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#funcall}.
	 * @param ctx the parse tree
	 */
	void exitFuncall(SmolangParser.FuncallContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#show_func}.
	 * @param ctx the parse tree
	 */
	void enterShow_func(SmolangParser.Show_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#show_func}.
	 * @param ctx the parse tree
	 */
	void exitShow_func(SmolangParser.Show_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#read_func}.
	 * @param ctx the parse tree
	 */
	void enterRead_func(SmolangParser.Read_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#read_func}.
	 * @param ctx the parse tree
	 */
	void exitRead_func(SmolangParser.Read_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#custom_func}.
	 * @param ctx the parse tree
	 */
	void enterCustom_func(SmolangParser.Custom_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#custom_func}.
	 * @param ctx the parse tree
	 */
	void exitCustom_func(SmolangParser.Custom_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#global_assignment}.
	 * @param ctx the parse tree
	 */
	void enterGlobal_assignment(SmolangParser.Global_assignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#global_assignment}.
	 * @param ctx the parse tree
	 */
	void exitGlobal_assignment(SmolangParser.Global_assignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(SmolangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(SmolangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(SmolangParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(SmolangParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#list_value}.
	 * @param ctx the parse tree
	 */
	void enterList_value(SmolangParser.List_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#list_value}.
	 * @param ctx the parse tree
	 */
	void exitList_value(SmolangParser.List_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic(SmolangParser.ArithmeticContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic(SmolangParser.ArithmeticContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#ar_value}.
	 * @param ctx the parse tree
	 */
	void enterAr_value(SmolangParser.Ar_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#ar_value}.
	 * @param ctx the parse tree
	 */
	void exitAr_value(SmolangParser.Ar_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmolangParser#typ}.
	 * @param ctx the parse tree
	 */
	void enterTyp(SmolangParser.TypContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmolangParser#typ}.
	 * @param ctx the parse tree
	 */
	void exitTyp(SmolangParser.TypContext ctx);
}