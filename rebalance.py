def prop_allocate(n, *bal_prop):
    #n: new amount to allocate
    #bal_prop: tuples of balance, proportion
    h = []
    t = sum([n]+[b[0] for b in bal_prop])
    for bp in bal_prop: h.append((bp[1]*t)-bp[0])
    return h
