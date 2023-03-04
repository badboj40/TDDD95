
__author__ = "Gustav Elmqvist"


def valid_clause(clause, x):
    for is_inverted, bit_index in clause:
        if is_inverted ^ ((x & bit_index) > 0):
            return True
    return False


def satisfiable(clauses, x):
    for clause in clauses:
        if not valid_clause(clause, x):
            return False
    return True


def parse_indata(m):
    clauses = []
    for _ in range(m):
        row = input().replace('X','').split(' v ')
        clause = []
        for variable in row:
            is_inverted = '~' in variable
            bit_index = 1 << (int(variable.replace('~',''))-1)
            clause.append((is_inverted, bit_index))
        clauses.append(clause)
    return clauses


for _ in range(int(input())):
    n, m = map(int, input().split())
    
    clauses = parse_indata(m)

    for x in range(1<<n):
        if satisfiable(clauses, x):
            print("satisfiable")
            break
    else:
        print("unsatisfiable")