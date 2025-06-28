import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load data
df = pd.read_csv("dashboard/main_data.csv")

# Konversi kolom tanggal ke format datetime
df["dteday"] = pd.to_datetime(df["dteday"])
df["mnth_name"] = df["dteday"].dt.strftime('%b')  # Nama bulan (opsional)

# Sidebar - Filter berdasarkan tanggal
st.sidebar.subheader("📅 Filter berdasarkan tanggal")
start_date = st.sidebar.date_input("Tanggal mulai", df["dteday"].min())
end_date = st.sidebar.date_input("Tanggal akhir", df["dteday"].max())

if start_date > end_date:
    st.sidebar.error("Tanggal mulai tidak boleh lebih besar dari tanggal akhir.")

# Filter data
filtered_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

# Judul
st.title("🚴‍♀️ Bike Sharing Dashboard")
st.markdown("Analisis peminjaman sepeda di Washington D.C. berdasarkan musim, hari kerja, cuaca, dan jenis pengguna.")

# Ringkasan metrik
col1, col2, col3 = st.columns(3)
col1.metric("Total Hari", filtered_df.shape[0])
col2.metric("Total Peminjaman", f"{filtered_df['cnt'].sum():,.0f}")
col3.metric("Rata-rata Harian", f"{filtered_df['cnt'].mean():.0f}")

st.markdown("---")

# Menu analisis
opsi = st.selectbox("Pilih Analisis", [
    "Distribusi Peminjaman",
    "Musim & Bulan",
    "Hari Kerja vs Libur",
    "Kondisi Cuaca",
    "Segmentasi Pengguna"
])

# Visualisasi berdasarkan pilihan
if opsi == "Distribusi Peminjaman":
    st.markdown("### Distribusi Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['cnt'], bins=30, kde=True, ax=ax)
    ax.set_title("Distribusi Jumlah Peminjaman Sepeda per Hari")
    st.pyplot(fig)

elif opsi == "Musim & Bulan":
    st.markdown("### Peminjaman Berdasarkan Musim")
    fig, ax = plt.subplots()
    sns.boxplot(x='season', y='cnt', data=filtered_df, palette='pastel', ax=ax)
    ax.set_title("Distribusi Peminjaman Berdasarkan Musim")
    st.pyplot(fig)

    st.markdown("### Rata-rata Peminjaman per Bulan")
    fig, ax = plt.subplots(figsize=(12, 4))
    order_m = list(range(1, 13))
    sns.barplot(x='mnth', y='cnt', data=filtered_df, order=order_m, ci=None, palette='Set2', ax=ax)
    ax.set_title("Rata-Rata Jumlah Peminjaman per Bulan")
    st.pyplot(fig)

elif opsi == "Hari Kerja vs Libur":
    st.markdown("### Perbandingan Hari Kerja vs Libur")
    fig, ax = plt.subplots()
    sns.boxplot(x='workingday', y='cnt', data=filtered_df, palette='cool', ax=ax)
    ax.set_xticklabels(['Libur/Akhir Pekan', 'Hari Kerja'])
    ax.set_title("Peminjaman: Hari Kerja vs Libur")
    st.pyplot(fig)

elif opsi == "Kondisi Cuaca":
    st.markdown("### Pengaruh Cuaca terhadap Jumlah Peminjaman")
    weather_labels = {
        1: 'Clear or Partly Cloudy',
        2: 'Mist or Cloudy',
        3: 'Light Snow or Rain',
        4: 'Heavy Rain or Fog'
    }
    filtered_df['weather_desc'] = filtered_df['weathersit'].map(weather_labels).fillna("Unknown")


    fig, ax = plt.subplots()
    sns.boxplot(x='weather_desc', y='cnt', data=filtered_df, palette='coolwarm', ax=ax)
    ax.set_title("Pengaruh Cuaca terhadap Peminjaman")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=15)
    st.pyplot(fig)

elif opsi == "Segmentasi Pengguna":
    st.markdown("### Total Peminjaman Berdasarkan Jenis Pengguna")
    fig, ax = plt.subplots()
    sns.barplot(x=['casual', 'registered'], y=filtered_df[['casual', 'registered']].sum().values,
                palette='Set2', ax=ax)
    ax.set_ylabel("Total Peminjaman")
    ax.set_xlabel("Jenis Pengguna")
    ax.set_title("Total Peminjaman: Registered vs Casual")
    st.pyplot(fig)

    # Rata-rata bulanan per jenis pengguna
    st.markdown("### Rata-Rata Peminjaman Bulanan per Jenis Pengguna")
    month_order = list(range(1, 13))
    df_month_user = filtered_df.groupby('mnth')[['casual', 'registered']].mean().reindex(month_order)
    fig, ax = plt.subplots(figsize=(12, 5))
    df_month_user.plot(kind='bar', ax=ax, color=['#9b59b6', '#3498db'])
    ax.set_title("Rata-Rata Bulanan: Casual vs Registered")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.legend(title="Jenis Pengguna")
    st.pyplot(fig)
