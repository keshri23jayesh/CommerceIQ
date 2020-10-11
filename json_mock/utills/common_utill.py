"""
    File Contains Utility Methods
"""


def check_key(dict, key):
    return True if key in dict.keys() else False


def query_set_to_dict(dict):
    res = {}
    for key in dict:
        res[key] = dict[key]
    return res

def isNumber(x):
    if type(x) == int:
        return True
    else:
        return False


def isStr(x):
    if type(x) == str:
        return True
    else:
        return False