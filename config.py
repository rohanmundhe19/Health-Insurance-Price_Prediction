import os

model_path=os.path.join("Model","KNN_model.pkl")
scaler_path=os.path.join("Model","scale.pkl")
json_path=os.path.join("Model","project_data.json")


DB_PARAM = {"host": "julydb.culi2vvhaxwm.ap-south-1.rds.amazonaws.com", "database":"vctchealth", "user":"root", "password":"adminadmin"}