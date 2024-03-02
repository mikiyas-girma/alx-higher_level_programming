
def dictionary():
    """return functional implementation of a dictionary"""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            # print(matches[0])
            key, value = matches[0]
            # print(key, value)
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch


"""lets test our custom dictionary implementation"""
d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
d('getitem', 3)
