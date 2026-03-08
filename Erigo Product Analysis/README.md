# Analisis Data Produk Erigo

## 📌 Deskripsi Projek
Projek ini bertujuan untuk mengumpulkan dan mengolah data produk dari toko Erigo. Data dikumpulkan menggunakan teknik web scraping, kemudian dibersihkan dan diproses menggunakan Python sebelum disimpan untuk dikelolah di PgAdmin

--

## 🎯 Tujuan Projek
Tujuan utama dari pyojek ini adalah:
- Mengumpulkan data sebanyak 50 produk dari toko Erigo
- Mengolah dan memberishkan data
- Menyimpan data ke dalam datasbase untuk dilanjutkan ke PostgreSQL

---

## 🧰 Tools
- Python
- Pandas
- Selenium
- Beautifulsoup
- PostgreSQL

---

## 🔎 Pengambilan Data
Data produk Erigo diambil menggunakan teknik Web Scraping. Proses ini dilakukan dengan menggunakan Selenium untuk membuka halaman website dan BeautifulSoup untuk membaca struktuk HTML.

Beberapa informasi yang dikumpulkan antara lain:
- Nama Produk
- Harga Produk
- Rating Produk
- Jumlah Ulasan

---

Data yang diperoleh kemudian disimpan dalam bentuk file CSV sebagai data mentah.

---

## 🧹 Pengolahan Data
Setelah data berhasil dikumpulkan, langkah selanjutnya adalah melakukan pembersihkan dan pengolahan data menggunakan Pandas.

Proses yang dilakukan meiliputi:
- Memeriksa struktuk dataset
- Membersihkan karakter yang tidak diperlukan
- Mengubah tipe data
- menangani nilai kosong
- menghapus data duplikat

---

## 💾 Penyimpanan Data
Data yang telah diproses kemudian disimpan ke dalam database PostgreSQL. Tahap yang dilakukan meliputi pembuatan database, pembuatan tabel, serta proses import.

---

## 📊 Hasil
Setelah seluruh proses selesai, data produk Erigo berhasil dikumpulkan, dibersihkan dan disimpan ke dalam database. Dataset ini dapat digunakan untuk berbagai analisis.