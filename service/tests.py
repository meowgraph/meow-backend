from django.http import HttpResponse

from GraphModel.tests import createNeo4j


def createTestdb(request):
    # createMySQL("data/test.json")
    createNeo4j("data/entities.txt", "data/relations.txt")
    return HttpResponse("Success")
