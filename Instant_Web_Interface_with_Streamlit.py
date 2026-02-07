import streamlit as st
import pandas as pd
import numpy as np

# 1. Başlık ve Metin
st.title("Anında Web Arayüzü")
st.write("Bu arayüz sadece birkaç satır Python ile oluşturuldu.")

# 2. Etkileşimli Araçlar (Input)
isim = st.text_input("Adın ne?")
sayi = st.slider("Bir değer seç", 0, 100, 50)

if st.button("Tıkla ve Selamla"):
    st.success(f"Selam {isim}! Seçtiğin sayı: {sayi}")

# 3. Veri Görselleştirme (Data Dashboard)
st.subheader("Rastgele Veri Grafiği")
grafik_verisi = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Dolar', 'Euro', 'Altın']
)
st.line_chart(grafik_verisi)