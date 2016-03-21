from elasticsearch import Elasticsearch
import requests


def download_content():
    url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
    return requests.get(url)


def create_mapping():
    mapping = {
        'properties': {
            'geometry': {
                'type': 'geo_shape'
            }
        }
    }

    es = Elasticsearch()
    es.indices.create(index='geospatial', ignore=400)
    es.indices.put_mapping(index='geospatial', doc_type='country', body=mapping)


def build_documents(response):
    geojson = response.json()
    countries = geojson.get('features')

    for country in countries:
        yield {
            'id': country.get('id'),
            'name': country.get('properties', {}).get('name'),
            'geometry': country.get('geometry')
        }


def index_documents(documents):
    es = Elasticsearch()
    for document in documents:
        country_id = document.get('id')
        try:
            es.index(index='geospatial', doc_type='country', id=country_id, body=document)
        except:
            print('Failed to index country={}'.format(country_id))


# Retrieve and index the country polygons
create_mapping()
response = download_content()
documents = build_documents(response)
index_documents(documents)
