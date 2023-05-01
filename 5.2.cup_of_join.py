def join(*args, sep='-'):
    res = []
    for i, arg in enumerate(args):
        res.extend(arg)
        if i < len(args) - 1:
            res.append(sep)

    if not res:
        return None
    else:
        return res


#print(join([1, 2], [8], [9, 5, 6], sep='@'))
#print(join([1, 2], [8], [9, 5, 6]))
#print(join([1]))
#print(join())