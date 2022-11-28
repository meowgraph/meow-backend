from py2neo import NodeMatcher

import BookModel.searchs
from Library.settings import graph


def extendTripple(entity):
    res = [entity]
    return res


def searchByEntity(entity):
    res = []
    node_matcher = NodeMatcher(graph)
    entities = list(node_matcher.match(entity["type"]).where(name=entity["name"]))
    for entity in entities:
        belong = entity['belong']
        for ISBN in belong:
            res.append(BookModel.searchs.searchByISBN(ISBN))
    return res


def searchByEntityandRelation(head, tail, relation):
    heads = extendTripple(head)
    tails = extendTripple(tail)
    res = []
    for h in heads:
        for t in tails:
            res.extend(
                graph.run(
                    f"MATCH p=(h)-[r]-(t) WHERE "
                    f"h.name='{h.name}' AND h.type='{h.type}' AND "
                    f"t.name='{t.name}' AND t.type='{t.type}' AND "
                    f"r.name='{relation.name}' RETURN p"
                ).data()
            )

    return res
