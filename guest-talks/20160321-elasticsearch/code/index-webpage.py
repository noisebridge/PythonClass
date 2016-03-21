import argparse
from elasticsearch import Elasticsearch
import requests
from urlparse import urlparse


def download_content(url):
    return requests.get(url)


def build_document(response):
    parsed_url = urlparse(response.url)
    return {
        'url': response.url,
        'domain': parsed_url.hostname,
        'content': response.text,
    }


def index_document(document):
    es = Elasticsearch()
    url = document.get('url')
    es.index(index='tutorial', doc_type='website', id=url, body=document)


# Command-line arguments
parser = argparse.ArgumentParser(description='Index a single web page')
parser.add_argument('url')
args = parser.parse_args()

# Retrieve and index the URL specified by the user
response = download_content(args.url)
document = build_document(response)
index_document(document)
