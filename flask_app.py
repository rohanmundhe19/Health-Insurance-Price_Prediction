from  flask import Flask,request,jsonify,render_template
import config
from Model.utils import MedicalInsurance

app = Flask(__name__)

@app.route("/")

def get_homeapi():

    return render_template("index.html")

@app.route("/predicted_charges",methods = ["POST","GET"])
def get_medicalInsurance():
    if request.method == "POST":
        data = request.form 
        age = eval(data["age"])
        gender = data["gender"]
        bmi = eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]

        medical = MedicalInsurance(age,gender,bmi,smoker,children,region)
        charges = medical.get_predicted_charges()
        return render_template("index.html",charges=charges)
    
    else:
        age = eval(request.args.get("age"))
        gender = request.args.get("gender")
        bmi = eval(request.args.get("bmi"))
        children = int((request.args.get("children")))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        medical = MedicalInsurance(age,gender,bmi,smoker,children,region)
        charges1 = medical.get_predicted_charges()

        return render_template("index.html",charges=charges1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

