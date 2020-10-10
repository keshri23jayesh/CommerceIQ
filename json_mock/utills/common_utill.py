"""
    Files Contains Utility Methods
"""


def check_key(dict, key):
    return True if key in dict.keys() else False

def query_set_to_dict(qs):
    res = {}
    for key in qs:
        res[key] = qs[key]
    return res