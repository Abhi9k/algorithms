def longestOnes(A, K):
    N = len(A)
    i = 0
    j = i
    maxOnes = 0
    ones = 0
    zeroes_rem = K
    while j < N:
        if A[j] == 0:
            zeroes_rem -= 1
        if zeroes_rem >= 0:
            ones += 1
        if zeroes_rem < 0:
            maxOnes = max(maxOnes, ones)
            while i < N and zeroes_rem != 0:
                if A[i] == 0:
                    zeroes_rem += 1
                ones -= 1
                i += 1
            if zeroes_rem == 0:
                ones += 1
        j += 1
    maxOnes = max(maxOnes, ones)
    return maxOnes


if __name__ == '__main__':
    while True:
        try:
            inp = raw_input()
            K = int(raw_input())
        except EOFError, e:
            break
        except Exception, e:
            print(e)
            break
        in_arr = inp.split(',')
        in_arr = map(lambda x: int(x), in_arr)

        print longestOnes(in_arr, K)
