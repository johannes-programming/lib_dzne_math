

def roman(number):
    if type(number) is not int:
        raise TypeError()
    if number <= 0:
        raise ValueError()
    translator = {
        1:"I", 
        4:"IV", 
        5:"V", 
        9:"IX", 
        10:"X", 
        40:"XL",
        50:"L", 
        90:"XC", 
        100:"C", 
        400:"CD", 
        500:"D", 
        900:"CM", 
        1000:"M",
    }
    ans = ""
    for integer in sorted(translator.keys(), reverse=True):
        div, number = divmod(number, integer)
        ans += div * translator[integer]
    return ans

def alpha(number):
    ascii_uppercase = "".join(chr(n) for n in range(0x41, 0x5B))
    digits = 1
    while number >= (26 ** digits):
        number -= (26 ** digits)
        digits += 1
    ans = ""
    while len(ans) < digits:
        number, r = divmod(number, 26)
        ans = chr(0x41 + r) + ans
    return ans 
