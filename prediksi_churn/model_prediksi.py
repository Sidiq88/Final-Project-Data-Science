import joblib
import os
import numpy as np
import pandas as pd

# Load model dan tools
model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")
ohe = joblib.load("ohe.pkl")
mean_map_country = joblib.load("mean_map_country.pkl")
mean_map_products = joblib.load("mean_map_products.pkl")
global_mean_country = joblib.load("global_mean_country.pkl")
global_mean_products = joblib.load("global_mean_products.pkl")

def predict_churn(input_data):

    #input_data = dict berisi fitur user
    
    # Ubah ke dataframe
    df = pd.DataFrame(input_data)

    # Encoding gender
    df_ohe = pd.DataFrame(
    ohe.transform(df[['gender']]),
    columns=ohe.get_feature_names_out(['gender'])
)

    # Drop kolom gender asli
    df_numeric = df.drop(columns=['gender'])

    # Gabungkan
    df_final = pd.concat([df_numeric, df_ohe], axis=1)

    # Mean map country
    df_final['country'] = df_final['country'].map(mean_map_country)
    df_final['country'] = df_final['country'].fillna(global_mean_country)

    # Mean map products
    df_final['products_number'] = df_final['products_number'].map(mean_map_products)
    df_final['products_number'] = df_final['products_number'].fillna(global_mean_products)

    # Scaling
    num_cols=['tenure','balance', 'credit_score', 'age', 'estimated_salary']
    df_final[num_cols] = scaler.transform(df_final[num_cols])


    # Prediksi probabilitas churn
    prob = model.predict_proba(df_final)[0][1]
    pred = model.predict(df_final)[0]

    return pred, prob
