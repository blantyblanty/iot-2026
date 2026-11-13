def to_lower_char(ch):
    """Робить одну велику латинську літеру малою."""
    code = ord(ch)
    return chr(code + 32) if 65 <= code <= 90 else ch

def count_ss(a , s , x):
    
    return a, s, x


def count_xo(s):
    x_count = 0
    o_count = 0
    for ch in s:
        c = to_lower_char(ch)
        if c == 'x':
            x_count += 1
        elif c == 'o':
            o_count += 1
    return x_count, o_count


def XO(s):
    x_count, o_count = count_xo(s)
    return x_count == o_count


text = input("Введіть рядок: ")
print(XO(text))

x_total, o_total = count_xo(text)
print("Кількість x:", x_total)
print("Кількість o:", o_total)
