from flask import Flask, jsonify
from flask_restful import Api, Resource
from apscheduler.schedulers.background import BackgroundScheduler

import requests
import main
import time

app = Flask(__name__)
api = Api(app)

def sendTemp():
    temp = main.read_temp()
    dictToSend = {'temp': temp[1], 'timestamp': time.time() }
    res = requests.post('http://192.168.0.11:5022/saveTemp', json=dictToSend)
    print('response from server:',res.text)

scheduler = BackgroundScheduler()
job = scheduler.add_job(sendTemp, 'interval', minutes=1)
scheduler.start()

class CurrentTemp(Resource):
    def get(self):
        temp = main.read_temp()
        return jsonify(c=temp[0],f=temp[1])

api.add_resource(CurrentTemp, '/current')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')




    
