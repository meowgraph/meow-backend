from BookModel.models import Book


def searchByISBN(_ISBN):
    res = Book.objects.get(ISBN=_ISBN)
    return res


def searchByTitle(_title):
    res = Book.objects.filter(title=_title)
    return res


def searchByAuthor(_author):
    res = Book.objects.filter(author__icontains=_author)
    return res


def searchByTranslator(_translator):
    res = Book.objects.filter(translator__icontains=_translator)
    return res


def searchByPublisher(_publisher):
    res = Book.objects.filter(publisher=_publisher)
    return res
