example = [[1, 2], [3, 4], [5, 6, 7]]


def first_value(value):
    return value[0]


def reverse_list(liste):
    fixed_list = []
    for i in example:
        if isinstance(i, list):
            i.sort(reverse=True)
            for k in i:
                if isinstance(k, list):
                    k.sort(reverse=True)
                    for j in k:
                        if isinstance(j, list):
                            j.sort(reverse=True)
                            for n in j:
                                if isinstance(n, list):
                                    n.sort(reverse=True)
                                    for m in n:
                                        if isinstance(m, list):
                                            m.sort(reverse=True)

    example.sort(key=first_value, reverse=True)
    return example


print(reverse_list(example))
