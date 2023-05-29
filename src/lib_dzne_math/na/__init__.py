
import pandas as _pd



def isna(*values):
    ans, = {_pd.isna(x) for x in values}
    return ans

def notna(*values):
    ans, = {_pd.notna(x) for x in values}
    return ans

def allisna(*values):
    return all(_pd.isna(x) for x in values)

def allnotna(*values):
    return all(_pd.notna(x) for x in values)

def anyisna(*values):
    return any(_pd.isna(x) for x in values)

def anynotna(*values):
    return any(_pd.notna(x) for x in values)



 
