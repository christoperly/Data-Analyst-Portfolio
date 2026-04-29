# 📊 FinTech Customer Lifetime Value (LTV) Analysis

> **Hacktiv8 Comprehensive Data Analytics Program — Phase 1 Milestone 2**

---

## 🔗 Dashboard & Notebook

| Resource | Link |
|----------|------|
| 📈 Tableau Dashboard | https://public.tableau.com/app/profile/kotak.susu/viz/Book1_17721161891410/Dashboard1?publish=yes |
| 📓 Jupyter Notebook | `digital_wallet_ltv.ipynb` |
| 📦 Dataset | [FinTech Customer LTV Dataset — Kaggle](https://www.kaggle.com/datasets/harunrai/fintech-customer-life-time-value-ltv-dataset) |

---

## 🎯 Deskripsi Projek

Projek ini merupakan analisis data pelanggan di industri **keuangan digital (FinTech)** dengan fokus pada **Customer Lifetime Value (LTV)**. Perusahaan FinTech sedang berupaya meningkatkan retensi pengguna dan pendapatan jangka panjang, namun strategi pemasaran yang ada belum menargetkan segmen pelanggan yang tepat.

Analisis ini menghasilkan insight berbasis data untuk mendukung pengambilan keputusan strategis terkait promosi, segmentasi pengguna, dan peningkatan layanan pelanggan.

---

## 🧩 Problem Statement (SMART Framework)

| Kriteria | Deskripsi |
|----------|-----------|
| **Specific** | Meningkatkan nilai rata-rata Customer Lifetime Value pengguna aplikasi |
| **Measurable** | Target kenaikan sebesar **10%** dari rata-rata LTV saat ini |
| **Achievable** | Dicapai melalui strategi berbasis insight data yang mempengaruhi LTV |
| **Relevant** | Meningkatkan profitabilitas jangka panjang melalui retensi pengguna |
| **Time-Bound** | Target dicapai dalam **5 bulan** ke depan |

> **Pernyataan Masalah**: Meningkatkan Customer Lifetime Value (LTV) rata-rata pengguna sebesar 10% melalui strategi promosi berbasis metode pembayaran dalam kurun waktu 5 bulan ke depan.

---

## ❓ Penjabaran Masalah (5W+1H)

Untuk memecahkan masalah utama, dilakukan penjabaran ke dalam 6 pertanyaan analisis:

| # | Pertanyaan | Metode |
|---|-----------|--------|
| 1 | Wilayah mana yang menyumbang total pendapatan terbesar?
| 2 | Apakah tingkat pendapatan mempengaruhi total pengeluaran?
| 3 | Bagaimana rata-rata transaksi berdasarkan umur pengguna?
| 4 | Metode pembayaran apa yang paling sering digunakan?
| 5 | Apakah pengguna yang sering menghubungi CS memiliki total pengeluaran lebih rendah?
| 6 | Bagaimana distribusi Customer Lifetime Value (LTV) pelanggan?

---

## 📦 Dataset

- **Sumber**: [Kaggle — FinTech Customer Life Time Value (LTV) Dataset](https://www.kaggle.com/datasets/harunrai/fintech-customer-life-time-value-ltv-dataset)
- **Format**: CSV
- **Nama File**: `digital_wallet_ltv_datasetss.csv`

**Kolom utama yang digunakan:**

| Kolom | Keterangan |
|-------|-----------|
| `Customer_ID` | ID unik pelanggan |
| `Age` | Usia pelanggan |
| `Location` | Wilayah domisili (Urban, Suburban, Rural) |
| `Income_Level` | Tingkat pendapatan (Low, Middle, High) |
| `Total_Spent` | Total pengeluaran pelanggan |
| `Avg_Transaction_Value` | Rata-rata nilai transaksi |
| `Preferred_Payment_Method` | Metode pembayaran yang dipilih |
| `Support_Tickets_Raised` | Jumlah tiket customer service |
| `LTV` | Customer Lifetime Value |

---

## 🛠️ Tools & Library

| Kategori | Tools |
|----------|-------|
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Visualisasi** | Matplotlib, Seaborn |
| **Statistik** | SciPy, Scikit-learn |
| **Dashboard** | Tableau Public |
| **Notebook** | Jupyter Notebook |

---

## 🔍 Data Cleaning

Proses pembersihan data yang dilakukan:

- ✅ Tidak ditemukan **missing values** pada seluruh kolom
- ✅ Tidak ditemukan **data duplikat**
- ✅ Konversi tipe data kolom `Total_Spent` dan `LTV` ke tipe `int`
- ✅ Pembulatan nilai numerik ke 2 desimal
- ✅ Pembuatan kolom baru `Age_Group` untuk segmentasi usia

Dataset dinyatakan **bersih dan siap dianalisis**.

---

## 📊 Analisis & Visualisasi

### 1. 🗺️ Total Pendapatan per Wilayah
Visualisasi bar chart untuk melihat kontribusi masing-masing wilayah (Urban, Suburban, Rural) terhadap total pendapatan.

> **Insight**: Wilayah **Suburban** menyumbang pendapatan tertinggi (33.70%), namun selisihnya sangat tipis dengan Urban dan Rural — menandakan bahwa pasar sudah tersebar **sangat merata** di semua wilayah.

---

### 2. 💰 Pengaruh Tingkat Pendapatan terhadap Total Pengeluaran
Menggunakan **Boxplot** dan **One-Way ANOVA** untuk menguji apakah Income Level (Low, Middle, High) berpengaruh signifikan terhadap Total Spent.

**Hipotesis:**
- **H₀**: Tidak ada perbedaan signifikan antara Total_Spent dan Income_Level
- **H₁**: Ada perbedaan signifikan

> **Insight**: Hasil ANOVA menunjukkan **tidak ada perbedaan signifikan** (p-value > 0.05). Pelanggan berpenghasilan rendah maupun tinggi memiliki **pola belanja yang serupa**.

---

### 3. 👥 Rata-rata Transaksi Berdasarkan Kelompok Umur
Segmentasi usia dibagi menjadi 4 kelompok: Remaja (<25), Dewasa Muda (25-45), Dewasa (45-65), Senior (>65).

> **Insight**: Nilai transaksi di semua kelompok umur **relatif stabil dan merata**, menunjukkan bahwa produk memiliki daya tarik yang sama bagi semua generasi.

---

### 4. 💳 Metode Pembayaran yang Paling Sering Digunakan
Bar chart distribusi penggunaan metode pembayaran (UPI, Debit Card, Wallet, dll).

> **Insight**: **UPI** merupakan metode pembayaran yang paling populer, namun Debit Card dan Wallet juga tetap diminati — pengguna menyukai **fleksibilitas** dalam memilih cara membayar.

---

### 5. 🎧 Hubungan Customer Service Tickets & Total Pengeluaran
Scatter plot dan **Pearson Correlation** untuk mengukur hubungan antara jumlah tiket CS dan total pengeluaran.

> **Insight**: Korelasi Pearson = **-0.0297** (p-value = 0.0131). Hubungan sangat lemah — pelanggan yang sering menghubungi CS **tidak terbukti** memiliki pengeluaran yang lebih rendah secara signifikan.

---

### 6. 📈 Distribusi Customer Lifetime Value (LTV) — Statistik Deskriptif
Histogram dengan KDE untuk melihat distribusi LTV pelanggan beserta statistik deskriptif (mean, median, std, min, max).

> **Insight**: Distribusi LTV **miring ke kanan (right-skewed)** — sebagian besar pelanggan memiliki LTV rendah hingga menengah, sementara sebagian kecil memiliki LTV sangat tinggi namun berkontribusi besar.

---

## 📝 Kesimpulan & Rekomendasi

| Temuan | Rekomendasi |
|--------|-------------|
| Pendapatan tersebar merata di semua wilayah | Tidak perlu fokus pada satu wilayah; optimalkan campaign secara nasional |
| Income Level tidak mempengaruhi pengeluaran | Segmentasi berbasis income kurang efektif; cari faktor diferensiasi lain |
| Semua kelompok umur bertransaksi merata | Desain produk bersifat universal; pertahankan inklusivitas fitur |
| UPI dominan, tapi metode lain tetap relevan | Tingkatkan cashback/promo untuk UPI; jaga ketersediaan semua metode |
| CS tickets tidak signifikan kurangi pengeluaran | Fokus pada kualitas CS untuk meningkatkan loyalitas, bukan retensi belanja |
| LTV terdistribusi right-skewed | Identifikasi dan nurture pelanggan High-LTV dengan program loyalitas khusus |

---