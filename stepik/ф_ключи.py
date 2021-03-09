def update_dictionary(d, key, value):
    if d.get(key, None) == None:
        if d.get(2 * key, None) == None:
            d.update({2 * key: [value]})
        else:
            d[2 * key] += [value]
    else:
        d[key] += [value]
