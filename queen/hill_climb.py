from random import randint
def genRandom(n):
    return list(randint(0, 10000)%n for _ in range(n))


def attacks(state):
    ans = 0
    n = len(state)
    
    for i in range(n):
        for j in range(i+1, n):
            if state[i]==state[j] or abs(state[i]-state[j])==j-i:
                ans += 1

    return ans


def genBoard(cur):
    n = len(cur)
    ans = list(list(0 for _ in range(n)) for __ in range(n))
    for i,x in enumerate(cur):
        ans[i][cur[i]] = 1
    return ans


def solve(n):
    cur = genRandom(n)
    
    while attacks(cur):
        prevAttacks = curAttacks = attacks(cur)

        for i in range(n):
            for j in range(n):
                if cur[i] != j:
                    next = cur[:]
                    next[i] = j
                    newAttacks = attacks(next)
                    if newAttacks < curAttacks:
                        curAttacks = newAttacks
                        cur = next
        if prevAttacks == curAttacks:
            cur = genRandom(n)

    return genBoard(cur)


print(*solve(8), sep='\n')
    