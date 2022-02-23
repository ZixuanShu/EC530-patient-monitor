from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Sup'

datas = {
    1: {"name": "Jen", "age":22, "gender": "female", "bloodtype": "AB", "height": 165, "weight": "50kg"},
    2: {"name": "Max", "age": 25, "gender": "male", "bloodtype": "B", "height": 185, "weight": "70kg"},
    3: {"name": "Larry", "age": 10, "gender": "male", "bloodtype": "O", "height": 105, "weight": "30kg"}
}

data_put_args = reqparse.RequestParser()
data_put_args.add_argument("name", type = str, help = "name of the patient is requried", required = True) 
data_put_args.add_argument("age", type = str, help = "age of the patient is requried", required = True) 
data_put_args.add_argument("gender", type = str, help = "gender of the patient is requried")
data_put_args.add_argument("bloodtype", type = str, help = "bloodtype of the patient is requried")
data_put_args.add_argument("height", type = str, help = "height of the patient is requried")
data_put_args.add_argument("weight", type = str, help = "weight of the patient is requried")

def abort_if_no_id(pid):
    if pid not in datas:
        abort(404, message = "Patient id is not valid...")

def abort_if_id(pid):
    if pid in datas:
        abort(409, message = "Patient id is already there...")

class PatientInfo(Resource):
    def get(self, pid):
        abort_if_no_id(pid)
        return datas[pid]

    def post(self):
        return {"data": "Posted"}

    def put(self,pid):
        abort_if_id(pid)
        args = data_put_args.parse_args()
        datas[pid] = args
        return datas[pid], 201

    def delete(self,pid):
        abort_if_no_id(pid)
        del datas[pid]
        return '', 204
    


api.add_resource(PatientInfo, "/patientinfo/<int:pid>")
 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= 8080, debug=True)