class EmptyClass:
    """
    Just an empty class with nothing to see
    """

    pass


def dict2obj(d):
    if type(d) == list:  # noqa: E721
        d = [dict2obj(i) for i in d]
    try:
        d = dict(d)
    except (TypeError, ValueError):
        return d
    obj = EmptyClass()
    for k, v in d.items():
        obj.__dict__[k] = dict2obj(v)
    return obj
