from antlr4 import CommonTokenStream, StdinStream, ParseTreeWalker
from SmolangLexer import SmolangLexer
from SmolangParser import SmolangParser
from SmolangPartialListener import SmolangPartialListener, VariableError, UnsupportedOperationError
from SmolangFunction import SmolangFunction
import sys

# vars { id: (no_change, type) }
# consts { (id, no_change): value}
# strings { id: (no_change, value) }
# lists {id: (no_change, type, length)}



class SmolangFullListener(SmolangPartialListener):
    def __init__(self):
        super().__init__()

    def enterFunc_declaration(self, ctx:SmolangParser.Func_declarationContext):
        fun_name = ctx.getChild(2).getText()
        for f in self.functions:
            if f.name == fun_name:
                raise Exception('Redefinition of function ' + fun_name + ' at name ' + str(self.current_line))
        self.functions.append(SmolangFunction(fun_name))
        self.current = self.functions[-1]
        typeof = ctx.getChild(1).getText()
        if typeof == 'real':
            self.functions[-1].type = 'double'
            header = '\ndefine double @' + fun_name + '('
        elif typeof == 'int':
            self.functions[-1].type = typeof
            header = '\ndefine i32 @' + fun_name + '('
        else:
            header = '\ndefine void @' + fun_name + '('

        index = 4
        while ctx.getChild(index).getText() != ')':
            if index != 4:
                index += 1
            name = ctx.getChild(index + 1).getText()
            if ctx.getChild(index).getText() == 'int':
                typeof = 'int'
                header += 'i32 %' + name + ', '
                self.current.code += "\n  %" + name + '.0' + ' = alloca i32'
                self.current.code += "\n  store i32 %" + name + ", i32* %" + name + '.0'
            elif ctx.getChild(index).getText() == 'real':
                typeof = 'double'
                header += 'double %' + name + ', '
                self.current.code += "\n  %" + name + '.0' + ' = alloca double'
                self.current.code += "\n  store double %" + name + ", double* %" + name + '.0'
            else:
                raise Exception('Bad variable type at line ' + str(self.current_line))
            self.current.vars[name] = (0, typeof)
            self.current.param_types.append(typeof)
            index += 2
        
        header = header[:len(header) - 2] + ') {'
        self.current.code = header + self.current.code
      

    def exitFunc_declaration(self, ctx:SmolangParser.Func_declarationContext):
        if self.current.type == 'void':
            self.current.code += '\n  ret void\n}\n'
        elif self.current.type == 'double':
            self.current.code += '\n  ret double 0.0\n}\n'
        elif self.current.type == 'int':
            self.current.code += '\n  ret i32 0\n}\n'
        self.current = self.functions[0]

    def exitReturn_st(self, ctx:SmolangParser.Return_stContext):
        if ctx.value().ID() != None:
            id = str(ctx.value().ID())
            typeof = self.checkID(id)
            if typeof == 'int':
                if self.current.type == typeof:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* %' + id + '.' + str(self.current.vars[id][0])
                    self.current.code += "\n  ret i32 %sup" + str(self.var_counter)
                    self.var_counter = self.var_counter + 1
                else:
                    raise Exception('Bad variable type at line ' + str(self.current_line))

            elif typeof == 'double':
                if self.current.type == typeof:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* %' + id + '.' + str(self.current.vars[id][0])
                    self.current.code += "\n  ret double %sup" + str(self.var_counter)
                    self.var_counter = self.var_counter + 1
                else:
                    raise Exception('Bad variable type at line ' + str(self.current_line))
            elif typeof == 'global':
                typeof = self.checkID(id, glob=True)
                if typeof == 'int':
                    if self.current.type == typeof:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* @global.' + id
                        self.current.code += "\n  ret i32 %sup" + str(self.var_counter)
                        self.var_counter = self.var_counter + 1
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))

                elif typeof == 'double':
                    if self.current.type == typeof:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* @global.' + id
                        self.current.code += "\n  ret double %sup" + str(self.var_counter)
                        self.var_counter = self.var_counter + 1
                else:
                    raise Exception('Bad variable type at line ' + str(self.current_line))
            elif type(typeof) == tuple and typeof[0] == 'list':
                if typeof[1] == 'int':
                    if self.current.type != typeof[1]:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
                    list_info = self.current.lists[id]
                    if ctx.value().INT() != None:
                        index = int(str(ctx.value().INT()))
                        if index < 0 or index >= list_info[2]:
                            raise IndexError('Bad index at line ' + str(self.current_line))

                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                        self.current.code += "\n  ret i32 %sup" + str(self.var_counter + 1)
                        self.var_counter = self.var_counter + 2
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
                elif typeof[1] == 'double':
                    if self.current.type != typeof[1]:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
                    list_info = self.current.lists[id]
                    if ctx.value().INT() != None:
                        index = int(str(ctx.value().INT()))
                        if index < 0 or index >= list_info[2]:
                            raise IndexError('Bad index at line ' + str(self.current_line))

                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                        self.current.code += "\n  ret double %sup" + str(self.var_counter + 1)
                        self.var_counter = self.var_counter + 2
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
            else:
                raise Exception('Bad variable type at line ' + str(self.current_line))
        elif ctx.value().arithmetic() != None:
            arithmetic = self.ar_stack.pop()
            if arithmetic[1] == 'int':
                if self.current.type == 'int':
                    self.current.code += "\n  ret i32 " + arithmetic[0]
                else:
                    raise Exception('Bad type at line ' + str(self.current_line))
            elif arithmetic[1] == 'double':
                if self.current.type == 'double':
                    self.current.code += "\n  ret double " + arithmetic[0]
                else:
                    raise Exception('Bad type at line ' + str(self.current_line))
        elif ctx.value().INT() != None:
            if self.current.type == 'int':
                self.current.code += "\n  ret i32 " + ctx.value().INT().getText()
            else:
                raise Exception('Bad type at line ' + str(self.current_line))
        elif ctx.value().REAL() != None:
            if self.current.type == 'double':
                self.current.code += "\n  ret double " + ctx.value().REAL().getText()
            else:
                raise Exception('Bad type at line ' + str(self.current_line))
        else:
            raise Exception('Bad variable type at line ' + str(self.current_line))

    def exitCustom_func(self, ctx:SmolangParser.Custom_funcContext):
        fun_name = ctx.getChild(0).getText()
        fun = None
        call = ""
        if fun_name == 'main':
            raise Exception('Forbidden function name at line ' + str(self.current_line))
        for f in self.functions:
            if fun_name == f.name:
                fun = f
        if fun == None:
            raise Exception('Unrecognised function name at line ' + str(self.current_line))
        if fun.type == 'int':
            call += "\n  %sup" + str(self.var_counter) + " = call i32 @" + fun_name + '('
            self.return_value = ('%sup' + str(self.var_counter), 'int')
            self.var_counter += 1
        elif fun.type == 'double':
            call += "\n  %sup" + str(self.var_counter) + " = call double @" + fun_name + '('
            self.return_value = ('%sup' + str(self.var_counter), 'double')
            self.var_counter += 1
        else:
            call += "\n  call void @" + fun_name + '('
            self.return_value = ('none', 'void')

        index = 2
        check_type_index = 0
        while ctx.getChild(index).getText() != ')':
            if index != 2:
                index += 1
            if ctx.getChild(index).ID() != None:
                id = str(ctx.getChild(index).ID())
                typeof = self.checkID(id)
                if typeof == 'int':
                    if fun.param_types[check_type_index] == typeof:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* %' + id + '.' + str(self.current.vars[id][0])
                        call += "i32 %sup" + str(self.var_counter) + ", "
                        self.var_counter = self.var_counter + 1
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))

                elif typeof == 'double':
                    if fun.param_types[check_type_index] == typeof:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* %' + id + '.' + str(self.current.vars[id][0])
                        call += "double %sup" + str(self.var_counter) + ", "
                        self.var_counter = self.var_counter + 1
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
                elif typeof == 'global':
                    typeof = self.checkID(id, glob=True)
                    if typeof == 'int':
                        if fun.param_types[check_type_index] == typeof:
                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* @global.' + id
                            call += "i32 %sup" + str(self.var_counter) + ", "
                            self.var_counter = self.var_counter + 1
                        else:
                            raise Exception('Bad variable type at line ' + str(self.current_line))

                    elif typeof == 'double':
                        if fun.param_types[check_type_index] == typeof:
                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* @global.' + id
                            call += "double %sup" + str(self.var_counter) + ", "
                            self.var_counter = self.var_counter + 1
                    else:
                        raise Exception('Bad variable type at line ' + str(self.current_line))
                elif type(typeof) == tuple and typeof[0] == 'list':
                    if typeof[1] == 'int':
                        if fun.param_types[check_type_index] != typeof[1]:
                            raise Exception('Bad variable type at line ' + str(self.current_line))
                        list_info = self.current.lists[id]
                        if ctx.getChild(index).INT() != None:
                            index = int(str(ctx.getChild(index).INT()))
                            if index < 0 or index >= list_info[2]:
                                raise IndexError('Bad index at line ' + str(self.current_line))

                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                            self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                            call += "i32 %sup" + str(self.var_counter + 1) + ", "
                            self.var_counter = self.var_counter + 2
                        else:
                            raise Exception('Bad variable type at line ' + str(self.current_line))
                    elif typeof[1] == 'double':
                        if fun.param_types[check_type_index] != typeof[1]:
                            raise Exception('Bad variable type at line ' + str(self.current_line))
                        list_info = self.current.lists[id]
                        if ctx.getChild(index).INT() != None:
                            index = int(str(ctx.getChild(index).INT()))
                            if index < 0 or index >= list_info[2]:
                                raise IndexError('Bad index at line ' + str(self.current_line))

                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                            self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                            call += "double %sup" + str(self.var_counter + 1) + ", "
                            self.var_counter = self.var_counter + 2
                else:
                    raise Exception('Bad variable type at line ' + str(self.current_line))
            elif ctx.getChild(index).arithmetic() != None:
                arithmetic = self.ar_stack.pop()
                if arithmetic[1] == 'int':
                    if fun.param_types[check_type_index] == 'int':
                        call += "i32 " + arithmetic[0] + ", "
                    else:
                        raise Exception('Bad type at line ' + str(self.current_line))
                elif arithmetic[1] == 'double':
                    if fun.param_types[check_type_index] == 'double':
                        call += "double " + arithmetic[0] + ", "
                    else:
                        raise Exception('Bad type at line ' + str(self.current_line))
            elif ctx.getChild(index).INT() != None:
                if fun.param_types[check_type_index] == 'int':
                    call += "i32 " + ctx.getChild(index).INT().getText() + ", "
                else:
                    raise Exception('Bad type at line ' + str(self.current_line))
            elif ctx.getChild(index).REAL() != None:
                if fun.param_types[check_type_index] == 'double':
                    call += "double " + ctx.getChild(index).REAL().getText() + ", "
                else:
                    raise Exception('Bad type at line ' + str(self.current_line))
            else:
                raise Exception('Bad variable type at line ' + str(self.current_line))

            index += 1
            check_type_index += 1
        
        self.current.code += call[:len(call) - 2] + ")"


    def exitCondition(self, ctx:SmolangParser.ConditionContext):
        left = self.conditionValue(ctx.getChild(0))
        right = self.conditionValue(ctx.getChild(2))
        operator = ctx.operator().getText()
        if left[1] != right[1]:
            raise TypeError('Comparing different types at line ' + str(self.current_line))
        if left[1] == 'int':
            if operator == '==':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp eq i32 ' + left[0] + ', ' + right[0]
            elif operator == '!=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp ne i32 ' + left[0] + ', ' + right[0]
            elif operator == '<':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp slt i32 ' + left[0] + ', ' + right[0]
            elif operator == '>':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp sgt i32 ' + left[0] + ', ' + right[0]
            elif operator == '>=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp sge i32 ' + left[0] + ', ' + right[0]
            elif operator == '<=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = icmp sle i32 ' + left[0] + ', ' + right[0]
        else:
            if operator == '==':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp oeq double ' + left[0] + ', ' + right[0]
            elif operator == '!=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp one double ' + left[0] + ', ' + right[0]
            elif operator == '<':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp olt double ' + left[0] + ', ' + right[0]
            elif operator == '>':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp ogt double ' + left[0] + ', ' + right[0]
            elif operator == '>=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp oge double ' + left[0] + ', ' + right[0]
            elif operator == '<=':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = fcmp ole double ' + left[0] + ', ' + right[0]
        condition = '%sup' + str(self.var_counter)
        self.var_counter += 1
        if self.instruction_stack[-1]['if_st']:
            self.current.code += "\n  br i1 " + condition + ', label %L' + str(self.instruction_stack[-1]['flags'][0]) + ', label %L' + str(self.instruction_stack[-1]['flags'][1])
        elif self.instruction_stack[-1]['while_st']:
            self.current.code += "\n  br i1 " + condition + ', label %L' + str(self.instruction_stack[-1]['flags'][1]) + ', label %L' + str(self.instruction_stack[-1]['flags'][2])

    def enterIf_st(self, ctx:SmolangParser.If_stContext):    
        self.instruction_stack.append({
            'if_st' : True,
            'else_st' : False,
            'while_st' : False,
            'flags' : [self.flag_counter, self.flag_counter + 1]
        })
        self.flag_counter += 2
        if ctx.getChildCount() > 5:
            self.instruction_stack[-1]['else_st'] = True
            self.instruction_stack[-1]['flags'].append(self.flag_counter)
            self.flag_counter += 1

    def exitIf_st(self, ctx:SmolangParser.If_stContext):
        self.current.code += "\nL" + str(self.instruction_stack[-1]['flags'][-1]) + ':'
        self.instruction_stack.pop()

    def enterWhile_st(self, ctx:SmolangParser.While_stContext):
        self.instruction_stack.append({
            'if_st' : False,
            'else_st' : False,
            'while_st' : True,
            'flags' : [self.flag_counter, self.flag_counter + 1, self.flag_counter + 2]
        })
        self.flag_counter += 3
        self.current.code += "\n  br label %L" + str(self.instruction_stack[-1]['flags'][0])
        self.current.code += "\nL" + str(self.instruction_stack[-1]['flags'][0]) + ':'
        

    def exitWhile_st(self, ctx:SmolangParser.While_stContext):
        self.current.code += "\nL" + str(self.instruction_stack[-1]['flags'][-1]) + ':'
        self.instruction_stack.pop()

    def enterCodeblock(self, ctx:SmolangParser.CodeblockContext):
        if len(self.instruction_stack) == 0:
            return
        if self.instruction_stack[-1]['if_st']:
            self.current.code += "\nL" + str(self.instruction_stack[-1]['flags'][0]) + ':'
        elif self.instruction_stack[-1]['else_st'] or self.instruction_stack[-1]['while_st']:
            self.current.code += "\nL" + str(self.instruction_stack[-1]['flags'][1]) + ':'
            

    def exitCodeblock(self, ctx:SmolangParser.CodeblockContext):
        if len(self.instruction_stack) == 0:
            return
        if self.instruction_stack[-1]['if_st']:
            self.current.code += "\n  br label %L" + str(self.instruction_stack[-1]['flags'][-1])
            self.instruction_stack[-1]['if_st'] = False
        elif self.instruction_stack[-1]['else_st']:
            self.current.code += "\n  br label %L" + str(self.instruction_stack[-1]['flags'][-1])
        elif self.instruction_stack[-1]['while_st']:
            self.current.code += "\n  br label %L" + str(self.instruction_stack[-1]['flags'][0])


    def exitShow_func(self, ctx: SmolangParser.Show_funcContext):
        declaration = "i32 @printf(i8*, ...)"
        if declaration not in self.decs:
            self.decs.append(declaration)
        if ctx.value().ID() != None:
            id = str(ctx.value().ID())
            typeof = self.checkID(id)
            
            if typeof == 'int':
                if ('', 'i32') not in self.consts.keys():
                    self.consts[('', 'i32')] = " = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n"
                    self.code_up += '@.i32 = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n'
                
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0'
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %' + id + '.' + str(self.current.vars[id][0])
                self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                    str(self.var_counter) + ", i32 %sup" + str(self.var_counter + 1) + ")"
                self.var_counter = self.var_counter + 2

            elif typeof == 'double':
                if ('', 'double') not in self.consts.keys():
                    self.consts[('', 'double')] = " = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n"
                    self.code_up += '@.double = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n'

                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0'
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %' + id + '.' + str(self.current.vars[id][0])
                self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                    str(self.var_counter) + ", double %sup" + str(self.var_counter + 1) + ")"
                self.var_counter = self.var_counter + 2

            elif typeof == 'string':
                value = self.current.strings[id][1]
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(len(
                    value) + 2) + ' x i8], [' + str(len(value) + 2) + ' x i8]* @' + self.current.name + '.' + id + '.' + str(self.current.strings[id][0]) + ", i32 0, i32 0"
                self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                    str(self.var_counter) + ")"
                self.var_counter = self.var_counter + 1

            elif type(typeof) == tuple and typeof[0] == 'list':
                if typeof[1] == 'int':
                    if ('', 'i32') not in self.consts.keys():
                        self.consts[('', 'i32')] = " = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n"
                        self.code_up += '@.i32 = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n'

                    list_info = self.current.lists[id]
                    if ctx.value().INT() != None:
                        index = int(str(ctx.value().INT()))
                        if index < 0 or index >= list_info[2]:
                            raise IndexError('Bad index at line ' + str(self.current_line))

                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                        self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0'
                        self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                            str(self.var_counter + 2) + ", i32 %sup" + str(self.var_counter + 1) + ")"
                        self.var_counter = self.var_counter + 3
                    else:
                        if ('', 'i32single') not in self.consts.keys():
                            self.consts[('', 'i32single')] = " = private unnamed_addr constant [4 x i8] c\"%d \\00\"\n"
                            self.code_up += '@.i32single = private unnamed_addr constant [4 x i8] c\"%d \\00\"\n'

                        for i in range(0, list_info[2] - 1):
                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(i)
                            self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                            self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32single, i32 0, i32 0'
                            self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                                str(self.var_counter + 2) + ", i32 %sup" + str(self.var_counter + 1) + ")"
                            self.var_counter = self.var_counter + 3
                        
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(list_info[2] - 1)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                        self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0'
                        self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                            str(self.var_counter + 2) + ", i32 %sup" + str(self.var_counter + 1) + ")"
                        self.var_counter = self.var_counter + 3



                elif typeof[1] == 'double':
                    if ('', 'double') not in self.consts.keys():
                        self.consts[('', 'double')] = " = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n"
                        self.code_up += '@.double = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n'

                    list_info = self.current.lists[id]
                    if ctx.value().INT() != None:
                        index = int(str(ctx.value().INT()))
                        if index < 0 or index >= list_info[2]:
                            raise IndexError('Bad index at line ' + str(self.current_line))

                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                        self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0'
                        self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                            str(self.var_counter + 2) + ", double %sup" + str(self.var_counter + 1) + ")"
                        self.var_counter = self.var_counter + 3
                    else:
                        if ('', 'doublesingle') not in self.consts.keys():
                            self.consts[('', 'doublesingle')] = " = private unnamed_addr constant [5 x i8] c\"%lf \\00\"\n"
                            self.code_up += '@.doublesingle = private unnamed_addr constant [5 x i8] c\"%lf \\00\"\n'

                        for i in range(0, list_info[2] - 1):
                            self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(i)
                            self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                            self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.doublesingle, i32 0, i32 0'
                            self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                                str(self.var_counter + 2) + ", double %sup" + str(self.var_counter + 1) + ")"
                            self.var_counter = self.var_counter + 3
                        
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(list_info[2] - 1)
                        self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                        self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0'
                        self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                            str(self.var_counter + 2) + ", double %sup" + str(self.var_counter + 1) + ")"
                        self.var_counter = self.var_counter + 3

            elif typeof == 'global':
                typeof = self.checkID(id, glob=True)
                if typeof == 'int':
                    if ('', 'i32') not in self.consts.keys():
                        self.consts[('', 'i32')] = " = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n"
                        self.code_up += '@.i32 = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n'
                    
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0'
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* @global.' + id
                    self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                        str(self.var_counter) + ", i32 %sup" + str(self.var_counter + 1) + ")"
                    self.var_counter = self.var_counter + 2
                elif typeof == 'double':
                    if ('', 'double') not in self.consts.keys():
                        self.consts[('', 'double')] = " = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n"
                        self.code_up += '@.double = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n'

                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0'
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* @global.' + id
                    self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                        str(self.var_counter) + ", double %sup" + str(self.var_counter + 1) + ")"
                    self.var_counter = self.var_counter + 2


                    
                
        elif ctx.value().STRING() != None or ctx.value().INT() != None or ctx.value().REAL() != None:
            if ctx.value().STRING() != None:
                value = ctx.getChild(2).getText()[1:len(ctx.getChild(2).getText())-1]
            else:
                value = ctx.getChild(2).getText()              
            if value in self.consts.values():
                for k, v in self.consts.items():
                    if v == value:
                        var = k
            else:
                var = ("cnst", str(len(self.consts.keys())))
                self.consts[var] = value
                self.code_up += '@' + var[0] + '.' + str(var[1]) + " = private global [" + str(len(value) + 2) + " x i8] c\"" + value + "\\0A\\00\" \n"
            self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(len(
                value) + 2) + ' x i8], [' + str(len(value) + 2) + ' x i8]* @' + var[0] + '.' + str(var[1]) + ", i32 0, i32 0"
            self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                str(self.var_counter) + ")"
            self.var_counter = self.var_counter + 1
                

        elif ctx.value().arithmetic() != None:
            arithmetic = self.ar_stack.pop()
            if arithmetic[1] == 'int':
                if ('', 'i32') not in self.consts.keys():
                    self.consts[('', 'i32')] = " = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n"
                    self.code_up += "@.i32 = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\"\n"

                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [4 x i8], [4 x i8]* @.i32, i32 0, i32 0'
                self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                    str(self.var_counter) + ", i32 " + arithmetic[0] + ")"
                self.var_counter = self.var_counter + 1
            elif arithmetic[1] == 'double':
                if ('', 'double') not in self.consts.keys():
                    self.consts[('', 'double')] = " = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n"
                    self.code_up += "@.double = private unnamed_addr constant [5 x i8] c\"%lf\\0A\\00\"\n"
                
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [5 x i8], [5 x i8]* @.double, i32 0, i32 0'
                self.current.code += "\n  call i32 (i8*, ...) @printf(i8* %sup" + \
                    str(self.var_counter) + ", double " + arithmetic[0] + ")"
                self.var_counter = self.var_counter + 1
            return
    

    def exitProgram(self, ctx: SmolangParser.ProgramContext):
        declarations = ""
        for d in self.decs:
            declarations = declarations + "declare " + d + "\n"
        declarations += "\n"
        code = declarations + self.code_up
        for i in range(1, len(self.functions)):
            code += self.functions[i].code
        code += '\ndefine i32 @main() {' + self.current.code + "\n  ret i32 1\n}"
        with open('program.ll', 'w') as f:
            f.write(code)
        print(code)



def main():
    code = sys.argv[1] if len(sys.argv) > 1 else 's'
    if code == 's':
        code = StdinStream()
    else:
        with open(code, 'r') as sys.stdin:
            code = StdinStream()
        sys.stdin = sys.__stdin__
    print(code)
    print('\n')
    lexer = SmolangLexer(code)
    stream = CommonTokenStream(lexer)
    parser = SmolangParser(stream)
    tree = parser.program()
    printer = SmolangFullListener()
    try:
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
