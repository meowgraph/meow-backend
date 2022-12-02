from py2neo import NodeMatcher, Node, Path, RelationshipMatcher

import BookModel.searchs
from Library.settings import graph


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
    res = []
    node_matcher = NodeMatcher(graph)
    relation_matcher = RelationshipMatcher(graph)
    heads = list(node_matcher.match(head["type"]).where(name=head["name"]))
    tails = list(node_matcher.match(tail["type"]).where(name=tail["name"]))
    for h in heads:
        for t in tails:
            relations = list(relation_matcher.match(nodes=(h, t), r_type=relation))
            for relation in relations:
                belong = relation['belong']
                for ISBN in belong:
                    res.append(BookModel.searchs.searchByISBN(ISBN))
    return res
