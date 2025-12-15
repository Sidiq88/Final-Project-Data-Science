# Analisis dan Prediksi Risiko Churn Pelanggan Bank Berbasis Machine Learning

## Project Background
Dalam beberapa tahun terakhir, industri perbankan menghadapi tingkat persaingan yang semakin tinggi akibat berkembangnya layanan digital banking, fintech, dan kebutuhan pelanggan yang semakin dinamis. Kondisi ini membuat pelanggan semakin mudah berpindah bank jika merasa layanan tidak memenuhi ekspektasi, seperti biaya administrasi yang tinggi, proses transaksi lambat, kualitas layanan kurang memadai, atau tidak adanya program loyalitas yang menarik.

Dataset Bank Customer Churn yang tersedia memberikan informasi profil pelanggan seperti usia, pendapatan, status keanggotaan, aktivitas transaksi, dan perilaku finansial. Data ini dapat dieksplorasi untuk membangun model prediksi churn yang dapat membantu pengambilan keputusan berbasis data.

## Problem Statement

Bank tidak memiliki sistem yang mampu mengidentifikasi pelanggan mana yang paling berisiko churn secara akurat. 
Masalah utamanya adalah
1. Bank tidak memiliki mekanisme prediktif untuk mengetahui pelanggan mana yang berpotensi churn.
2. Retensi dilakukan tanpa segmentasi, menyebabkan biaya kampanye meningkat dan efektivitas menurun.

Maka, pernyataan masalah dapat dirumuskan sebagai berikut

“Bagaimana membangun model prediksi untuk mengidentifikasi pelanggan dengan risiko tinggi melakukan churn berdasarkan data profil dan perilaku pelanggan, sehingga tim bisnis dapat melakukan tindakan retensi secara tepat sasaran dan efisien?”

## Conclucison
1. Tingkat churn tergolong tinggi
    Jumlah customer yang tidak churn (79.63%) lebih banyak dibanding churn (20.37%).
2. Perbedaan pola churn berdasarkan demografi dan karakteristik nasabah
    Gender male lebih banyak tidak churn (57.25%) dan female lebih banyak churn (55.92%).
    Country France lebih banyak yang tidak Churn (52.79%).
3. Nasabah aktif lebih loyal 
    Member yang aktif lebih banyak yang tidak churn (55.46%). 
4. Churn tertinggi terjadi pada kelompok usia 49 sampai 57 tahun
5. Customer yang baru atau sudah lama menjadi nasabah banyak tidak churn
6. High-value customers (saldo tinggi) juga rentan churn. 
    Terdapat 10 customer dengan saldo rekening terbanyak yang churn.
7. Nasabah dengan jumlah produk sedikit (product number = 1) lebih mudah churn

## Recommendation
1. Segmentasi pelanggan berbasis risiko dan budget:
    a. Low-risk customers lakukan automated nurturing (email, promo ringan)
    b. Medium-risk lakukan edukasi produk & upselling personal
    c. High-risk lakukan intervensi langsung oleh relationship manager

2. Buat program loyalitas atau produk yang lebih menarik bagi nasabah wanita, misalnya:
    a. Program finansial untuk keluarga dan  investasi jangka Panjang
    b. Edukasi investasi dan manajemen keuangan untuk wanita profesional.

3. Evaluasi mengapa negara lain memiliki churn lebih tinggi perlu lakukan perbaikan lokal.

4. Ciptakan produk khusus segmen  usia lebih dari 45: Perencanaan pension, Income protection, Konsultasi finansial personal

5. Implementasikan VIP Retention Program: Dedicated relationship manager, Prioritas pelayanan, Tingkat bunga lebih kompetitif, Produk wealth management khusus.

6. . Evaluasi mengapa nasabah hanya menggunakan 1 produk sehingga churn lebih tinggi perlu lakukan perbaikan pelayanan.


