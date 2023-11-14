n = 5

def isSafe(state, row, col):
    for cell in state[row]:
        if cell:
            return False
        
    for r,c in zip(range(row, n), range(col, -1, -1)):
        if state[r][c]:
            return False
    
    for r,c in zip(range(row, -1, -1), range(col, -1, -1)):
        if state[r][c]:
            return False
    
    return True

def solve(state, col):
    if col==n:
        print(*state, sep='\n')
        return True
    for row in range(n):
        if isSafe(state, row, col):
            state[row][col] = 1
            if solve(state, col+1):
                return True
            state[row][col] = 0
    return False

a = [0]*n
solve(list(a[:] for _ in range(n)), 0)