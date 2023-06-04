
import pandas as _pd


def isna(*values):
    ans = {(_pd.isna(x) is True) for x in values}
    ans, = ans
    return ans

def notna(*values):
    return not isna(*values)

def allisna(*values):
    return all(isna(x) for x in values)

def allnotna(*values):
    return all(notna(x) for x in values)

def anyisna(*values):
    return any(isna(x) for x in values)

def anynotna(*values):
    return any(notna(x) for x in values)



 
