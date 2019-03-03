def maxArea(height):
    maxWater = 0
    N = len(height)
    i = 0
    j = N - 1
    while i < j:
        h = min(height[i], height[j])
        maxWater = max(maxWater, h * (j - i))
        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1
    return maxWater


if __name__ == '__main__':
    while True:
        try:
            inp = raw_input()
        except EOFError, e:
            break
        except Exception, e:
            print(e)
            break
        in_arr = inp.split(',')
        in_arr = map(lambda x: int(x), in_arr)
        print maxArea(in_arr)
