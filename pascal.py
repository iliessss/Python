def pascal(N):
    if N == 1:
        return [1]
    else:
        previous = pascal(N-1)
        return [1] + [previous[i] + previous[i+1] for i in range(N-2)] + [1]

print(pascal(6))