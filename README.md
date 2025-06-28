# Bike Sharing Dashboard

Dashboard interaktif berbasis Streamlit untuk menganalisis data peminjaman sepeda menggunakan dataset *Bike Sharing*.

## Deskripsi Proyek

Proyek ini dibuat sebagai bagian dari submission akhir kelas **Analisis Data dengan Python** dari Dicoding. Tujuan utamanya adalah melakukan analisis eksploratif dan visualisasi interaktif terhadap data peminjaman sepeda berdasarkan faktor-faktor seperti musim, cuaca, tipe pengguna, hari kerja, dan lainnya.  
Dashboard ini juga dilengkapi dengan fitur **filter interaktif berdasarkan tanggal** untuk mengeksplorasi data secara dinamis.


## Struktur Direktori

SUBMISSION/
├── dashboard/
│ ├── dashboard.py # Script utama dashboard Streamlit
│ └── main_data.csv # Dataset hasil pembersihan untuk visualisasi
├── data/
│ └── day.csv # Dataset mentah (asli) dari Bike Sharing
├── notebook.ipynb # Exploratory Data Analysis dan visualisasi
├── requirements.txt # Daftar dependencies Python
├── url.txt # Link dashboard Streamlit
└── README.md # Dokumentasi proyek


## Cara Menjalankan Dashboard


## Cara Menjalankan Dashboard

1. **Clone repositori** (atau ekstrak ZIP jika dari submission):

   ```bash
   git clone <repo-url>
   cd Submission
2. **Install semua dependensi** : 
pip install -r requirements.txt

3. Jalankan Streamlit:
streamlit run dashboard/dashboard.py

4. Akses di browser :
Streamlit biasanya akan terbuka otomatis di localhost:8501

## Fitur Analisis
Dashboard mencakup analisis interaktif berikut:
- Filter berdasarkan tanggal (fitur interaktif sidebar)
- Distribusi jumlah peminjaman harian 
- Pengaruh musim dan bulan terhadap peminjaman 
- Perbandingan hari kerja vs libur/akhir pekan
- Pengaruh kondisi cuaca 
- Segmentasi tipe pengguna (casual vs registered)

## Teknologi yang Digunakan
- Python
- Pandas
- Matplotlib & Seaborn
- Streamlit

## Sumber Dataset
Dataset yang digunakan berasal dari: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset 


## Lisensi
Proyek ini dibuat untuk keperluan pembelajaran dan tidak untuk keperluan komersial.
