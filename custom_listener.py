from gen.evmTestListener import evmTestListener
from gen.evmTestParser import evmTestParser

class evmTestCustomListener(evmTestListener):

    def __init__(self):
        self.variables = {}
        self.functions = {}


    def error(self, msg, ctx):
        line = ctx.start.line
        col = ctx.start.column
        # self.errors.append(f"[line {line}:{col}] SemanticError: {msg}")
        # print(self.errors[-1])
        raise ValueError(f"[line {line}:{col}] SemanticError: {msg}")


    def exitVariable_declaration(self, ctx: evmTestParser.Variable_declarationContext):
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        value = ctx.getChild(3).value
        value_type = ctx.getChild(3).type

        if var_name in self.variables:
            self.error(f"Variable '{var_name}' is already declared.", ctx)
            return

        if not self.types_compatible(var_type, value_type):
            self.error(f"Cannot assign '{value_type}' to '{var_type}' variable '{var_name}'.", ctx)

        ctx.value = value

        self.variables[var_name] = { "type": var_type, "value": value }

    def exitAssignment(self, ctx: evmTestParser.AssignmentContext):
        var_name = ctx.getChild(0).getText()

        if var_name not in self.variables:
            self.error(f"Undefined variable '{var_name}'", ctx)
            return

        expr_ctx = ctx.getChild(2)
        new_value = expr_ctx.value
        new_type = expr_ctx.type

        var_info = self.variables[var_name]

        if not self.types_compatible(var_info['type'], new_type):
            self.error(f"Type mismatch: cannot assign {new_type} to {var_info['type']}", ctx)
            return

        self.variables[var_name]['value'] = new_value

    def exitValue(self, ctx: evmTestParser.ValueContext):
        if ctx.INT_LITERAL():
            ctx.type = "int"
            ctx.value = int(ctx.getText())
        elif ctx.FLOAT_LITERAL():
            ctx.type = "float"
            ctx.value = float(ctx.getText())
        elif ctx.STRING_LITERAL():
            ctx.type = "string"
            ctx.value = ctx.getText()

    def exitId(self, ctx: evmTestParser.IdContext):
        if isinstance(ctx.parentCtx, evmTestParser.Variable_declarationContext):
            return
        if isinstance(ctx.parentCtx, evmTestParser.Variable_signatureContext):
            return
        if isinstance(ctx.parentCtx, evmTestParser.Function_declaraionContext):
            return

        name = ctx.getText()
        if name not in self.variables:
            self.error(f"Undefined variable '{name}'.", ctx)

        var_info = self.variables.get(name)
        if var_info:
            ctx.type = var_info["type"]
            ctx.value = var_info.get("value")

    def exitTerm(self, ctx: evmTestParser.TermContext):
        if ctx.getChildCount() == 3:

            first_type = ctx.getChild(0).type
            second_type = ctx.getChild(2).type
            if not self.types_mathematical_compatible(first_type, second_type):
                self.error("Both operands must be numeric", ctx)
                return

            if first_type == 'float' or second_type == 'float':
                ctx.type = 'float'
            else:
                ctx.type = 'int'

            if ctx.getChild(1).getText() == '/':
                if ctx.getChild(2).value == 0:
                    self.error("Division by zero.", ctx)
                    return
                ctx.value = ctx.getChild(0).value / ctx.getChild(2).value
            else:
                ctx.value = ctx.getChild(0).value * ctx.getChild(2).value

        else:
            ctx.value = ctx.getChild(0).value
            ctx.type = ctx.getChild(0).type


    def exitExpression(self, ctx: evmTestParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            first_type = ctx.getChild(0).type
            second_type = ctx.getChild(2).type
            if not self.types_mathematical_compatible(first_type, second_type):
                self.error("Both operands must be numeric", ctx)
                return

            if first_type == 'float' or second_type == 'float':
                ctx.type = 'float'
            else:
                ctx.type = 'int'

            if ctx.getChild(1).getText() == '+':
                ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
            else:
                ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
        else:
            ctx.value = ctx.getChild(0).value
            ctx.type = ctx.getChild(0).type

    def exitFactor(self, ctx:evmTestParser.FactorContext):
        # '(' expression ')'
        if ctx.getChildCount() == 3:
            value = ctx.getChild(1).value
            value_type = ctx.getChild(1).type
            if value_type not in ['int', 'float']:
                self.error("Mathematical operands should be numeric", ctx)
                return
            ctx.value = value
            ctx.type = value_type
        # SUB factor
        elif ctx.getChildCount() == 2:
            value = ctx.getChild(1).value * -1
            value_type = ctx.getChild(1).type
            if value_type not in ['int', 'float']:
                self.error("Mathematical operands should be numeric", ctx)
                return
            ctx.value = value
            ctx.type = value_type
        else:
            value = ctx.getChild(0).value
            value_type = ctx.getChild(0).type
            # Commented to accept strings
            # if value_type not in ['int', 'float']:
            #     self.error("Mathematical operands should be numeric", ctx)
            #     return
            ctx.value = value
            ctx.type = value_type

    def exitReturn_statement(self, ctx: evmTestParser.Return_statementContext):
        # return ;
        if ctx.getChildCount() == 2:
            ctx.type = "void"
            ctx.value = None
            return

        # return something;
        returned_ctx = ctx.getChild(1)
        ctx.type = returned_ctx.type
        ctx.value = returned_ctx.value

    def enterFunction_body(self, ctx: evmTestParser.Function_bodyContext):
        ctx.has_return = False
        ctx.return_type = None
        ctx.return_value = None

    def exitFunction_body(self, ctx: evmTestParser.Function_bodyContext):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, evmTestParser.Return_statementContext):
                ctx.has_return = True
                ctx.return_type = child.type
                ctx.return_value = child.value
                break

    def exitFunction_type(self, ctx: evmTestParser.Function_typeContext):
        if ctx.VOID():
            ctx.type = "void"
        elif ctx.INT():
            ctx.type = "int"
        elif ctx.FLOAT():
            ctx.type = "float"
        elif ctx.STRING():
            ctx.type = "string"

    def exitFunction_declaraion(self, ctx: evmTestParser.Function_declaraionContext):
        func_type = ctx.getChild(0).type
        func_name = ctx.getChild(2).getText()
        body_ctx = ctx.getChild(ctx.getChildCount() - 1)

        params_list = {}
        params_ctx = ctx.params()
        if params_ctx:
            for sig in params_ctx.variable_signature():
                t = sig.getChild(0).getText()
                n = sig.getChild(1).getText()
                self.variables[n] = {"type": t, "value": None}
                params_list[n] = t

        if func_name in self.functions:
            self.error(f"Function '{func_name}' is already declared.", ctx)
            return

        if func_name in self.variables:
            self.error(f"Function name '{func_name}' conflicts with a variable name.", ctx)
            return

        # Checking function type with returned type
        if func_type == "void":
            if body_ctx.has_return and body_ctx.return_type != "void":
                self.error(f"Void function '{func_name}' cannot return a value.", ctx)

        else:
            if not body_ctx.has_return:
                self.error(f"Non-void function '{func_name}' must return a value.", ctx)
                return

            if body_ctx.return_type == "void":
                self.error(f"Function '{func_name}' must return '{func_type}', not void.", ctx)
                return

            if not self.types_compatible(func_type, body_ctx.return_type):
                self.error(
                    f"Function '{func_name}' returns '{body_ctx.return_type}' but expected '{func_type}'.", ctx)
                return

        self.functions[func_name] = { "type": func_type, "params": params_list }

    def exitFor_statement(self, ctx: evmTestParser.For_statementContext):
        var_decl = ctx.getChild(2)
        var_name = var_decl.getChild(1).getText()
        # Using this later :) :
        var_value = var_decl.getChild(3).getText()

        if var_name in self.variables:
            del self.variables[var_name]

    def enterSwitch_statement(self, ctx: evmTestParser.Switch_statementContext):
        self.case_values = set()

    def exitSwitch_statement(self, ctx: evmTestParser.Switch_statementContext):
        expr = ctx.getChild(2)
        switch_type = getattr(expr, "type", None)

        for case in ctx.case_statement():
            case_val = case.getChild(2)
            case_type = None

            if case_val.INT_LITERAL():
                case_type = "int"
            elif case_val.FLOAT_LITERAL():
                case_type = "float"
            elif case_val.STRING_LITERAL():
                case_type = "string"

            if switch_type and case_type and switch_type != case_type:
                self.error("Case type does not match switch expression type.", case)

    def types_compatible(self, t1, t2):
        if t1 == t2:
            return True
        elif t1 == "float" and t2 == "int":
            return True
        return False

    def types_mathematical_compatible(self, t1, t2):
        numeric = {"int", "float"}
        if t1 in numeric and t2 in numeric:
            return True
        return False
