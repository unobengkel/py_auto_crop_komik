import cv2
import os

def process_comics(input_dir, output_base_dir):
    # Buat folder output utama jika belum ada
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)
        print(f"Folder output utama dibuat: {output_base_dir}")

    # Iterasi setiap file di folder input
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(input_dir, filename)
            
            # Buat nama folder spesifik untuk file ini di dalam folder output utama
            folder_name = os.path.splitext(filename)[0]
            target_output_dir = os.path.join(output_base_dir, folder_name)
            
            # Buat folder spesifik tersebut
            os.makedirs(target_output_dir, exist_ok=True)
            print(f"Memproses: {filename} -> {target_output_dir}")

            # --- Logika Deteksi Panel (OpenCV) ---
            image = cv2.imread(file_path)
            if image is None:
                print(f"Gagal memuat: {filename}")
                continue
                
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
            
            # Temukan kontur
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            panels = []
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                # Filter ukuran (minimal area panel untuk menghindari noise)
                if w > 200 and h > 200:
                    panels.append((x, y, w, h))

            # Urutkan panel (atas-bawah, kiri-kanan)
            panels = sorted(panels, key=lambda p: (p[1], p[0]))

            # Simpan potongan
            for i, (x, y, w, h) in enumerate(panels):
                panel_crop = image[y:y+h, x:x+w]
                save_path = os.path.join(target_output_dir, f"panel_{i+1}.png")
                cv2.imwrite(save_path, panel_crop)
            
            print(f"   -> Berhasil menyimpan {len(panels)} panel.")

# --- KONFIGURASI PATH ---
# Ganti path di bawah ini sesuai lokasi di komputer Anda
input_folder = 'input'
output_folder = 'output'

process_comics(input_folder, output_folder)
