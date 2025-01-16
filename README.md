# Forecasting-Analysis-ARIMA

## **Ringkasan Proyek**
Proyek ini bertujuan untuk memprediksi perubahan persentase harga saham harian menggunakan data historis. Algoritma yang digunakan adalah **Linear Regression** untuk menganalisis hubungan antara fitur saham utama dengan variabel target, `chg(close)`.

---

## **Deskripsi Dataset**
Dataset mencakup data harga saham historis dengan kolom utama:
- `Date`: Tanggal perdagangan.
- `Open`, `High`, `Low`: Harga pembukaan, tertinggi, dan terendah.
- `Close`: Harga penutupan.
- `chg(close)`: Perubahan persentase harga penutupan harian (dihitung).

---

## **Alur Proyek**

1. **Preprocessing Data**
   - Mengimpor dataset dan mengubah kolom `Date` ke format datetime.
   - Menghitung perubahan persentase (`chg(close)`) dan menghapus data yang tidak valid.

2. **Pemilihan Fitur**
   - Fitur: `Open`, `High`, `Low`.
   - Target: `chg(close)`.

3. **Pembagian Data**
   - Data dibagi menjadi **training** (80%) dan **testing** (20%).

4. **Pelatihan Model**
   - Melatih model **Linear Regression** menggunakan data training.

5. **Prediksi dan Visualisasi**
   - Menggunakan model untuk memprediksi `chg(close)` pada data testing.
   - Membandingkan hasil prediksi dengan data aktual menggunakan grafik.

---

## **Teknologi yang Digunakan**
- **Bahasa Pemrograman**: Python.
- **Library**:
  - `pandas`: Manipulasi data.
  - `numpy`: Operasi numerik.
  - `matplotlib`: Visualisasi data.
  - `scikit-learn`: Algoritma **Linear Regression**.

---

## **Cara Menjalankan Proyek**
1. Pastikan Python sudah terinstal.
2. Instal library yang dibutuhkan:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
3. Simpan dataset (`stock_data.csv`) di direktori proyek.
4. Jalankan skrip untuk menghasilkan prediksi:
   ```bash
   python stock_prediction.py
   ```

---

## **Hasil dan Pengembangan**
- **Hasil**: Model memberikan pemahaman awal terhadap perubahan harga saham berdasarkan fitur yang dipilih.
- **Pengembangan**:
  - Uji algoritma lain seperti **Random Forest** untuk meningkatkan akurasi.
  - Tambahkan fitur baru seperti volume perdagangan atau indikator keuangan eksternal.
  - Gunakan metrik evaluasi seperti **MAE** atau **RMSE**.

