from Library.settings import graph


def extendTripple(entity):
    res = [entity]
    return res


def searchByEntityandRelation(head, tail, relation):
    heads = extendTripple(head)
    tails = extendTripple(tail)
    res = []
    for h in heads:
        for t in tails:
            res.extend(graph.run(
                f"MATCH p=(h)-[r]-(t) WHERE h.name='{h.name}' AND h.type='{h.type}' AND "
                f"t.name='{t.name}' AND t.type='{t.type}' AND r.name='{relation.name}' RETURN p").data())

    return res
