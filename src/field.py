def field(items, *args):
    assert len(args) > 0
    assert type(items) == list
    
    if len(args) == 1:
        for it in items:
            yield it[args[0]]
    else:
        for _dict in items:
            yield {_key:_dict[_key] for _key in args}

