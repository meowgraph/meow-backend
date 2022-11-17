import json

from BookModel.models import Book


# Create your tests here.
def createMySQL(file):
    fin = open(file, encoding="utf-8", mode="r")
    for line in fin.readlines():
        line = json.loads(line)
        book = Book(
            title=line["title"],
            ISBN=line["ISBN"],
            author=line["author"],
            translator=line["translator"],
            publisher=line["publisher"],
        )
        book.save()

    fin.close()
