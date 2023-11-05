from roman import toRoman as roman


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
