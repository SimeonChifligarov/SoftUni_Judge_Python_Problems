def all_permutations(seq):
    length = len(seq)

    if length == 0:
        return []

    if length == 1:
        return [seq]

    l = []

    for i in range(length):
        m = seq[i]

        rem_list = seq[:i] + seq[i + 1:]

        for p in all_permutations(rem_list):
            l.append([m] + p)

    return l


def possible_permutations(ll):
    perms = all_permutations(ll)
    for p in perms:
        yield p

# [print(n) for n in possible_permutations([1, 2, 3])]
