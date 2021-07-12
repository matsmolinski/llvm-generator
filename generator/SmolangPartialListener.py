from antlr4 import CommonTokenStream, StdinStream, ParseTreeWalker
from SmolangLexer import SmolangLexer
from SmolangListener import SmolangListener
from SmolangParser import SmolangParser
from SmolangFunction import SmolangFunction
import sys

class VariableError(Exception):
    pass

class UnsupportedOperationError(Exception):
    pass

class SmolangPartialListener(SmolangListener):
    def __init__(self):
        super().__init__()
        self.decs = []
        self.consts = {}
        self.global_vars = {}
        self.code_up = ""

        self.functions = [SmolangFunction('main')]
        self.functions[0].type = 'int'
        self.current = self.functions[0]

        self.var_counter = 0
        self.ar_stack = []
        self.return_value = None
        self.current_line = 1

        self.instruction_stack = []
        self.flag_counter = 0

    def checkID(self, id, typeof='any', glob=False):
        if glob:
            if id in self.global_vars.keys():
                return self.global_vars[id][1]
            else:
                return False
        if id in self.current.vars.keys():
            var_type = self.current.vars[id][1]
        else:
            if id in self.global_vars.keys():
                return 'global'
            raise VariableError(id + " is an unknown variable at line " + str(self.current_line))

        if typeof in ('any', 'number'):
            if var_type == 'int' or var_type == 'double':
                return self.current.vars[id][1]
        if typeof in ('any', 'string'):
            if var_type == 'string':
                return self.current.vars[id][1]
        if typeof in ('any', 'list'):
            if var_type == 'list':
                return self.current.vars[id][1], self.current.lists[id][1]
        raise VariableError(id + " is an invalid variable at line " + str(self.current_line))

    def exitLine(self, ctx:SmolangParser.LineContext):
        if str(ctx.NL()) != ';':
            self.current_line += 1

    def exitList_value(self, ctx:SmolangParser.List_valueContext):
        self.current.lists['!new_list'] = []

        for i in range (0, ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() != ',':
                self.current.lists['!new_list'].append(child.getText())

    def conditionValue(self, ctx:SmolangParser.ValueContext):
        if ctx.ID() != None:
            id = str(ctx.ID())
            if ctx.getChildCount() == 1:
                typeof = self.checkID(id, 'number')
                if typeof == 'global':
                    typeof = self.checkID(id, glob='true')
                    if typeof == 'int':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* @global.' + id
                    elif typeof == 'double':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* @global.' + id
                    else:
                        raise VariableError('Incorrect variable type at line ' + str(self.current_line))                  
                    self.var_counter = self.var_counter + 1
                    return ('%sup' + str(self.var_counter - 1), typeof)
                else:
                    typeof = self.checkID(id, 'number')
                    if typeof == 'int':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* %' + id + "." + str(self.current.vars[id][0])
                    elif typeof == 'double':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* %' + id + "." + str(self.current.vars[id][0])
                    self.var_counter = self.var_counter + 1
                    return ('%sup' + str(self.var_counter - 1), typeof)
                    
            else:
                self.checkID(id, 'list')
                list_info = self.current.lists[id]
                index = int(str(ctx.INT()))
                if index < 0 or index >= list_info[2]:
                    raise IndexError('Bad index at line ' + str(self.current_line))

                if list_info[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                    self.var_counter = self.var_counter + 2
                    return ('%sup' + str(self.var_counter - 1), 'int')

                elif list_info[1] == 'double':
                    
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                    self.var_counter = self.var_counter + 2
                    return ('%sup' + str(self.var_counter - 1), 'double')
                
        elif ctx.INT() != None:
            integer = str(ctx.INT())
            return (integer, 'int')

        elif ctx.REAL() != None:
            double = str(ctx.REAL())
            return (double, 'double')

        elif ctx.arithmetic() != None:
            return self.ar_stack.pop()


    def exitAr_value(self, ctx:SmolangParser.Ar_valueContext):
        if ctx.ID() != None:
            id = str(ctx.ID())
            if ctx.getChildCount() == 1:
                typeof = self.checkID(id, 'number')
                if typeof == 'global':
                    typeof = self.checkID(id, glob='true')
                    if typeof == 'int':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* @global.' + id
                    elif typeof == 'double':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* @global.' + id
                    else:
                        raise VariableError('Incorrect variable type at line ' + str(self.current_line))
                    self.ar_stack.append(('%sup' + str(self.var_counter), typeof))
                    self.var_counter = self.var_counter + 1
                else:
                    typeof = self.checkID(id, 'number')
                    if typeof == 'int':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load i32, i32* %' + id + "." + str(self.current.vars[id][0])
                    elif typeof == 'double':
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = load double, double* %' + id + "." + str(self.current.vars[id][0])
                    self.ar_stack.append(('%sup' + str(self.var_counter), self.current.vars[id][1]))
                    self.var_counter = self.var_counter + 1
            else:
                self.checkID(id, 'list')
                list_info = self.current.lists[id]
                index = int(str(ctx.INT()))
                if index < 0 or index >= list_info[2]:
                    raise IndexError('Bad index at line ' + str(self.current_line))

                if list_info[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                    self.ar_stack.append(('%sup' + str(self.var_counter + 1), 'int'))
                    self.var_counter = self.var_counter + 2

                elif list_info[1] == 'double':
                    
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                    self.ar_stack.append(('%sup' + str(self.var_counter + 1), 'double'))
                    self.var_counter = self.var_counter + 2
                

        elif ctx.INT() != None:
            integer = str(ctx.INT())
            self.ar_stack.append((integer, 'int'))

        elif ctx.REAL() != None:
            double = str(ctx.REAL())
            self.ar_stack.append((double, 'double'))
        else:
            if self.return_value[1] == 'int':
                self.ar_stack.append((self.return_value[0], 'int'))
            elif self.return_value[1] == 'double':
                self.ar_stack.append((self.return_value[0], 'double'))
            elif self.return_value[1] == 'void':
                raise Exception("Function does not return a value at line " + str(self.current_line))

    
    def exitArithmetic(self, ctx:SmolangParser.ArithmeticContext):
        if str(ctx.getChild(1)) == '+':
            right = self.ar_stack.pop()
            left = self.ar_stack.pop()
            if left[1] == 'int' and right[1] == 'int':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = add i32 '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'int'))
                self.var_counter = self.var_counter + 1
            else:
                if left[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + left[0] + ' to double'
                    left = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1
                if right[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + right[0] + ' to double'
                    right = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1

                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = fadd double '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'double'))
                self.var_counter = self.var_counter + 1

        elif str(ctx.getChild(1)) == '-':
            right = self.ar_stack.pop()
            left = self.ar_stack.pop()
            if left[1] == 'int' and right[1] == 'int':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = sub i32 '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'int'))
                self.var_counter = self.var_counter + 1
            else:
                if left[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + left[0] + ' to double'
                    left = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1
                if right[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + right[0] + ' to double'
                    right = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1

                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = fsub double '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'double'))
                self.var_counter = self.var_counter + 1

        elif str(ctx.getChild(1)) == '*':
            right = self.ar_stack.pop()
            left = self.ar_stack.pop()
            if left[1] == 'int' and right[1] == 'int':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = mul i32 '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'int'))
                self.var_counter = self.var_counter + 1
            else:
                if left[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + left[0] + ' to double'
                    left = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1
                if right[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + right[0] + ' to double'
                    right = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1

                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = fmul double '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'double'))
                self.var_counter = self.var_counter + 1

        elif str(ctx.getChild(1)) == '/':
            right = self.ar_stack.pop()
            left = self.ar_stack.pop()
            if left[1] == 'int' and right[1] == 'int':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = sdiv i32 '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'int'))
                self.var_counter = self.var_counter + 1
            else:
                if left[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + left[0] + ' to double'
                    left = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1
                if right[1] == 'int':
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = sitofp i32 ' + right[0] + ' to double'
                    right = ('%sup' + str(self.var_counter), 'double')
                    self.var_counter = self.var_counter + 1

                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = fdiv double '+ left[0] + ', ' + right[0]
                self.ar_stack.append(("%sup"+ str(self.var_counter), 'double'))
                self.var_counter = self.var_counter + 1
        else:
            pass

    def exitGlobal_assignment(self, ctx:SmolangParser.Global_assignmentContext):
        id = str(ctx.ID())
        if ctx.custom_func() != None:
            if self.return_value[1] == 'int':
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'int':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store i32 " + self.return_value[0] + ", i32* @global." + id
                else:
                    self.code_up += "@global." + id + " = global i32 0 \n"
                    self.current.code += "\n  store i32 " + self.return_value[0] + ", i32* @global." + id
                self.global_vars[id] = (0, 'int')
            elif self.return_value[1] == 'double':
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'double':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store double " + self.return_value[0] + ", double* @global." + id
                else:
                    self.code_up += "@global." + id + " = global double 0.0 \n"
                    self.current.code += "\n  store double " + self.return_value[0] + ", double* @global." + id
                self.global_vars[id] = (0, 'double')
            elif self.return_value[1] == 'void':
                raise Exception("Function does not return a value at line " + str(self.current_line))
        elif ctx.value().ID() != None and ctx.value().INT() == None:
            value_id = str(ctx.value().ID())
            typeof = self.checkID(value_id)
            if typeof == 'double':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load double, double* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'double':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* @global." + id
                else:
                    self.code_up += "@global." + id + " = global double 0 \n"
                    self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* @global." + id
                self.global_vars[id] = (0, 'double')
                self.var_counter = self.var_counter + 1

            elif typeof == 'int':
                self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load i32, i32* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'int':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* @global." + id
                else:
                    self.code_up += "@global." + id + " = global i32 0 \n"
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* @global." + id
                self.global_vars[id] = (0, 'int')
                self.var_counter = self.var_counter + 1

            elif typeof == 'global':                
                typeof = self.checkID(value_id, glob=True)
                if typeof == 'int':
                    self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load i32, i32* @global.' +  value_id
                    if id in self.current.vars.keys():
                        raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                    if id in self.global_vars.keys():
                        if self.global_vars[id][1] != 'int':
                            raise ValueError('Wrong value type at line '+ str(self.current_line))
                        self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* @global." + id
                    else:
                        self.code_up += "@global." + id + " = global i32 0 \n"
                        self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* @global." + id
                    self.global_vars[id] = (0, 'int')
                    self.var_counter = self.var_counter + 1
                elif typeof == 'double':
                    self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load double, double* @global.' +  value_id
                    if id in self.current.vars.keys():
                        raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                    if id in self.global_vars.keys():
                        if self.global_vars[id][1] != 'double':
                            raise ValueError('Wrong value type at line '+ str(self.current_line))
                        self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* @global." + id
                    else:
                        self.code_up += "@global." + id + " = global double 0 \n"
                        self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* @global." + id
                    self.global_vars[id] = (0, 'double')
                    self.var_counter = self.var_counter + 1
            

        elif ctx.value().INT() != None and ctx.value().ID() == None:
            value = str(ctx.value().INT())
            if id in self.current.vars.keys():
                raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
            if id in self.global_vars.keys():
                if self.global_vars[id][1] != 'int':
                    raise ValueError('Wrong value type at line '+ str(self.current_line))
                self.current.code += "\n  store i32 " + value + ", i32* @global." + id
            else:
                self.code_up += "@global." + id + " = global i32 " + value + " \n"
            self.global_vars[id] = (0, 'int')

        elif ctx.value().REAL() != None:
            value = str(ctx.value().REAL())
            if id in self.current.vars.keys():
                raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
            if id in self.global_vars.keys():
                if self.global_vars[id][1] != 'double':
                    raise ValueError('Wrong value type at line '+ str(self.current_line))
                self.current.code += "\n  store double " + value + ", double* @global." + id
            else:
                self.code_up += "@global." + id + " = global double " + value + " \n"
            self.global_vars[id] = (0, 'double')

        elif ctx.value().arithmetic() != None:
            arithmetic = self.ar_stack.pop()
            if arithmetic[1] == 'int':
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'int':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store i32 " + arithmetic[0] + ", i32* @global." + id
                else:
                    self.code_up += "@global." + id + " = global i32 0 \n"
                    self.current.code += "\n  store i32 " + arithmetic[0] + ", i32* @global." + id
                self.global_vars[id] = (0, 'int')
            else:
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'double':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store double " + arithmetic[0] + ", double* @global." + id
                else:
                    self.code_up += "@global." + id + " = global double 0.0 \n"
                    self.current.code += "\n  store double " + arithmetic[0] + ", double* @global." + id
                self.global_vars[id] = (0, 'double')


        elif ctx.value().INT() != None and ctx.value().ID() != None:
            id_val = str(ctx.value().ID())
            self.checkID(id_val, 'list')
            list_info_val = self.current.lists[id_val]
            index_val = int(str(ctx.value().INT()))
            if index_val < 0 or index_val >= list_info_val[2]:
                raise IndexError('Bad index in value at line ' + str(self.current_line))

            if list_info_val[1] == 'int':
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x i32], [' + str(list_info_val[2]) + ' x i32]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'int':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* @global." + id
                else:
                    self.code_up += "@global." + id + " = global i32 0 \n"
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* @global." + id
                self.global_vars[id] = (0, 'int')
                self.var_counter = self.var_counter + 2

            elif list_info_val[1] == 'double': 
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x double], [' + str(list_info_val[2]) + ' x double]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                if id in self.current.vars.keys():
                    raise VariableError('Cannot assign global variable with name ' + id + ' at line ' + str(self.current_line))
                if id in self.global_vars.keys():
                    if self.global_vars[id][1] != 'double':
                        raise ValueError('Wrong value type at line '+ str(self.current_line))
                    self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* @global." + id
                else:
                    self.code_up += "@global." + id + " = global double 0 \n"
                    self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* @global." + id
                self.global_vars[id] = (0, 'double')
                self.var_counter = self.var_counter + 2
        else:
            raise NotImplementedError('Cannot assign global variable at line ' + str(self.current_line))



    def exitAssignment(self, ctx: SmolangParser.AssignmentContext):
        id = str(ctx.ID())
        table_assignment = False

        if ctx.INT() != None:
            table_assignment = True
            index = int(str(ctx.INT()))
            typeof = self.checkID(id)
            if typeof != 'string':
                if type(typeof) == tuple and typeof[0] == 'list':
                    list_info = self.current.lists[id]
                    if index < 0 or index >= list_info[2]:
                        raise IndexError('Bad index at line ' + str(self.current_line))
                else:
                    raise IndexError('Variable cannot be indexed at line ' + str(self.current_line))

        if ctx.read_func() != None:
            declaration = "i32 @scanf(i8*, ...)"
            if declaration not in self.decs:
                self.decs.append(declaration)
            # only i32 working
            if ('', 'i32scanf') not in self.consts.keys():
                self.consts[('', 'i32scanf')] = " = private unnamed_addr constant [3 x i8] c\"%d\\00\"\n"
                self.code_up += '@.i32scanf = private unnamed_addr constant [3 x i8] c\"%d\\00\"\n'

            if not table_assignment:
                if id in self.current.vars.keys():
                    if self.current.vars[id][1] != 'int':
                        self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                        self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                else:
                    self.current.vars[id] = (0, 'int')
                    self.current.code += "\n  %" + id + '.0 = alloca i32'
            else:
                if typeof[0] != 'list' or list_info[1] != 'int':
                    raise UnsupportedOperationError('This operation is not implemented yet at line ' + str(self.current_line))

            if not table_assignment:
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = getelementptr inbounds [3 x i8], [3 x i8]* @.i32scanf, i32 0, i32 0'
                self.current.code += "\n  call i32 (i8*, ...) @scanf(i8* %sup" + \
                            str(self.var_counter + 1) + ", i32* %" + id + '.' + str(self.current.vars[id][0]) + ")"         
                self.var_counter = self.var_counter + 2
            else:
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = getelementptr inbounds [3 x i8], [3 x i8]* @.i32scanf, i32 0, i32 0'
                self.current.code += "\n  call i32 (i8*, ...) @scanf(i8* %sup" + \
                            str(self.var_counter + 1) + ", i32* %sup" + str(self.var_counter) + ")"
                self.var_counter = self.var_counter + 2

        elif ctx.custom_func() != None:
            if self.return_value[1] == 'int':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'int':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                    else:
                        self.current.vars[id] = (0, 'int')
                        self.current.code += "\n  %" + id + '.0 = alloca i32'
                else:
                    if typeof[0] != 'list' or list_info[1] != 'int':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  store i32 " + self.return_value[0] + ", i32* %" + id + '.' + str(self.current.vars[id][0])
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store i32 " + self.return_value[0] + ", i32* %sup" + str(self.var_counter)
                    self.var_counter = self.var_counter + 1
            elif self.return_value[1] == 'double':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'double':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                    else:
                        self.current.vars[id] = (0, 'double')
                        self.current.code += "\n  %" + id + '.0 = alloca double'
                else:
                    if typeof[0] != 'list' or list_info[1] != 'double':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  store double " + self.return_value[0] + ", double* %" + id + '.' + str(self.current.vars[id][0])
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store double " + self.return_value[0] + ", double* %sup" + str(self.var_counter)
                    self.var_counter = self.var_counter + 1
            elif self.return_value[1] == 'void':
                raise Exception("Function does not return a value at line " + str(self.current_line))


        elif ctx.value().STRING() != None:            
            if table_assignment:
                self.checkID(id, 'string')
                newest = self.current.strings[id][0]
                value = str(ctx.getChild(5).getText()[
                    1:len(ctx.getChild(5).getText())-1])
                if len(value) > 1:
                    raise TypeError("Cannot assign string as a char at line " + str(self.current_line))
                if index < 0 or index >= len(self.current.strings[id][1]):
                    raise IndexError('Bad index at line ' + str(self.current_line))
                char = value[0]
                self.current.strings[id] = (newest, self.current.strings[id][1][:index] + char + self.current.strings[id][1][index + 1:])
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(len(self.current.strings[id][1]) + 2) + ' x i8], [' + str(len(self.current.strings[id][1]) + 2) + ' x i8]* @' + self.current.name + '.' + id + '.' + str(newest) + ', i32 0, i32 ' + str(index)
                self.current.code += "\n  store i8 " + str(ord(char)) + ", i8* %sup" + str(self.var_counter) 
                self.var_counter = self.var_counter + 1

            else:
                value = ctx.getChild(2).getText()[
                    1:len(ctx.getChild(2).getText())-1]
                counter = 0
                if id in self.current.vars.keys():
                    counter = self.current.vars[id][0] + 1
                self.current.vars[id] = (counter, 'string')
                self.current.strings[id] = (counter, value)
                self.code_up += '@' + self.current.name + '.' + id + '.' + str(counter) + " = private global [" + str(len(value) + 2) + " x i8] c\"" + value + "\\0A\\00\" \n"
            
        elif ctx.value().INT() != None and ctx.value().ID() == None:
            value = str(ctx.value().INT())

            if not table_assignment:
                if id in self.current.vars.keys():
                    if self.current.vars[id][1] != 'int':
                        self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                        self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                else:
                    self.current.vars[id] = (0, 'int')
                    self.current.code += "\n  %" + id + '.0 = alloca i32'
            else:
                if typeof[0] != 'list' or list_info[1] != 'int':
                    raise TypeError('Wrong data type at line ' + str(self.current_line))

            if not table_assignment:
                self.current.code += "\n  store i32 " + value + ", i32* %" + id + '.' + str(self.current.vars[id][0])
            else:
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                self.current.code += "\n  store i32 " + value + ", i32* %sup" + str(self.var_counter) 
                self.var_counter = self.var_counter + 1 


        elif ctx.value().REAL() != None:
            value = str(ctx.value().REAL())
            if not table_assignment:
                if id in self.current.vars.keys():
                    if self.current.vars[id][1] != 'double':
                        self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                        self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                else:
                    self.current.vars[id] = (0, 'double')
                    self.current.code += "\n  %" + id + '.0 = alloca double'
            else:
                if typeof[0] != 'list' or list_info[1] != 'double':
                    raise TypeError('Wrong data type at line ' + str(self.current_line))

            if not table_assignment:
                self.current.code += "\n  store double " + value + ", double* %" + id + '.' + str(self.current.vars[id][0])
            else:
                self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                self.current.code += "\n  store double " + value + ", double* %sup" + str(self.var_counter) 
                self.var_counter = self.var_counter + 1 

        elif ctx.value().INT() == None and ctx.value().ID() != None:
            value_id = str(ctx.value().ID())
            typeof = self.checkID(value_id)
            if typeof == 'string':
                if table_assignment:
                    raise UnsupportedOperationError('String arrays not supported yet at line ' + str(self.current_line))
                counter = 0
                if id in self.current.vars.keys():
                    counter = self.current.vars[id][0] + 1
                self.current.vars[id] = (counter, 'string')
                new_var = (id, counter)
                newest = self.current.strings[value_id][0]
                var = (value_id, newest)
                value = self.current.strings[value_id][1]
                self.current.strings[id] = (counter, value)
                self.code_up += '@' + self.current.name + '.' + new_var[0] + '.' + str(new_var[1]) + " = private global [" + str(len(value) + 2) + " x i8] c\"" + value + "\\0A\\00\" \n"

            elif typeof == 'double':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'double':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                    else:
                        self.current.vars[id] = (0, 'double')
                        self.current.code += "\n  %" + id + '.0 = alloca double'
                else:
                    if list_info[1] != 'double':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load double, double* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                    self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* %" + id + '.' + str(self.current.vars[id][0])
                    self.var_counter = self.var_counter + 1
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup"+ str(self.var_counter + 1) + ' = load double, double* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                    self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* %sup" + str(self.var_counter) 
                    self.var_counter = self.var_counter + 2

            elif typeof == 'int':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'int':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                            self.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                    else:
                        self.current.vars[id] = (0, 'int')
                        self.current.code += "\n  %" + id + '.0 = alloca i32'
                else:
                    if list_info[1] != 'int':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load i32, i32* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* %" + id + '.' + str(self.current.vars[id][0])
                    self.var_counter = self.var_counter + 1
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  %sup"+ str(self.var_counter + 1) + ' = load i32, i32* %' +  value_id + '.' + str(self.current.vars[value_id][0])
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* %sup" + str(self.var_counter) 
                    self.var_counter = self.var_counter + 2
            elif typeof == 'list':
                if table_assignment:
                    raise TypeError("Cannot assign list to a list element at line " + str(self.current_line))
                else:
                    raise UnsupportedOperationError("List dynamic typing not supported yet at line " + str(self.current_line))
            elif typeof == 'global':                
                typeof = self.checkID(value_id, glob=True)
                if typeof == 'int':
                    if not table_assignment:
                        if id in self.current.vars.keys():
                            if self.current.vars[id][1] != 'int':
                                self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                                self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                        else:
                            self.current.vars[id] = (0, 'int')
                            self.current.code += "\n  %" + id + '.0 = alloca i32'
                    else:
                        if list_info[1] != 'int':
                            raise TypeError('Wrong data type at line ' + str(self.current_line))

                    if not table_assignment:
                        self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load i32, i32* @global.' +  value_id
                        self.current.code += "\n  store i32 %sup" + str(self.var_counter) + ", i32* %" + id + '.' + str(self.current.vars[id][0])
                        self.var_counter = self.var_counter + 1
                    else:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup"+ str(self.var_counter + 1) + ' = load i32, i32* @global.' +  value_id
                        self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* %sup" + str(self.var_counter) 
                        self.var_counter = self.var_counter + 2
                elif typeof == 'double':
                    if not table_assignment:                        
                        if id in self.current.vars.keys():
                            print(id)
                            if self.current.vars[id][1] != 'double':
                                self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                                self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                        else:                          
                            self.current.vars[id] = (0, 'double')
                            self.current.code += "\n  %" + id + '.0 = alloca double'
                    else:
                        if list_info[1] != 'double':
                            raise TypeError('Wrong data type at line ' + str(self.current_line))

                    if not table_assignment:
                        self.current.code += "\n  %sup"+ str(self.var_counter) + ' = load double, double* @global.' +  value_id
                        self.current.code += "\n  store double %sup" + str(self.var_counter) + ", double* %" + id + '.' + str(self.current.vars[id][0])
                        self.var_counter = self.var_counter + 1
                    else:
                        self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                        self.current.code += "\n  %sup"+ str(self.var_counter + 1) + ' = load double, double* @global.' +  value_id
                        self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* %sup" + str(self.var_counter) 
                        self.var_counter = self.var_counter + 2
            

        elif ctx.value().arithmetic() != None:
            arithmetic = self.ar_stack.pop()
            if arithmetic[1] == 'int':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'int':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                    else:
                        self.current.vars[id] = (0, 'int')
                        self.current.code += "\n  %" + id + '.0 = alloca i32'
                else:
                    if typeof[0] != 'list' or list_info[1] != 'int':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  store i32 " + arithmetic[0] + ", i32* %" + id + '.' + str(self.current.vars[id][0])
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store i32 " + arithmetic[0] + ", i32* %sup" + str(self.var_counter) 
                    self.var_counter = self.var_counter + 1

            else:
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'double':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                    else:
                        self.current.vars[id] = (0, 'double')
                        self.current.code += "\n  %" + id + '.0 = alloca double'
                else:
                    if list_info[1] != 'double':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  store double " + arithmetic[0] + ", double* %" + id + '.' + str(self.current.vars[id][0])
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store double " + arithmetic[0] + ", double* %sup" + str(self.var_counter) 
                    self.var_counter = self.var_counter + 1

        elif ctx.value().list_value() != None:
            if table_assignment:
                raise UnsupportedOperationError('list cannot be a value at line ' + str(self.current_line))
            counter = 0
            if id in self.current.vars.keys():
                counter = self.current.vars[id][0] + 1
            self.current.vars[id] = (counter, 'list')
            var = (id, counter)
            typeof = 'int'
            for element in self.current.lists['!new_list']:
                if '.' in element:
                    typeof = 'double' 
            if typeof == 'double':
                for i in range(0, len(self.current.lists['!new_list'])):
                    if '.' not in self.current.lists['!new_list'][i]:
                        self.current.lists['!new_list'][i] = self.current.lists['!new_list'][i] + '.0'
            self.code_up += "@" + self.current.name + '.' + var[0] + '.' + str(var[1]) + " = dso_local global [" + str(len(self.current.lists['!new_list'])) + " x " + (typeof if typeof == 'double' else 'i32') + "] ["
            for element in self.current.lists['!new_list']:
                self.code_up += (typeof if typeof == 'double' else 'i32') + ' ' + element + ', '
            self.code_up = self.code_up[:len(self.code_up) - 2] + ']\n'
            self.current.lists[id] = (counter, typeof, len(self.current.lists['!new_list']))
            del self.current.lists['!new_list']

        elif ctx.value().INT() != None and ctx.value().ID() != None:
            id_val = str(ctx.value().ID())
            self.checkID(id_val, 'list')
            list_info_val = self.current.lists[id_val]
            index_val = int(str(ctx.value().INT()))
            if index_val < 0 or index_val >= list_info_val[2]:
                raise IndexError('Bad index in value at line ' + str(self.current_line))

            if list_info_val[1] == 'int':
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'int':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'int')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca i32'
                    else:
                        self.current.vars[id] = (0, 'int')
                        self.current.code += "\n  %" + id + '.0 = alloca i32'
                else:
                    if typeof[0] != 'list' or list_info[1] != 'int':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x i32], [' + str(list_info_val[2]) + ' x i32]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* %" + id + '.' + str(self.current.vars[id][0])
                    self.var_counter = self.var_counter + 2
                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x i32], [' + str(list_info_val[2]) + ' x i32]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load i32, i32* %sup' + str(self.var_counter)
                    self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x i32], [' + str(list_info[2]) + ' x i32]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store i32 %sup" + str(self.var_counter + 1) + ", i32* %sup" + str(self.var_counter + 2) 
                    self.var_counter = self.var_counter + 3

            elif list_info_val[1] == 'double':     
                if not table_assignment:
                    if id in self.current.vars.keys():
                        if self.current.vars[id][1] != 'double':
                            self.current.vars[id] = (self.current.vars[id][0] + 1, 'double')
                            self.current.code += "\n  %" + id + '.' + str(self.current.vars[id][0]) + ' = alloca double'
                    else:
                        self.current.vars[id] = (0, 'double')
                        self.current.code += "\n  %" + id + '.0 = alloca double'
                else:
                    if list_info[1] != 'double':
                        raise TypeError('Wrong data type at line ' + str(self.current_line))

                if not table_assignment:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x double], [' + str(list_info_val[2]) + ' x double]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                    self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* %" + id + '.' + str(self.current.vars[id][0])
                    self.var_counter = self.var_counter + 2

                else:
                    self.current.code += "\n  %sup" + str(self.var_counter) + ' = getelementptr inbounds [' + str(list_info_val[2]) + ' x double], [' + str(list_info_val[2]) + ' x double]* @' + self.current.name + '.' + id_val + '.' + str(list_info_val[0]) + ', i32 0, i32 ' + str(index_val)
                    self.current.code += "\n  %sup" + str(self.var_counter + 1) + ' = load double, double* %sup' + str(self.var_counter)
                    self.current.code += "\n  %sup" + str(self.var_counter + 2) + ' = getelementptr inbounds [' + str(list_info[2]) + ' x double], [' + str(list_info[2]) + ' x double]* @' + self.current.name + '.' + id + '.' + str(list_info[0]) + ', i32 0, i32 ' + str(index)
                    self.current.code += "\n  store double %sup" + str(self.var_counter + 1) + ", double* %sup" + str(self.var_counter + 2) 
                    self.var_counter = self.var_counter + 3
            

    