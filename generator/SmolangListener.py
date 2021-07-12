# Generated from .\Smolang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmolangParser import SmolangParser
else:
    from SmolangParser import SmolangParser

# This class defines a complete listener for a parse tree produced by SmolangParser.
class SmolangListener(ParseTreeListener):

    # Enter a parse tree produced by SmolangParser#program.
    def enterProgram(self, ctx:SmolangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SmolangParser#program.
    def exitProgram(self, ctx:SmolangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SmolangParser#line.
    def enterLine(self, ctx:SmolangParser.LineContext):
        pass

    # Exit a parse tree produced by SmolangParser#line.
    def exitLine(self, ctx:SmolangParser.LineContext):
        pass


    # Enter a parse tree produced by SmolangParser#lastline.
    def enterLastline(self, ctx:SmolangParser.LastlineContext):
        pass

    # Exit a parse tree produced by SmolangParser#lastline.
    def exitLastline(self, ctx:SmolangParser.LastlineContext):
        pass


    # Enter a parse tree produced by SmolangParser#while_st.
    def enterWhile_st(self, ctx:SmolangParser.While_stContext):
        pass

    # Exit a parse tree produced by SmolangParser#while_st.
    def exitWhile_st(self, ctx:SmolangParser.While_stContext):
        pass


    # Enter a parse tree produced by SmolangParser#if_st.
    def enterIf_st(self, ctx:SmolangParser.If_stContext):
        pass

    # Exit a parse tree produced by SmolangParser#if_st.
    def exitIf_st(self, ctx:SmolangParser.If_stContext):
        pass


    # Enter a parse tree produced by SmolangParser#return_st.
    def enterReturn_st(self, ctx:SmolangParser.Return_stContext):
        pass

    # Exit a parse tree produced by SmolangParser#return_st.
    def exitReturn_st(self, ctx:SmolangParser.Return_stContext):
        pass


    # Enter a parse tree produced by SmolangParser#condition.
    def enterCondition(self, ctx:SmolangParser.ConditionContext):
        pass

    # Exit a parse tree produced by SmolangParser#condition.
    def exitCondition(self, ctx:SmolangParser.ConditionContext):
        pass


    # Enter a parse tree produced by SmolangParser#operator.
    def enterOperator(self, ctx:SmolangParser.OperatorContext):
        pass

    # Exit a parse tree produced by SmolangParser#operator.
    def exitOperator(self, ctx:SmolangParser.OperatorContext):
        pass


    # Enter a parse tree produced by SmolangParser#func_declaration.
    def enterFunc_declaration(self, ctx:SmolangParser.Func_declarationContext):
        pass

    # Exit a parse tree produced by SmolangParser#func_declaration.
    def exitFunc_declaration(self, ctx:SmolangParser.Func_declarationContext):
        pass


    # Enter a parse tree produced by SmolangParser#codeblock.
    def enterCodeblock(self, ctx:SmolangParser.CodeblockContext):
        pass

    # Exit a parse tree produced by SmolangParser#codeblock.
    def exitCodeblock(self, ctx:SmolangParser.CodeblockContext):
        pass


    # Enter a parse tree produced by SmolangParser#funcall.
    def enterFuncall(self, ctx:SmolangParser.FuncallContext):
        pass

    # Exit a parse tree produced by SmolangParser#funcall.
    def exitFuncall(self, ctx:SmolangParser.FuncallContext):
        pass


    # Enter a parse tree produced by SmolangParser#show_func.
    def enterShow_func(self, ctx:SmolangParser.Show_funcContext):
        pass

    # Exit a parse tree produced by SmolangParser#show_func.
    def exitShow_func(self, ctx:SmolangParser.Show_funcContext):
        pass


    # Enter a parse tree produced by SmolangParser#read_func.
    def enterRead_func(self, ctx:SmolangParser.Read_funcContext):
        pass

    # Exit a parse tree produced by SmolangParser#read_func.
    def exitRead_func(self, ctx:SmolangParser.Read_funcContext):
        pass


    # Enter a parse tree produced by SmolangParser#custom_func.
    def enterCustom_func(self, ctx:SmolangParser.Custom_funcContext):
        pass

    # Exit a parse tree produced by SmolangParser#custom_func.
    def exitCustom_func(self, ctx:SmolangParser.Custom_funcContext):
        pass


    # Enter a parse tree produced by SmolangParser#global_assignment.
    def enterGlobal_assignment(self, ctx:SmolangParser.Global_assignmentContext):
        pass

    # Exit a parse tree produced by SmolangParser#global_assignment.
    def exitGlobal_assignment(self, ctx:SmolangParser.Global_assignmentContext):
        pass


    # Enter a parse tree produced by SmolangParser#assignment.
    def enterAssignment(self, ctx:SmolangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SmolangParser#assignment.
    def exitAssignment(self, ctx:SmolangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SmolangParser#value.
    def enterValue(self, ctx:SmolangParser.ValueContext):
        pass

    # Exit a parse tree produced by SmolangParser#value.
    def exitValue(self, ctx:SmolangParser.ValueContext):
        pass


    # Enter a parse tree produced by SmolangParser#list_value.
    def enterList_value(self, ctx:SmolangParser.List_valueContext):
        pass

    # Exit a parse tree produced by SmolangParser#list_value.
    def exitList_value(self, ctx:SmolangParser.List_valueContext):
        pass


    # Enter a parse tree produced by SmolangParser#arithmetic.
    def enterArithmetic(self, ctx:SmolangParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by SmolangParser#arithmetic.
    def exitArithmetic(self, ctx:SmolangParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by SmolangParser#ar_value.
    def enterAr_value(self, ctx:SmolangParser.Ar_valueContext):
        pass

    # Exit a parse tree produced by SmolangParser#ar_value.
    def exitAr_value(self, ctx:SmolangParser.Ar_valueContext):
        pass


    # Enter a parse tree produced by SmolangParser#typ.
    def enterTyp(self, ctx:SmolangParser.TypContext):
        pass

    # Exit a parse tree produced by SmolangParser#typ.
    def exitTyp(self, ctx:SmolangParser.TypContext):
        pass



del SmolangParser