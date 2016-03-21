from elasticsearch import Elasticsearch
from flask import Flask
from flask_restful import reqparse, Api, Resource


class CountryResource(Resource):

    def _coordinate_query(self, longitude, latitude):
        return {
            'query': {
                'filtered': {
                    'filter': {
                        'geo_shape': {
                            'geometry': {
                                'relation': 'intersects',
                                'shape': {
                                    'type': 'point',
                                    'coordinates': [longitude, latitude]
                                }
                            }
                        }
                    }
                }
            }
        }

    def _build_response(self, hits):
        return [
            {
                'id': hit.get('_source').get('id'),
                'name': hit.get('_source').get('name'),
            }
            for hit in hits
        ]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lon', type=float, required=True)
        parser.add_argument('lat', type=float, required=True)
        args = parser.parse_args()

        es = Elasticsearch()
        search_query = self._coordinate_query(args['lon'], args['lat'])
        search_result = es.search(index='geospatial', body=search_query)
        hits = search_result.get('hits', {}).get('hits', [])
        return self._build_response(hits)

app = Flask(__name__)
api = Api(app)
api.add_resource(CountryResource, '/countries')
app.run()
