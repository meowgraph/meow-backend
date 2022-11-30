from django.http import HttpResponse

from BookModel.tests import createMySQL
from GraphModel.tests import createNeo4j
from service import searchs


def createTestdb(request):
    createMySQL("data/books.json")
    createNeo4j("data/entities.txt", "data/relations.txt")
    return HttpResponse("Success")


def testSearch(request):
    res1 = searchs.search("作者是何希才的书")
    res2 = searchs.search("标题是冲压工艺与模具设计实用技术的书")
    res3 = searchs.search("湖南省湘阴郭氏家族史")
    return HttpResponse(res2)
