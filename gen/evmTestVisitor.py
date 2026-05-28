# Generated from C:/Users/Asus/Desktop/Compiler/TA/GIT/evmTest.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .evmTestParser import evmTestParser
else:
    from evmTestParser import evmTestParser

# This class defines a complete generic visitor for a parse tree produced by evmTestParser.

class evmTestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by evmTestParser#program.
    def visitProgram(self, ctx:evmTestParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#statements.
    def visitStatements(self, ctx:evmTestParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#statement.
    def visitStatement(self, ctx:evmTestParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#variable_declaration.
    def visitVariable_declaration(self, ctx:evmTestParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#variable_type.
    def visitVariable_type(self, ctx:evmTestParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#id.
    def visitId(self, ctx:evmTestParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#value.
    def visitValue(self, ctx:evmTestParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#expression.
    def visitExpression(self, ctx:evmTestParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#term.
    def visitTerm(self, ctx:evmTestParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#factor.
    def visitFactor(self, ctx:evmTestParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#assignment.
    def visitAssignment(self, ctx:evmTestParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#function_declaraion.
    def visitFunction_declaraion(self, ctx:evmTestParser.Function_declaraionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#function_type.
    def visitFunction_type(self, ctx:evmTestParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#params.
    def visitParams(self, ctx:evmTestParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#variable_signature.
    def visitVariable_signature(self, ctx:evmTestParser.Variable_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#function_body.
    def visitFunction_body(self, ctx:evmTestParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#return_statement.
    def visitReturn_statement(self, ctx:evmTestParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#if_statement.
    def visitIf_statement(self, ctx:evmTestParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#condition.
    def visitCondition(self, ctx:evmTestParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#condition_and.
    def visitCondition_and(self, ctx:evmTestParser.Condition_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#condition_compare.
    def visitCondition_compare(self, ctx:evmTestParser.Condition_compareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#operation.
    def visitOperation(self, ctx:evmTestParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#elsif_statement.
    def visitElsif_statement(self, ctx:evmTestParser.Elsif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#else_statement.
    def visitElse_statement(self, ctx:evmTestParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#while_statement.
    def visitWhile_statement(self, ctx:evmTestParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#for_statement.
    def visitFor_statement(self, ctx:evmTestParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#update.
    def visitUpdate(self, ctx:evmTestParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#switch_statement.
    def visitSwitch_statement(self, ctx:evmTestParser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by evmTestParser#case_statement.
    def visitCase_statement(self, ctx:evmTestParser.Case_statementContext):
        return self.visitChildren(ctx)



del evmTestParser