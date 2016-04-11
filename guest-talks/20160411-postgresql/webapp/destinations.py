from flask import Flask
from flask_restful import reqparse, Api, Resource
import psycopg2


class DestinationsResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('from_iata', type=str, required=True, action='append')
        args = parser.parse_args()

        from_iata_list = args.get('from_iata')

        conn = psycopg2.connect('')
        cursor = conn.cursor()

        statement = '''
            select to_country, to_iata, airline
            from routes_view
            where from_iata in ('{}')
        '''.format("', '".join(from_iata_list))
        cursor.execute(statement)        
        results = cursor.fetchall()

        response = {}
        for result in results:
            country, airport, airline = result
            if country not in response:
                response[country] = {}
            if airport not in response[country]:
                response[country][airport] = []
            response[country][airport].append(airline)

        return response

app = Flask(__name__)
api = Api(app)
api.add_resource(DestinationsResource, '/destinations')
app.run(debug=True)
