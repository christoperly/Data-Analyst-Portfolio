# 🚗 BMW Car Sales — Data Pipeline Automation

> **Hacktiv8 Comprehensive Data Analytics Program — Phase 2 Milestone 3**

---

## 📌 Deskripsi Projek

Projek ini membangun sistem otomasi **ETL (Extract, Transform, Load) Pipeline** untuk data penjualan mobil BMW menggunakan **Apache Airflow**, **PySpark**, **Great Expectations**, dan **MongoDB Atlas**.

Pipeline berjalan otomatis setiap Sabtu pukul 09:10–09:30 WIB dan memproses data dari file CSV hingga tersimpan di database NoSQL.

---

## 📦 Dataset

- **Sumber**: [BMW Car Sales Classification Dataset — Kaggle](https://www.kaggle.com/datasets/junaid512/bmw-car-sales-classification-dataset)
- **File**: `BMW_Car_Sales_Classification.csv`
- **Kolom**: `model`, `year`, `region`, `color`, `fuel_type`, `transmission`, `engine_size_l`, `mileage_km`, `price_usd`, `sales_volume`, `sales_classification`

---

## 🛠️ Tech Stack

| Tools | Kegunaan |
|-------|----------|
| **Apache Airflow** | Workflow orchestration & scheduling |
| **PySpark** | Ekstraksi & transformasi data |
| **Great Expectations** | Validasi kualitas data |
| **MongoDB Atlas** | Penyimpanan data (NoSQL) |
| **Python** | Scripting (extract, transform, load) |

---

## ⚙️ Arsitektur Pipeline

```
[extract.py] ──► [transform.py] ──► [load.py]
   PySpark           PySpark          MongoDB Atlas
```

DAG `Tugas_Milestones_3` mengorkestrasi 3 task secara berurutan:

1. **`python_extract`** — Membaca CSV dengan PySpark
2. **`python_transform`** — Cleaning: lowercase kolom, hapus duplikat & null
3. **`python_load`** — Simpan hasil ke MongoDB collection `bmw_car_sales`

**Jadwal**: Setiap Sabtu pukul 09:10, 09:20, 09:30 (`10,20,30 9 * * 6`)

---

## ✅ Great Expectations (7 Validasi)

| # | Expectation | Kolom | Status |
|---|-------------|-------|--------|
| 1 | `expect_column_values_to_not_be_null` | `model` | ✅ |
| 2 | `expect_column_values_to_be_between` | `price_usd` ($30K–$120K) | ✅ |
| 3 | `expect_column_values_to_be_in_set` | `fuel_type` | ✅ |
| 4 | `expect_column_values_to_be_in_type_list` | `price_usd` | ✅ |
| 5 | `expect_column_values_to_not_be_null` | `model` | ✅ |
| 6 | `expect_column_mean_to_be_between` | `price_usd` ($70K–$80K) | ✅ |
| 7 | `expect_column_to_exist` | `year` | ✅ |

---

## 📸 Screenshot

| Komponen | Preview |
|----------|---------|
| MongoDB Atlas | Data 50K dokumen tersimpan di collection `bmw_car_sales` |
| Airflow DAG Grid | 3 success runs, 2 running — rata-rata durasi 3 menit 43 detik |
| Airflow DAG Graph | `python_extract → python_transform → python_load` |

---

## 📁 Struktur Repository

```
├── P2M3_christoper_leonardo_yosseri_GX.ipynb   # Eksplorasi & Great Expectations
├── DAG.py                                       # Airflow DAG
├── extract.py                                   # ETL: Extract (PySpark)
├── transform.py                                 # ETL: Transform (PySpark)
├── load.py                                      # ETL: Load (MongoDB)
├── P2M3_christoper_leonardo_yosseri_MongoDB.png # Screenshot MongoDB
├── P2M3_christoper_leonardo_yosseri_Airflow.png # Screenshot Airflow Grid
├── P2M3_christoper_leonardo_yosseri_GRAPH.png   # Screenshot DAG Graph
└── README.md
```

---

**Christoper Leonardo Yosseri** | Batch CODA-015-RMT | Hacktiv8
