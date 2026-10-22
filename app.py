import joblib
import pandas as pd
import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Content Engagement Simulator", layout="wide")

@st.cache_resource
def load_artifacts():
    model = joblib.load('xgb_model.pkl')
    columns = joblib.load('model_columns.pkl')
    return model, columns

model, model_columns = load_artifacts()

st.title("🎯 What-If Simulator: Prediksi Total Engagement Konten")
st.markdown("Ubah parameter konten di bawah ini untuk melihat estimasi interaksi secara instan berdasarkan model **XGBoost**.")

# Sidebar untuk input pengguna
st.sidebar.header("🔧 Pengaturan Atribut Konten")

content_format = st.sidebar.selectbox("Format Konten", ['Feed', 'Reels', 'Carousel']) 
content_type = st.sidebar.selectbox("Tipe Konten", [
    'Call-to-Action', 
    'Dokumentasi Kegiatan', 
    'Edukasi', 
    'Hari Besar', 
    'Hiburan', 
    'Informasi', 
    'Kolaborasi', 
    'Lainnya', 
    'Testimoni'
])
topik = st.sidebar.selectbox("Topik", [
    'Bank Sampah', 
    'Daur Ulang', 
    'Lingkungan', 
    'Sampah Organik', 
    'Sampah Plastik'
])
time_slot = st.sidebar.selectbox("Time Slot", ['Pagi', 'Siang', 'Sore', 'Malam'])
day_name = st.sidebar.selectbox("Hari (Day Name)", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

caption_word_count = st.sidebar.slider("Jumlah Kata Caption", 10, 300, 50)
hashtag_count = st.sidebar.slider("Jumlah Hashtag", 0, 30, 10)

# Tombol Simulasi
if st.sidebar.button("Jalankan Simulasi"):
    # Buat dataframe kosong dengan struktur kolom persis seperti saat training
    skenario = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Format nama kolom sesuai One-Hot Encoding
    col_format = f"Content_Format_{content_format}"
    col_type = f"Content_Type_{content_type}"
    col_topik = f"Topik_{topik}"
    col_time = f"Time_Slot_{time_slot}"
    col_day = f"Day_Name_{day_name}"
    
    # Set nilai 1 jika kolom tersedia dalam fitur
    if col_format in skenario.columns: skenario[col_format] = 1
    if col_type in skenario.columns: skenario[col_type] = 1
    if col_topik in skenario.columns: skenario[col_topik] = 1
    if col_time in skenario.columns: skenario[col_time] = 1
    if col_day in skenario.columns: skenario[col_day] = 1
    
    # Masukkan nilai fitur numerik
    if 'Caption_Word_Count' in skenario.columns: skenario['Caption_Word_Count'] = caption_word_count
    if 'Hashtag_Count' in skenario.columns: skenario['Hashtag_Count'] = hashtag_count
    
    # Prediksi menggunakan model
    pred_engagement = model.predict(skenario)[0]
    pred_engagement = max(0, pred_engagement)
    
    # Tampilkan Hasil di Halaman Utama
    st.success("Simulasi Selesai!")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🎯 Estimasi Total Engagement", value=f"{int(round(pred_engagement)):,} interaksi")
    
    with col2.expander("Lihat Detail Parameter Skenario"):
        st.json({
            "Content_Format": content_format,
            "Content_Type": content_type,
            "Topik": topik,
            "Time_Slot": time_slot,
            "Day_Name": day_name,
            "Caption_Word_Count": caption_word_count,
            "Hashtag_Count": hashtag_count
        })
else:
    st.info("👈 Silakan atur parameter di sidebar sebelah kiri, lalu klik tombol **Jalankan Simulasi**.")
