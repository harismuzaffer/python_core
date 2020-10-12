def max_result_expression(expression, variables):
    vars = variables
    exp = list(expression.replace(' ', ''))
    exp.reverse()
    for var in vars:
        n = len(vars[var])
        vars[var] = (vars[var])[n - 1]
    l = []
    operators = ['+', '-', '*', '/']
    for i in range(len(exp)):
        if (exp[i] in operators) and len(l) < 2:
            break
        elif exp[i].isalpha():
            l.append((vars[exp[i]]))
        elif exp[i] in operators:
            var1 = int(l.pop())
            var2 = int(l.pop())
            var3 = (eval(str(var1) + exp[i] + str(var2) ))
            l.append(str(var3))
        else:
            l.append(exp[i])
    return l[0]