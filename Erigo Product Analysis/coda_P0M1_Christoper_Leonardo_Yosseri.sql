/*
=================================================
Buat DATABASE
=================================================
*/
-- Membuat DATABASE
CREATE DATABASE Data_ERIGO;

-- MEMBUAT TABLE STAGING
CREATE TABLE staging (
    tipe_produk VARCHAR(100),
    nama_produk VARCHAR(255),
    harga NUMERIC,
    rating_produk NUMERIC
);

--Query ini digunakan untuk mencopy data_clean_jualan_erigo.csv untuk dimasukkan dalam "table staging"
COPY staging (tipe_produk, nama_produk, harga, rating_produk)
FROM 'C:\tmp\data_clean_jualan_erigo.csv'
DELIMITER ','
CSV HEADER;

-- Membuat Table PRODUK
CREATE TABLE produk(
	id_produk SERIAL PRIMARY KEY,
	nama_produk VARCHAR(255),
	id_kategori INTEGER REFERENCES kategori(id_kategori),
	harga NUMERIC,
	rating_produk NUMERIC
);

-- Mengambil Data untuk memastikan isi Data
SELECT * FROM staging;
SELECT * FROM kategori;
SELECT * FROM produk;

-- Memasukkan Data ke 'KATEGORI'
INSERT INTO kategori(tipe_produk)
SELECT DISTINCT tipe_produk FROM staging;

-- Memasukkan Data ke 'PRODUK'
INSERT INTO produk(nama_produk, id_kategori, harga, rating_produk)
SELECT s.nama_produk, k.id_kategori, s.harga, s.rating_produk
FROM staging s JOIN kategori k 
ON s.tipe_produk = k.tipe_produk;