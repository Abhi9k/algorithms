import sys

if __name__ == '__main__':
    dirname = sys.argv[1]
    outfile = open("{0}/output".format(dirname), 'r')
    solution = open("{0}/solution".format(dirname), 'r')
    outputs = outfile.readlines()
    solutions = solution.readlines()
    N = len(solutions)
    if len(outputs) != N:
        print("Output and solution length mismatch!")
        exit(0)
    incorrect = filter(lambda x: outputs[x] != solutions[x], range(N))

    outfile.close()
    solution.close()
    print("{0} passed, {1} failed".format(N - len(incorrect), len(incorrect)))
