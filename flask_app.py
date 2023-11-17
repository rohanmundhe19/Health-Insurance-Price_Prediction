from  flask import Flask,request,jsonify,render_template
import config
from Model.utils import MedicalInsurance
from query import insert_query

app = Flask(__name__)

@app.route("/")
def get_homeapi():
    return render_template("index.html")

@app.route("/predicted_charges",methods = ["POST"])
def get_medicalInsurance():

    data = request.form 
    age = eval(data["age"])
    gender = data["gender"]
    bmi = eval(data["bmi"])
    children = int(data["children"])
    smoker = data["smoker"]
    region = data["region"]

    medical = MedicalInsurance(age,gender,bmi,smoker,children,region)
    charges = medical.get_predicted_charges()
    charges = float(charges)
    user_data = (age,gender,bmi,children,smoker,region, charges)
    insert_query(user_data)
    return render_template("index.html",charges=charges)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

