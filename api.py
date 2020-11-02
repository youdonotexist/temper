from flask import Flask, jsonify
from flask_restful import Api, Resource

import main

app = Flask(__name__)
api = Api(app)

class CurrentTemp(Resource):
    def get(self):
        temp = main.read_temp()
        return jsonify(c=temp[0],f=temp[1])

api.add_resource(CurrentTemp, '/current')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')




    
