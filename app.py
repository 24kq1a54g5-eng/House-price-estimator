from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("house_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    area = float(request.form["area"])
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    age = float(request.form["age"])

    prediction = model.predict([[area, bedrooms, bathrooms, age]])

    result = "Predicted House Price: ₹{:,.0f}".format(prediction[0])

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)