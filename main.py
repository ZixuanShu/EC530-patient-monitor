from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PatientInfo(Resource):
    def get(self):
        return {"data": "blood pressure, height, weight, age"}

api.add_resource(PatientInfo, "/patientinfo")
 


if __name__ == "__main__":
    app.run(debug=True)