example = [[1, 'a', ['cat'], 2], [[[[3]]], 'dog'], 4, 5]


def flatten(liste):
    fixed_list = []
    for i in example:
        if isinstance(i, list):
            for k in i:
                if isinstance(k, list):
                    for j in k:
                        if isinstance(j, list):
                            for n in j:
                                if isinstance(n, list):
                                    for m in n:
                                        fixed_list.append(m)
                                else:
                                    fixed_list.append(n)
                        else:
                            fixed_list.append(j)
                else:
                    fixed_list.append(k)
        else:
            fixed_list.append(i)
    print(fixed_list)


flatten(example)

