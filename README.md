# 🎯 Social Media Engagement Simulator

Aplikasi web berbasis Machine Learning yang dirancang untuk memprediksi dan mensimulasikan estimasi **Total Engagement** pada postingan media sosial berdasarkan berbagai atribut konten (*What-If Analysis*).

🚀 **Live App**: [Engagement Simulator Streamlit App](https://engagement-simulator-8kxzvlsqqi7qcmgyddy4ch.streamlit.app/)

---

## 📌 Fitur Utama

- **What-If Simulation**: Melakukan simulasi secara instan untuk melihat estimasi engagement berdasarkan pengaturan parameter konten.
- **Pengaturan Atribut Konten**:
  - **Format Konten**: Feed, Story, Reels, dll.
  - **Tipe Konten**: Call-to-Action, Edukasi, Hiburan, Kolaborasi, dll.
  - **Topik**: Bank Sampah, Daur Ulang, Lingkungan, Sampah Plastik, Organik, dll.
  - **Waktu & Hari Posting**: Slot waktu (Pagi, Siang, Malam) dan hari (Monday - Sunday).
  - **Metrik Teks**: Jumlah kata caption dan jumlah hashtag.
- **Model Feature Importance**: Visualisasi grafik faktor/fitur utama yang paling berpengaruh terhadap tingginya nilai *engagement*.

---

## 🛠️ Teknologi & Library

- **Python** (Versi 3.x)
- **Streamlit**: Framework antarmuka web interaktif
- **XGBoost**: Model Machine Learning untuk regresi/prediksi
- **Pandas & NumPy**: Pemrosesan dan manipulasi data
- **Matplotlib / Seaborn**: Visualisasi grafik Feature Importance
- **Joblib / Pickle**: Serialisasi model machine learning

---

## 📁 Struktur Repositori

```text
├── app.py                  # Script utama aplikasi Streamlit
├── xgb_model.pkl           # Model trained XGBoost
├── model_columns.pkl       # Daftar kolom/fitur untuk konsistensi input model
├── quartiles.pkl           # Data kuartil/kategori acuan
├── requirements.txt        # Daftar dependency Python
└── README.md               # Dokumentasi proyek
