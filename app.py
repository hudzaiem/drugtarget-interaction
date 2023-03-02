import pandas as pd
import numpy as np
import streamlit as st
import pickle
from utilities.util import to_maccs,make_dataframe

model = pickle.load(open('static/model_baru.pkl','rb'))

def main():
    st.title("Prediksi Senyawa Potensial untuk Obesitas")
    smiles = st.text_area("Masukan SMILES")
    predict = st.button("Predict")

    maccs = to_maccs(smiles)
    df = make_dataframe(maccs)
    df.columns = df.columns.astype(str)
    y_pred = model.predict(df)
    y_pred = y_pred.tolist()
    x = y_pred.count('Berinteraksi')

    if x >= 3:
        hasil = 'Berpotensi'
    else:
        hasil = 'Tidak Berpotensi'

    if predict:
        try:    
            st.success(f"Senyawa diatas {hasil} terhadap obesitas")
        except:
            st.error("coba lagi")

if __name__ == '__main__':
    main()

