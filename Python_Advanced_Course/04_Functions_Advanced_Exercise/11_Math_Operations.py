def math_operations(*args, **kwargs):
    args_as_list = list(args)

    for i in range(len(args_as_list)):
        if i % 4 == 0:
            kwargs['a'] += args_as_list[i]
        elif i % 4 == 1:
            kwargs['s'] -= args_as_list[i]
        elif i % 4 == 2:
            if args_as_list[i] == 0:
                continue
            kwargs['d'] /= args_as_list[i]
        elif i % 4 == 3:
            kwargs['m'] *= args_as_list[i]

    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda item: (-item[1], item[0])))
    result = []

    for k, v in sorted_kwargs.items():
        result.append(f'{k}: {v:.1f}')

    return '\n'.join(result)

# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
