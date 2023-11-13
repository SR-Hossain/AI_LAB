'''''
234
157
89_

23415789_
2341578_9, 23415_89 # +3 -3 (-1@%0 +1@%2)


243
159
8_7
'''''

initial = list(input()+input()+input())
input()
final = list(input()+input()+input())
print(initial, final)
visited = dict()

    
def h(cur):
    return sum(int(cur[i]!=final[i]) for i in range(9))

def manhattan(cur):
    return sum(abs(final.index(cur[i])-i) for i in range(9))
def move(condition, cur, pos, new_pos):
    if condition:
        return (10**9, 10**9, cur, pos)
    cur[pos], cur[new_pos] = cur[new_pos], cur[pos]
    if ''.join(cur) in visited:
        return (10**9, 10**9, cur, pos)
    visited[''.join(cur)] = True
    return (
        h(cur),
        manhattan(cur),
        cur,
        new_pos
    )

def up(cur, pos): return move(pos-3<0, cur, pos, pos-3);
def down(cur, pos): return move(pos+3>8, cur, pos, pos+3);
def left(cur, pos): return move(pos%3==0, cur, pos, pos-1);
def right(cur, pos): return move(pos%3==2, cur, pos, pos+1);


cur = initial
pos = cur.index('_')
i=0
while cur != final:
    cur = min(
        up(cur[:], pos), 
        down(cur[:], pos),
        left(cur[:], pos),
        right(cur[:], pos)
    )
    print(cur)
    pos = cur[3]
    cur = cur[2]


