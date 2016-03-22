from elasticsearch import Elasticsearch
import requests


def build_document():
    return {
        'title': 'The Art of Computer Programming, Volume 1',
        'author': 'Donald Knuth',
        'isbn': '0-201-03801-3',
    }


def index_document(document):
    es = Elasticsearch()
    isbn = document.get('isbn')
    es.index(
        index='tutorial',
        doc_type='book',
        id=isbn,
        body=document
    )


# Build and index a document
document = build_document()
index_document(document)
