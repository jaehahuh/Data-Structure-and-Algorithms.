def eval_postfix_boolean_exp(boolean_exp_str):
    stack = []
    operators = '<>&|'
    boolean_tokens = boolean_exp_str.split()
    for token in boolean_tokens:
        if token not in operators:
            num = int(token)
            stack.append(num)
        else:
            rhs_arg = stack.pop()
            lhs_arg = stack.pop()
            if token == "<":
                stack.append(lhs_arg < rhs_arg)
            elif token == ">":
                stack.append(lhs_arg > rhs_arg)
            elif token == "&":
                stack.append(lhs_arg and rhs_arg)
            elif token == "|":
                stack.append(lhs_arg or rhs_arg)
    return stack.pop()


