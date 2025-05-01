def fibonacci(N):
    out = [0, 1]
    for i in range(2, N+1):
        out.append(out[i-1] + out[i-2])
    return out

