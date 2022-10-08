def get_coeffs(digits):
    digits = digits.strip().strip(' = 0')
    digits = digits.split(' + ')
    coeffs = {}
    for i in digits:
        a, *b = i.split(' * x ** ')
        if b:
            coeffs[int(b[0])] = int(a)
        else:
            if i.endswith('x'):
                a, *b = i.split(' * x')
                coeffs[1] = int(a)
            else:
                coeffs[0] = int(i)
    return coeffs


def sum_coeffs(d, coeffs):
    for key in d:
        if not key in coeffs:
            coeffs[key] = 0
        coeffs[key] += d[key]
    return coeffs


with open('res.txt') as f:
    digits1 = f.read()
    digits2 = digits1[:]
coeffs1 = get_coeffs(digits1)
coeffs2 = get_coeffs(digits2)
coeffs = {}
coeffs = sum_coeffs(coeffs1, coeffs)
coeffs = sum_coeffs(coeffs2, coeffs)
res = ''
max_num = max(coeffs.keys())
for i, j in coeffs.items():
    res += str(j)
    if i != 0 and j != 0 and i != 1:
        res += ' * x ** '
        res += str(i)
        res += ' + '
    elif j == 0:
        continue
    eli
elif i == 1:
        res += ' * x + '
    else:
        res += ' = 0'
print(res)
