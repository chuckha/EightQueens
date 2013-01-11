SIZE = 8

def solve(queens):
    """Returns a list of all good solutions that exist for the configuration described by queens"""
    print_solution(queens)
    if len(queens) == SIZE:
        return [queens]
    else:
        return sum([solve(queens + [i]) for i in range(SIZE) if is_valid(queens + [i])], [])

def is_valid(queens):
    # must be unique to imply different columns
    if len(set(queens)) != len(queens):
        return False
    for i, q in enumerate(queens):
        for i2, q2 in enumerate(queens):
            if i == i2:
                continue
            index_difference = i - i2
            if q2 == q - index_difference:
                return False
            if q2 == q + index_difference:
                return False
    return True

def print_solution(solution):
    print "=={}==".format(solution)
    for q in solution:
        x = ['-' for _ in range(SIZE)]
        x[q] = 'Q'
        print ' '.join(x)

if __name__ == '__main__':
    solutions = solve([])
    for solution in solutions:
        print_solution(solution)

