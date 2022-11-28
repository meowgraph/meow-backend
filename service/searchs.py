import json

from django.http import HttpResponse

import BookModel.searchs
import GraphModel.searchs


def getTripples(content):
    fin = open("data/tests_entities.txt", encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        if line["text"] == content:
            res = {"entities": line["entities"]}
            return res
    return dict()


def search(content):
    res = []
    tripples = getTripples(content)
    for entity in tripples["entities"]:
        if entity["type"] == "person":
            name = entity["name"]
            res.extend(BookModel.searchs.searchByAuthor(name))
            res.extend(BookModel.searchs.searchByTranslator(name))
            res.extend(GraphModel.searchs.searchByEntity({"type": "person", "name": name}))
        else:
            res.extend(GraphModel.searchs.searchByEntity({"type": entity["type"], "name": entity["name"]}))
    return HttpResponse(res)
