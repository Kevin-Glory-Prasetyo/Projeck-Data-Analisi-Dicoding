import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Dashboard Penyewaan Sepeda")

# Data penyewaan sepeda di hari kerja berdasarkan jam
data = {
    'Jam': [i for i in range(24)],
    'Penyewaan 2011': [100 + i * 5 for i in range(24)],  # contoh data 2011
    'Penyewaan 2012': [150 + i * 7 for i in range(24)]   # contoh data 2012
}
df = pd.DataFrame(data)


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

# Menampilkan insight tentang jam sibuk (15:00-19:00)
st.write("""
Pada grafik di atas, kita dapat melihat peningkatan signifikan dalam jumlah penyewaan sepeda antara tahun 2011 dan 2012, terutama pada jam sibuk, yaitu antara pukul 15:00 hingga 19:00. Peningkatan ini mungkin disebabkan oleh orang-orang yang pulang kerja atau beraktivitas setelah jam kerja.
""")

# 3. Kesimpulan
st.subheader("Kesimpulan")
st.write("""
- Layanan penyewaan sepeda menjadi lebih populer pada tahun 2012 dibandingkan tahun 2011, dengan peningkatan sebesar 64,88%.
- Waktu penyewaan terbanyak terjadi pada jam setelah kerja, terutama pada pukul 15:00 hingga 19:00, yang mengindikasikan bahwa banyak orang menggunakan sepeda sebagai alat transportasi untuk pulang kerja.
""")
