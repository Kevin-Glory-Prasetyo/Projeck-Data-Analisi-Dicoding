import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset
hari = "https://raw.githubusercontent.com/Kevin-Glory-Prasetyo/Projek-Data-Analisis-Dicoding/refs/heads/main/day.csv"
data_hari = pd.read_csv(hari)

# Pastikan kolom 'dteday' bertipe datetime
data_hari['dteday'] = pd.to_datetime(data_hari['dteday'])

# Widget kalender untuk menentukan rentang tanggal
start_date = st.date_input('Select Start Date', value=data_hari['dteday'].min())
end_date = st.date_input('Select End Date', value=data_hari['dteday'].max())

# Filter data berdasarkan rentang tanggal
filtered_data = data_hari[(data_hari['dteday'] >= pd.to_datetime(start_date)) & (data_hari['dteday'] <= pd.to_datetime(end_date))]


# Judul aplikasi
st.title('Analisis Penyewaan Sepeda')

# Analisis rata-rata penyewaan sepeda berdasarkan kategori kecepatan angin
avg_windspeed = data_hari.pivot_table(values=['casual', 'registered', 'cnt'], 
                                      index='windspeed', 
                                      aggfunc='mean')

st.subheader('Rata-rata Penyewaan Sepeda Berdasarkan Kecepatan Angin')
st.write(avg_windspeed)
st.subheader('Pengaruh Kecepata Angin Terhadap Penyewaan Sepeda')
# Membuat scatter plot untuk melihat hubungan antara windspeed dengan jumlah penyewaan sepeda
plt.figure(figsize=(12, 6))
sns.scatterplot(x='windspeed', y='casual', data=data_hari, color='blue', label='Casual', alpha=0.6)
sns.scatterplot(x='windspeed', y='registered', data=data_hari, color='orange', label='Registered', alpha=0.6)

plt.title('Pengaruh Kecepatan Angin terhadap Penyewaan Sepeda (Casual vs Registered)')
plt.xlabel('Kecepatan Angin (Windspeed)')
plt.ylabel('Jumlah Penyewaan')
plt.legend()
plt.grid(True)
st.pyplot(plt)




# Menghitung rata-rata penyewaan sepeda berdasarkan suhu
temp_avg = data_hari.groupby('temp')[['casual', 'registered']].mean().reset_index()

# Membuat line plot
plt.figure(figsize=(12, 6))

# Line plot untuk pengguna casual
plt.plot(temp_avg['temp'], temp_avg['casual'], color='blue', label='Casual', marker='o')

# Line plot untuk pengguna registered
plt.plot(temp_avg['temp'], temp_avg['registered'], color='green', label='Registered', marker='o')


st.subheader('Pengaruh Suhu  Terhadap Penyewaan Sepeda')

# Mengatur label dan judul
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Suhu')
plt.xlabel('Suhu (Temp)')
plt.ylabel('Rata-rata Penyewaan Sepeda')
plt.legend()
plt.grid()
st.pyplot(plt)
