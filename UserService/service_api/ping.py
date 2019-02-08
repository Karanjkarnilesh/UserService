from django.db import connections
from django.db.utils import OperationalError
from flask_restful import Resource

class Ping(Resource):
    def get(self):
        db_conn = connections['default']
        try:
            c=db_conn.cursor()
        except OperationalError:
            return "dailed to connect db !!"
        else:
            return "welcome to restful. all well !!"