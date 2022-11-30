import json

from django.http import HttpResponse

import BookModel.searchs
import GraphModel.searchs


def getTripples(content):
    res = {"entities": [], "relations": []}
    fin = open("data/tests_entities.txt", encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        if line["text"] == content:
            res["entities"].extend(line["entities"])
    fin.close()

    fin = open("data/tests_relations.txt", encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        if line['text'] == content:
            res["relations"].append({"h": line["h"], "t": line["t"], "relation": line["relation"]})
    fin.close()
    return res


def sortBooks(books):
    res = {}
    for book in books:
        if book in res.keys():
            res[book] = res[book] + 1
        else:
            res[book] = 1

    return sorted(res.items(), key=lambda x:x[1], reverse=True)


def search(content):
    books = []
    tripples = getTripples(content)
    for entity in tripples["entities"]:
        if entity["type"] == "person":
            name = entity["name"]
            books.extend(BookModel.searchs.searchByAuthor(name))
            books.extend(BookModel.searchs.searchByTranslator(name))
            books.extend(GraphModel.searchs.searchByEntity({"type": "person", "name": name}))
        else:
            books.extend(GraphModel.searchs.searchByEntity({"type": entity["type"], "name": entity["name"]}))

    for relation in tripples["relations"]:
        books.extend(GraphModel.searchs.searchByEntityandRelation(relation["h"], relation["t"], relation["relation"]))
    return HttpResponse(sortBooks(books))
