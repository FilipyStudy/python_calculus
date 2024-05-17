import sympy, math, sys

GOLDEN_RATIO = float(sympy.S.GoldenRatio)


def fib(x):
    if x == 1:
        return 1
    else:
        n_one = math.pow(GOLDEN_RATIO, x)
        n_two = math.pow(1 - GOLDEN_RATIO, x)
        n_sum = n_one - n_two

        return int(n_sum / math.sqrt(5))

try:
    if len(sys.argv) != 3:
        print(len(sys.argv))
        print('Arguments are insufficient')
        sys.exit()
    else:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

    for i in range(start, end):
        print(fib(i), end=' ')

except:
    print('Something goes wrong, verify the input values and try again.')
