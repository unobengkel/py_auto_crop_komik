Berikut adalah file `README.md` yang lengkap dan terstruktur untuk proyek Anda. Anda bisa menyalin teks ini ke dalam file bernama `README.md` di folder proyek Anda.

```markdown
# Comic Panel Auto-Cropper

Alat bantu berbasis Python untuk memotong halaman komik secara otomatis menjadi panel-panel terpisah. Program ini menggunakan pustaka **OpenCV** untuk mendeteksi garis batas panel dan melakukan *cropping* secara akurat.

## Fitur
* **Batch Processing:** Memproses semua gambar dalam folder input sekaligus.
* **Organisasi Otomatis:** Membuat folder terpisah untuk setiap file gambar agar file hasil potongan rapi.
* **Deteksi Kontur:** Menggunakan deteksi tepi (edge detection) untuk mengenali batas panel secara otomatis.

## Prasyarat
Anda perlu menginstal Python dan pustaka OpenCV.

1. Install Python (jika belum ada).
2. Install OpenCV melalui terminal/command prompt:
   ```bash
   pip install opencv-python

```

## Struktur Proyek

```text
/proyek-anda
│
├── crop.py              # Skrip utama pemotong gambar
├── README.md            # Dokumentasi ini
├── input_folder/        # Letakkan file komik Anda di sini
└── output_folder/       # Hasil potongan akan otomatis masuk ke sini

```

## Cara Penggunaan

1. **Siapkan Gambar:** Letakkan file komik (PNG/JPG) ke dalam folder `input_folder`.
2. **Konfigurasi Path:** Buka file `script.py` dan ubah variabel `input_folder` dan `output_folder` sesuai dengan direktori di komputer Anda:
```python
input_folder = 'C:/path/ke/input_folder'
output_folder = 'C:/path/ke/output_folder'

```


3. **Jalankan Skrip:**
```bash
python crop.py

```


4. **Hasil:** Cek folder `output_folder`. Program akan membuat sub-folder dengan nama yang sama dengan file asli, berisi file `panel_1.png`, `panel_2.png`, dst.

## Kustomisasi

Jika deteksi panel kurang akurat (misalnya karena komik terlalu bersih atau resolusinya kecil), Anda bisa mengubah parameter di dalam `script.py`:

* **Thresholding:** Mengubah `50` pada `cv2.threshold(gray, 50, 255, ...)` dapat membantu jika gambar memiliki *background* yang tidak putih bersih.
* **Filter Ukuran:** Ubah nilai `200` pada `if w > 200 and h > 200:` jika Anda ingin mendeteksi panel yang ukurannya lebih kecil atau lebih besar.

## Lisensi

Proyek ini bersifat open source dan dapat digunakan untuk kebutuhan pribadi maupun komersial.

```

```
