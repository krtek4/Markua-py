from CommonMark import dump


def dumpJSON(obj):
    return dump.dumpJSON(obj)


def dumpAST(obj, ind=0, topnode=False):
    return dump.dumpAST(obj, ind, topnode)
