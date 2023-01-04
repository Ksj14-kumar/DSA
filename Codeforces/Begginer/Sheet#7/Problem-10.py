N= int(input())


def rec(n):
    if n<2:
        return 0
    return 1+rec(n/2)

print(rec(N))