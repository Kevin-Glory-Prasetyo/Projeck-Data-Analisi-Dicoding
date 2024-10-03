import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs Github tempat data csv disimpan
hari = "https://raw.githubusercontent.com/Kevin-Glory-Prasetyo/Projek-Data-Analisis-Dicoding/refs/heads/main/day.csv"
jam = "https://raw.githubusercontent.com/Kevin-Glory-Prasetyo/Projek-Data-Analisis-Dicoding/refs/heads/main/hour.csv"

# Load data file csv
day_df = pd.read_csv(hari)
hour_df = pd.read_csv(jam)

# Lakukan filter data khusus untuk "WORKING DAY"
working_day_data = hour_df[hour_df['workingday'] == 1]

# Kelompokkan data peminjaman sepeda dan jumlahkan masing" datanya  dan untuk data tahun 2021 menggunakan "yr" == 0  dan untuk data tahun 2012 menggunakan "yr" == 1 
rental_by_hour_2011 = working_day_data[working_day_data['yr'] == 0].groupby('hr')['cnt'].sum()
rental_by_hour_2012 = working_day_data[working_day_data['yr'] == 1].groupby('hr')['cnt'].sum()

# Combine into a DataFrame
df = pd.DataFrame({
    'Jam': rental_by_hour_2011.index,
    'Penyewaan 2011': rental_by_hour_2011.values,
    'Penyewaan 2012': rental_by_hour_2012.values
})

# Membuat Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

# 1. Visualisasi penyewaan sepeda di hari kerja berdasarkan jam
st.subheader("Penyewaan Sepeda di Hari Kerja Berdasarkan Jam")
fig1, ax1 = plt.subplots()
ax1.plot(df['Jam'], df['Penyewaan 2011'], marker='o', label='2011')
ax1.plot(df['Jam'], df['Penyewaan 2012'], marker='o', label='2012')
ax1.set_title('Penyewaan Sepeda per Jam di Hari Kerja')
ax1.set_xlabel('Jam')
ax1.set_ylabel('Jumlah Penyewaan')
ax1.legend()
ax1.grid(True)

# Tampilkan grafik di Streamlit
st.pyplot(fig1)

# 2. Peningkatan jumlah penyewaan antara tahun 2011 dan 2012
st.subheader("Peningkatan Penyewaan Sepeda antara Tahun 2011 dan 2012")
df['Peningkatan'] = df['Penyewaan 2012'] - df['Penyewaan 2011']
st.line_chart(df[['Jam', 'Peningkatan']].set_index('Jam'))

# Menampilkan Informasi  tentang jam sibuk (15:00-19:00)
st.write("""
Pada grafik di atas, kita dapat melihat peningkatan signifikan dalam jumlah penyewaan sepeda antara tahun 2011 dan 2012, terutama pada jam sibuk, yaitu antara pukul 15:00 hingga 19:00. Peningkatan ini mungkin disebabkan oleh orang-orang yang pulang kerja atau beraktivitas setelah jam kerja.
""")

# 3. Kesimpulan
st.subheader("Kesimpulan")
st.write("""
- Layanan penyewaan sepeda menjadi lebih populer pada tahun 2012 dibandingkan tahun 2011.
- Waktu penyewaan terbanyak terjadi pada jam setelah kerja, terutama pada pukul 15:00 hingga 19:00, yang mengindikasikan bahwa banyak orang menggunakan sepeda sebagai alat transportasi untuk pulang kerja.
""")
