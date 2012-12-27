SIZE = 8

def solve(queens, solutions):
    if len(queens) == SIZE:
        solutions.append(queens)
    else:
        for i in range(SIZE):
            new_queens = queens + [i]
            if is_valid(new_queens):
                solve(queens + [i], solutions)
    return solutions


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
        x = ['-' for _ in range(len(solution))]
        x[q] = 'Q'
        print ' '.join(x)

if __name__ == '__main__':
    solutions = solve([], [])
    for solution in solutions:
        print_solution(solution)
