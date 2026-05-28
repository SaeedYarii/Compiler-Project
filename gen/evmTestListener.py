# Generated from C:/Users/Asus/Desktop/Compiler/TA/GIT/evmTest.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .evmTestParser import evmTestParser
else:
    from evmTestParser import evmTestParser

# This class defines a complete listener for a parse tree produced by evmTestParser.
class evmTestListener(ParseTreeListener):

    # Enter a parse tree produced by evmTestParser#program.
    def enterProgram(self, ctx:evmTestParser.ProgramContext):
        pass

    # Exit a parse tree produced by evmTestParser#program.
    def exitProgram(self, ctx:evmTestParser.ProgramContext):
        pass


    # Enter a parse tree produced by evmTestParser#statements.
    def enterStatements(self, ctx:evmTestParser.StatementsContext):
        pass

    # Exit a parse tree produced by evmTestParser#statements.
    def exitStatements(self, ctx:evmTestParser.StatementsContext):
        pass


    # Enter a parse tree produced by evmTestParser#statement.
    def enterStatement(self, ctx:evmTestParser.StatementContext):
        pass

    # Exit a parse tree produced by evmTestParser#statement.
    def exitStatement(self, ctx:evmTestParser.StatementContext):
        pass


    # Enter a parse tree produced by evmTestParser#variable_declaration.
    def enterVariable_declaration(self, ctx:evmTestParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by evmTestParser#variable_declaration.
    def exitVariable_declaration(self, ctx:evmTestParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by evmTestParser#variable_type.
    def enterVariable_type(self, ctx:evmTestParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by evmTestParser#variable_type.
    def exitVariable_type(self, ctx:evmTestParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by evmTestParser#id.
    def enterId(self, ctx:evmTestParser.IdContext):
        pass

    # Exit a parse tree produced by evmTestParser#id.
    def exitId(self, ctx:evmTestParser.IdContext):
        pass


    # Enter a parse tree produced by evmTestParser#value.
    def enterValue(self, ctx:evmTestParser.ValueContext):
        pass

    # Exit a parse tree produced by evmTestParser#value.
    def exitValue(self, ctx:evmTestParser.ValueContext):
        pass


    # Enter a parse tree produced by evmTestParser#expression.
    def enterExpression(self, ctx:evmTestParser.ExpressionContext):
        pass

    # Exit a parse tree produced by evmTestParser#expression.
    def exitExpression(self, ctx:evmTestParser.ExpressionContext):
        pass


    # Enter a parse tree produced by evmTestParser#term.
    def enterTerm(self, ctx:evmTestParser.TermContext):
        pass

    # Exit a parse tree produced by evmTestParser#term.
    def exitTerm(self, ctx:evmTestParser.TermContext):
        pass


    # Enter a parse tree produced by evmTestParser#factor.
    def enterFactor(self, ctx:evmTestParser.FactorContext):
        pass

    # Exit a parse tree produced by evmTestParser#factor.
    def exitFactor(self, ctx:evmTestParser.FactorContext):
        pass


    # Enter a parse tree produced by evmTestParser#assignment.
    def enterAssignment(self, ctx:evmTestParser.AssignmentContext):
        pass

    # Exit a parse tree produced by evmTestParser#assignment.
    def exitAssignment(self, ctx:evmTestParser.AssignmentContext):
        pass


    # Enter a parse tree produced by evmTestParser#function_declaraion.
    def enterFunction_declaraion(self, ctx:evmTestParser.Function_declaraionContext):
        pass

    # Exit a parse tree produced by evmTestParser#function_declaraion.
    def exitFunction_declaraion(self, ctx:evmTestParser.Function_declaraionContext):
        pass


    # Enter a parse tree produced by evmTestParser#function_type.
    def enterFunction_type(self, ctx:evmTestParser.Function_typeContext):
        pass

    # Exit a parse tree produced by evmTestParser#function_type.
    def exitFunction_type(self, ctx:evmTestParser.Function_typeContext):
        pass


    # Enter a parse tree produced by evmTestParser#params.
    def enterParams(self, ctx:evmTestParser.ParamsContext):
        pass

    # Exit a parse tree produced by evmTestParser#params.
    def exitParams(self, ctx:evmTestParser.ParamsContext):
        pass


    # Enter a parse tree produced by evmTestParser#variable_signature.
    def enterVariable_signature(self, ctx:evmTestParser.Variable_signatureContext):
        pass

    # Exit a parse tree produced by evmTestParser#variable_signature.
    def exitVariable_signature(self, ctx:evmTestParser.Variable_signatureContext):
        pass


    # Enter a parse tree produced by evmTestParser#function_body.
    def enterFunction_body(self, ctx:evmTestParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by evmTestParser#function_body.
    def exitFunction_body(self, ctx:evmTestParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by evmTestParser#return_statement.
    def enterReturn_statement(self, ctx:evmTestParser.Return_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#return_statement.
    def exitReturn_statement(self, ctx:evmTestParser.Return_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#if_statement.
    def enterIf_statement(self, ctx:evmTestParser.If_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#if_statement.
    def exitIf_statement(self, ctx:evmTestParser.If_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#condition.
    def enterCondition(self, ctx:evmTestParser.ConditionContext):
        pass

    # Exit a parse tree produced by evmTestParser#condition.
    def exitCondition(self, ctx:evmTestParser.ConditionContext):
        pass


    # Enter a parse tree produced by evmTestParser#condition_and.
    def enterCondition_and(self, ctx:evmTestParser.Condition_andContext):
        pass

    # Exit a parse tree produced by evmTestParser#condition_and.
    def exitCondition_and(self, ctx:evmTestParser.Condition_andContext):
        pass


    # Enter a parse tree produced by evmTestParser#condition_compare.
    def enterCondition_compare(self, ctx:evmTestParser.Condition_compareContext):
        pass

    # Exit a parse tree produced by evmTestParser#condition_compare.
    def exitCondition_compare(self, ctx:evmTestParser.Condition_compareContext):
        pass


    # Enter a parse tree produced by evmTestParser#operation.
    def enterOperation(self, ctx:evmTestParser.OperationContext):
        pass

    # Exit a parse tree produced by evmTestParser#operation.
    def exitOperation(self, ctx:evmTestParser.OperationContext):
        pass


    # Enter a parse tree produced by evmTestParser#elsif_statement.
    def enterElsif_statement(self, ctx:evmTestParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#elsif_statement.
    def exitElsif_statement(self, ctx:evmTestParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#else_statement.
    def enterElse_statement(self, ctx:evmTestParser.Else_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#else_statement.
    def exitElse_statement(self, ctx:evmTestParser.Else_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#while_statement.
    def enterWhile_statement(self, ctx:evmTestParser.While_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#while_statement.
    def exitWhile_statement(self, ctx:evmTestParser.While_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#for_statement.
    def enterFor_statement(self, ctx:evmTestParser.For_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#for_statement.
    def exitFor_statement(self, ctx:evmTestParser.For_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#update.
    def enterUpdate(self, ctx:evmTestParser.UpdateContext):
        pass

    # Exit a parse tree produced by evmTestParser#update.
    def exitUpdate(self, ctx:evmTestParser.UpdateContext):
        pass


    # Enter a parse tree produced by evmTestParser#switch_statement.
    def enterSwitch_statement(self, ctx:evmTestParser.Switch_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#switch_statement.
    def exitSwitch_statement(self, ctx:evmTestParser.Switch_statementContext):
        pass


    # Enter a parse tree produced by evmTestParser#case_statement.
    def enterCase_statement(self, ctx:evmTestParser.Case_statementContext):
        pass

    # Exit a parse tree produced by evmTestParser#case_statement.
    def exitCase_statement(self, ctx:evmTestParser.Case_statementContext):
        pass



del evmTestParser