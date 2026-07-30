import joblib
import pandas as pd

pd.set_option("display.max_columns", None)

MODEL_PATH = "model/laptop_price_model.pkl"
FEATURES_PATH = "model/feature_names.pkl"

model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURES_PATH)


def get_feature_names():

    return feature_names

def encode_feature(input_df, prefix, value):

    column_name = f"{prefix}_{value}"

    if column_name in input_df.columns:
        input_df[column_name] = 1    


def prepare_input(
    brand,
    ram_type,
    rom_type,
    os,
    cpu_brand,
    cpu_family,
    cpu_series,
    gpu_brand,
    gpu_series,
    spec_rating,
    ram,
    rom,
    display_size,
    resolution_width,
    resolution_height,
    warranty,
    cpu_generation,
    cpu_cores,
    cpu_threads,
    gpu_memory
):

    spec_rating = float(spec_rating)
    ram = int(ram)
    rom = int(rom)
    display_size = float(display_size)
    resolution_width = int(resolution_width)
    resolution_height = int(resolution_height)
    warranty = int(warranty)
    cpu_generation = int(cpu_generation)
    cpu_cores = int(cpu_cores)
    cpu_threads = int(cpu_threads)
    gpu_memory = int(gpu_memory)

    # Build empty dataframe with all features set to 0
    input_df = pd.DataFrame(
        [[0] * len(feature_names)],
        columns=feature_names
    )

    # Set numeric features
    input_df["spec_rating"] = spec_rating
    input_df["Ram"] = ram
    input_df["ROM"] = rom
    input_df["display_size"] = display_size
    input_df["resolution_width"] = resolution_width
    input_df["resolution_height"] = resolution_height
    input_df["warranty"] = warranty
    input_df["CPU_Generation"] = cpu_generation
    input_df["CPU_Cores"] = cpu_cores
    input_df["CPU_Threads"] = cpu_threads
    input_df["GPU_Memory"] = gpu_memory

    # Encode categorical features
    encode_feature(input_df, "brand", brand)
    encode_feature(input_df, "Ram_type", ram_type)
    encode_feature(input_df, "ROM_type", rom_type)
    encode_feature(input_df, "OS", os)
    encode_feature(input_df, "CPU_Brand", cpu_brand)
    encode_feature(input_df, "CPU_Family", cpu_family)
    encode_feature(input_df, "CPU_Series", cpu_series)
    encode_feature(input_df, "GPU_Brand", gpu_brand)
    encode_feature(input_df, "GPU_Series", gpu_series)

    return input_df


def predict_price(input_df):
    print(input_df.T)
    print(input_df.dtypes)

    prediction = model.predict(input_df)

    print("Prediction =", prediction)

    return round(prediction[0], 2)