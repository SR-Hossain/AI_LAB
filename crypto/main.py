def str2num(inp, d):
    inp_num = 0
    for c in inp:
        inp_num = inp_num*10 + int(d[c])
    return inp_num

def num2str(inp, d):
    return ''.join(list(d.get(c, c) for c in inp))

first, second, third = input(), input(), input()
st = ''.join(set(first+second))

n = len(st)

for ans in range(10**(n+2)):
    s = str(ans)
    if len(s) == len(set(s)) and len(s) == n:
        d = dict(zip(st, s))
        reverse_d = dict(zip(s, st))
        first_num = str2num(first, d)
        second_num = str2num(second, d)
        third_num = str(first_num + second_num)
        if len(third_num)<=len(third):
            third_num = '0'*(len(third)-len(third_num))+third_num
            third_num_str = num2str(third_num, reverse_d)
            for i in range(len(third_num_str)):
                try:
                    int(third_num_str[i])
                    if third[i] not in d:
                        d[third[i]] = third_num_str[i]
                    elif d[third[i]] != third_num_str[i]:
                        break
                except:
                    if third_num_str[i] != third[i]:
                        break
            else:
                print(first_num, '+', second_num, '=', third_num)
                break

