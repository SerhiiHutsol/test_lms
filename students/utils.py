def qs2html(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(str(line))
    else:
        lst.append('QuerySet is empty!')
    return '<br>'.join(lst)
