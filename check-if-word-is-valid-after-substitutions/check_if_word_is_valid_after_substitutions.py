def isValid(S):
    N = len(S)
    if N < 3 or (N % 3) != 0:
        return False
    if N == 3 and S != 'abc':
        return False
    s_arr_tmp = []
    j = 3
    while j <= N:
        if S[j - 3: j] != 'abc':
            s_arr_tmp.append(S[j - 3])
            j += 1
        else:
            j += 3
    if j - 3 < N:
        s_arr_tmp.extend(S[j - 3:])
    if len(s_arr_tmp) == 0:
        return True

    S_new = "".join(s_arr_tmp)
    if N == len(S_new):
        return False
    return isValid(S_new)


if __name__ == '__main__':
    while True:
        try:
            inp = raw_input()
        except EOFError, e:
            break
        except Exception, e:
            print(e)
            break
        print isValid(inp)
