
# Proyek Analisis Data Peminjaman Sepeda
## Deskripsi
Proyek ini bertujuan untuk menganalisis data peminjaman sepeda menggunakan teknik analisis dan visualisasi. Analisis meliputi pemahaman pola peminjaman berdasarkan faktor waktu dan peningkatan peminjaman antara dua tahun. Dashboard interaktif juga disediakan untuk memvisualisasikan data dan mendapatkan insight yang lebih baik.

## Fitur Utama
1. **Visualisasi Penyewaan Sepeda Berdasarkan Jam**: 
   - Menampilkan grafik penyewaan sepeda di hari kerja berdasarkan jam untuk tahun 2011 dan 2012.
   
2. **Peningkatan Penyewaan Sepeda antara Tahun 2011 dan 2012**: 
   - Menunjukkan grafik peningkatan jumlah penyewaan sepeda antara dua tahun, terutama pada jam sibuk (15:00-19:00).
   
3. **Dashboard Interaktif**: 
   - Dashboard yang memungkinkan pengguna melihat tren peminjaman sepeda dan analisis interaktif.
   
4. **Kesimpulan Penggunaan Layanan Sepeda**: 
   - Menyediakan insight mengenai peningkatan popularitas layanan sepeda, terutama pada waktu setelah jam kerja.

## Library yang Digunakan
- **Pandas**: Untuk pengolahan dan analisis data.
- **NumPy**: Untuk operasi numerik.
- **Matplotlib**: Untuk membuat visualisasi data.
- **Streamlit**: Untuk membuat dashboard interaktif.

## Instalasi

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Buat dan aktifkan virtual environment**:
   - Untuk macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Untuk Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

1. Jalankan perintah berikut di terminal untuk memulai dashboard:
   ```bash
   streamlit run app.py
   streamlit run Dashboard/Dashboard.py # Jika Berada di penyimpanan Local
   
   ```

2. Aplikasi akan berjalan di browser Anda secara otomatis dan menampilkan dashboard interaktif dengan data peminjaman sepeda.

## Insight Utama
- Pada tahun 2012, terdapat peningkatan penyewaan sepeda sebesar 64.88% dibandingkan tahun 2011.
- Puncak penggunaan sepeda terjadi pada jam 15:00 hingga 19:00, menunjukkan bahwa sepeda menjadi alat transportasi populer bagi orang yang pulang kerja.
- Layanan penyewaan sepeda semakin populer, terutama di waktu setelah jam kerja.

