import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class FiltreUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Gelişmiş Görüntü Filtreleme")
        
        self.orjinal_resim = None
        self.islenmis_resim = None

        # --- Arayüz Bileşenleri ---
        ust_cerceve = tk.Frame(pencere)
        ust_cerceve.pack(pady=10)

        self.buton_sec = tk.Button(ust_cerceve, text="Gözat (Resim Seç)", command=self.resim_yukle, bg="lightblue", width=15)
        self.buton_sec.pack(side=tk.LEFT, padx=5)

        self.buton_kaydet = tk.Button(ust_cerceve, text="Resmi Kaydet", command=self.resim_kaydet, bg="lightgreen", width=15)
        self.buton_kaydet.pack(side=tk.LEFT, padx=5)

        self.filtre_var = tk.StringVar(value="blur")
        filtre_cerceve = tk.LabelFrame(pencere, text="Filtre / İşlem Seçin")
        filtre_cerceve.pack(padx=10, pady=5)
        
        # Filtre seçenekleri
        filtreler = [
            ("Averaging", "blur"), ("Gaussian", "gaussian"), 
            ("Median", "median"), ("Bilateral", "bilateral"),
            ("Canny Kenar", "canny"), ("Gri Tonlama", "gray"),
            ("Keskinleştir", "sharpen"), ("Laplacian", "laplacian"),
            ("Erosion", "erode"), ("Dilation", "dilate")
        ]

        for text, mode in filtreler:
            tk.Radiobutton(filtre_cerceve, text=text, variable=self.filtre_var, value=mode, command=self.filtre_uygula).pack(side=tk.LEFT, padx=2)

        self.kernel_label = tk.Label(pencere, text="Filtre Gücü (Kernel): 5")
        self.kernel_label.pack()
        
        self.trackbar = tk.Scale(pencere, from_=1, to=51, orient=tk.HORIZONTAL, command=self.trackbar_guncelle)
        self.trackbar.set(5)
        self.trackbar.pack(fill=tk.X, padx=20)

        # --- Parlaklık ve Kontrast Kontrolleri ---
        ayar_cerceve = tk.Frame(pencere)
        ayar_cerceve.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(ayar_cerceve, text="Parlaklık:").pack(side=tk.LEFT)
        self.parlaklik_scale = tk.Scale(ayar_cerceve, from_=-100, to=100, orient=tk.HORIZONTAL, command=lambda x: self.filtre_uygula())
        self.parlaklik_scale.set(0)
        self.parlaklik_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        tk.Label(ayar_cerceve, text="Kontrast:").pack(side=tk.LEFT)
        self.kontrast_scale = tk.Scale(ayar_cerceve, from_=0, to=3, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: self.filtre_uygula())
        self.kontrast_scale.set(1)
        self.kontrast_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.panel = tk.Label(pencere, text="Henüz bir resim seçilmedi.")
        self.panel.pack(padx=10, pady=10)

    def resim_yukle(self):
        yol = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.jpg *.jpeg *.png *.bmp")])
        if yol:
            try:
                with open(yol, "rb") as f:
                    chunk = f.read()
                arr = np.frombuffer(chunk, dtype=np.uint8)
                self.orjinal_resim = cv2.imdecode(arr, cv2.IMREAD_COLOR)

                if self.orjinal_resim is not None:
                    self.filtre_uygula()
                else:
                    messagebox.showerror("Hata", "Resim dosyası açılamadı!")
            except Exception as e:
                messagebox.showerror("Hata", f"Hata: {e}")

    def resim_kaydet(self):
        if self.islenmis_resim is None:
            messagebox.showwarning("Uyarı", "Kaydedilecek işlenmiş bir resim yok!")
            return
            
        yol = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("Tüm Dosyalar", "*.*")])
        if yol:
            # Türkçe karakter desteği için imencode kullanıyoruz
            uzanti = yol.split('.')[-1].lower()
            if uzanti == "jpg": uzanti = "jpeg"
            is_success, buffer = cv2.imencode(f".{uzanti}", self.islenmis_resim)
            if is_success:
                with open(yol, "wb") as f:
                    f.write(buffer)
                messagebox.showinfo("Başarılı", "Resim kaydedildi.")
            else:
                messagebox.showerror("Hata", "Resim kaydedilirken bir sorun oluştu.")

    def trackbar_guncelle(self, val):
        k = int(val)
        if k % 2 == 0: k += 1
        self.kernel_label.config(text=f"Filtre Gücü (Kernel): {k}")
        self.filtre_uygula()

    def filtre_uygula(self):
        if self.orjinal_resim is None:
            return

        k = self.trackbar.get()
        if k % 2 == 0: k += 1
        
        mod = self.filtre_var.get()

        # 1. Filtreyi Uygula
        if mod == "blur":
            img = cv2.blur(self.orjinal_resim, (k, k))
        elif mod == "gaussian":
            img = cv2.GaussianBlur(self.orjinal_resim, (k, k), 0)
        elif mod == "median":
            img = cv2.medianBlur(self.orjinal_resim, k)
        elif mod == "bilateral":
            img = cv2.bilateralFilter(self.orjinal_resim, k, 75, 75)
        elif mod == "canny":
            gray = cv2.cvtColor(self.orjinal_resim, cv2.COLOR_BGR2GRAY)
            img = cv2.Canny(gray, k*2, k*5)
        elif mod == "gray":
            img = cv2.cvtColor(self.orjinal_resim, cv2.COLOR_BGR2GRAY)
        elif mod == "sharpen":
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            img = cv2.filter2D(self.orjinal_resim, -1, kernel)
        elif mod == "laplacian":
            laplacian = cv2.Laplacian(self.orjinal_resim, cv2.CV_64F)
            img = cv2.convertScaleAbs(laplacian)
        elif mod == "erode":
            kernel = np.ones((k, k), np.uint8)
            img = cv2.erode(self.orjinal_resim, kernel, iterations=1)
        elif mod == "dilate":
            kernel = np.ones((k, k), np.uint8)
            img = cv2.dilate(self.orjinal_resim, kernel, iterations=1)
        else:
            img = self.orjinal_resim.copy()

        # 2. Parlaklık ve Kontrast Ayarlarını Uygula
        alpha = self.kontrast_scale.get()
        beta = self.parlaklik_scale.get()
        self.islenmis_resim = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

        self.resmi_goster(self.islenmis_resim)

    def resmi_goster(self, img):
        if len(img.shape) == 2: # Eğer gri tonlamaysa RGB'ye çevir ki PIL gösterebilsin
            img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((700, 500))
        img_tk = ImageTk.PhotoImage(img_pil)
        self.panel.config(image=img_tk, text="")
        self.panel.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = FiltreUygulamasi(root)
    root.mainloop()