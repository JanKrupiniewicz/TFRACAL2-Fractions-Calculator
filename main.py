from fractions import Fraction
def read_input_case():
    case = input()
    equations = []
    last_variable = input()
    while not last_variable[-1].isdigit():
        equations.append(last_variable)
        last_variable = input()
    return case, equations, last_variable

def parse_fraction(fraction_str):
    num, den = map(int, fraction_str.split("/"))
    return Fraction(num, den)

def evaluate_expression(expr, case_dict):
    onp_stack = []
    itr = 1
    while itr != len(expr):
        itr_end = itr
        if "a" <= expr[itr] <= "z":
            while "a" <= expr[itr_end] <= "z":
                itr_end = itr_end + 1
            onp_stack.append(case_dict[expr[itr:itr_end]])
            itr = itr_end
        elif expr[itr] == "_":
            itr += 1
        else:
            var1 = onp_stack.pop()
            var2 = onp_stack.pop()
            if expr[itr] == '+':
                onp_stack.append(var2 + var1)
            elif expr[itr] == '*':
                onp_stack.append(var2 * var1)
            elif expr[itr] == '/':
                onp_stack.append(var2 / var1)
            itr = itr + 1
    return onp_stack.pop()

def solve_test_case(case, equations, last_var):
    case_dict = {}
    var, fraction = last_var.split("=")
    case_dict[var] = parse_fraction(fraction)

    for equation in reversed(equations):
        var, expression = equation.split("=")
        result = evaluate_expression(expression, case_dict)
        case_dict[var] = result

    sorted_dict = dict(sorted(case_dict.items()))
    print(case + " Y")
    for key, item in sorted_dict.items():
        print(f"{key} {item.numerator} {item.denominator}")

for _ in range(1000):
    case, equations, last_variable = read_input_case()
    solve_test_case(case, equations, last_variable)
