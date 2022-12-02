import http.client
import json
import synonyms

from django.http import HttpResponse

import BookModel.searchs
import GraphModel.searchs


def extendEntity(entity):
    res = [{"name": entity["name"], "type": entity["type"], "score": 1}]
    relative = synonyms.nearby(entity["name"], 5)
    for i in range(len(relative[0])):
        res.append({"name": relative[0][i], "type": entity["type"], "score": relative[1][i]})
    return res


def extendRelation(head, tail, relation):
    heads = extendEntity(head)
    tails = extendEntity(tail)
    res = []
    for head in heads:
        for tail in tails:
            res.append({"h": head, "t": tail, "relation": relation, "score": head["score"] * tail["score"]})
    return res


def getTripples(content):
    res = {"entities": [], "relations": []}
    fin = open("data/tests_entities.txt", encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        if line["text"] == content:
            for entity in line["entities"]:
                res["entities"].extend(extendEntity(entity))
    fin.close()

    fin = open("data/tests_relations.txt", encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        if line['text'] == content:
            res["relations"].extend(extendRelation(line["h"], line["t"], line["relation"]))
    fin.close()
    return res


def search(content):
    res = {}

    def countBook(books, score):
        for book in books:
            if book in res.keys():
                res[book] = res[book] + score
            else:
                res[book] = score

    tripples = getTripples(content)
    for entity in tripples["entities"]:
        books = []
        if entity["type"] == "person":
            name = entity["name"]
            books.extend(BookModel.searchs.searchByAuthor(name))
            books.extend(BookModel.searchs.searchByTranslator(name))
            books.extend(GraphModel.searchs.searchByEntity({"type": "person", "name": name}))
        else:
            books.extend(GraphModel.searchs.searchByEntity({"type": entity["type"], "name": entity["name"]}))
        countBook(books, entity["score"])

    for relation in tripples["relations"]:
        books = []
        books.extend(GraphModel.searchs.searchByEntityandRelation(relation["h"], relation["t"], relation["relation"]))
        countBook(books, relation["score"])

    return HttpResponse(sorted(res.items(), key=lambda x: x[1], reverse=True))
