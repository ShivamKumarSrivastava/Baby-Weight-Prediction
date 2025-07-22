from flask import Flask , request , jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/predict",methods=["POST"])
def get_prediction():
    baby_data = request.get_json()

    baby_df = pd.DataFrame(baby_data)

    with open("model/model.pkl","rb") as obj:
        model = pickle.load(obj)

    prediction = model.predict(baby_df)

    prediction = round(float(prediction))

    response = {"prediction":prediction}
    return jsonify(response)


if(__name__ == "__main__"):
    app.run(debug=True)