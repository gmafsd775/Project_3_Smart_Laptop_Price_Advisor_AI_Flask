from flask import Flask, render_template, request, jsonify
from prediction import prepare_input, predict_price
import joblib
import pandas as pd
import json

app = Flask(__name__)
MODEL_PATH = "model/laptop_price_model.pkl"
FEATURES_PATH = "model/feature_names.pkl"


DATA_PATH = "data/laptop_price.csv"

df = pd.read_csv(DATA_PATH)

brand_avg = (
    df.groupby("brand")["price"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

chart_labels = brand_avg.index.tolist()
chart_values = brand_avg.values.tolist()


model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURES_PATH)

print("✅ Model Loaded Successfully")
print("✅ Feature Names Loaded Successfully")

@app.route("/", methods=["GET", "POST"])
def index():

    predicted_price = None

    selected_brand = ""
    selected_ram = ""
    selected_storage = ""
    selected_cpu = ""
    selected_gpu = ""

    if request.method == "POST":

        form_data = request.form.to_dict()

        model_input = prepare_input(

            form_data["brand"],
            form_data["ram_type"],
            form_data["rom_type"],
            form_data["os"],
            form_data["cpu_brand"],
            form_data["cpu_family"],
            form_data["cpu_series"],
            form_data["gpu_brand"],
            form_data["gpu_series"],
            form_data["spec_rating"],
            form_data["ram"],
            form_data["rom"],
            form_data["display_size"],
            form_data["resolution_width"],
            form_data["resolution_height"],
            form_data["warranty"],
            form_data["cpu_generation"],
            form_data["cpu_cores"],
            form_data["cpu_threads"],
            form_data["gpu_memory"]

        )

        predicted_price = predict_price(model_input)

        selected_brand = form_data["brand"]
        selected_ram = form_data["ram"]
        selected_storage = form_data["rom"]
        selected_cpu = form_data["cpu_brand"] + " " + form_data["cpu_series"]
        selected_gpu = form_data["gpu_brand"] + " " + form_data["gpu_series"]

    return render_template(

        "index.html",

        predicted_price=predicted_price,

        chart_labels=chart_labels,
        chart_values=chart_values,

        selected_brand=selected_brand,
        selected_ram=selected_ram,
        selected_storage=selected_storage,
        selected_cpu=selected_cpu,
        selected_gpu=selected_gpu

    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)