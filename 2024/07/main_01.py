
def main():
    input_fn = "input_ex.txt"
    equations = []

    with open(input_fn) as f:
        while l := f.readline():
            initial_split = l.split(":")
            result = int(initial_split[0])
            digits = [int(n) for n in initial_split[1].split()]
            equations.append((result, digits))

    equations = iter(equations)
    current_equation = next(equations)
    equation_result = current_equation[0]
    equation_digits = current_equation[1]


main()
