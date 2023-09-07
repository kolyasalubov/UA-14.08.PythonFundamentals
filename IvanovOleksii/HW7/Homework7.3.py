def func(string: str) -> dict:
    """

    :param string: input string
    :return: dict in which calculated count of characters in given string
    """

    res = {}
    for i in string:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res


print(func('hello'))
