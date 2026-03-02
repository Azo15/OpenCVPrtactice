import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class FiltreUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Görüntü Yumuşatıcı - 4 Filtre Testi")
        
        self.orjinal_resim = None
        self.islenmis_resim = None

        # --- Arayüz Bileşenleri ---
        self.buton_sec = tk.Button(pencere, text="Gözat (Resim Seç)", command=self.resim_yukle, bg="lightblue")
        self.buton_sec.pack(pady=10)

        self.filtre_var = tk.StringVar(value="blur")
        filtre_cerceve = tk.LabelFrame(pencere, text="Filtre Yöntemi Seçin")
        filtre_cerceve.pack(padx=10, pady=5)
        
        # Dokümanda belirtilen 4 yumuşatma fonksiyonu [cite: 181]
        tk.Radiobutton(filtre_cerceve, text="Averaging", variable=self.filtre_var, value="blur", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Gaussian", variable=self.filtre_var, value="gaussian", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Median", variable=self.filtre_var, value="median", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Bilateral", variable=self.filtre_var, value="bilateral", command=self.filtre_uygula).pack(side=tk.LEFT)

        self.kernel_label = tk.Label(pencere, text="Kernel Boyutu: 5")
        self.kernel_label.pack()
        
        self.trackbar = tk.Scale(pencere, from_=1, to=51, orient=tk.HORIZONTAL, command=self.trackbar_guncelle)
        self.trackbar.set(5)
        self.trackbar.pack(fill=tk.X, padx=20)

        self.panel = tk.Label(pencere, text="Henüz bir resim seçilmedi.")
        self.panel.pack(padx=10, pady=10)

    def resim_yukle(self):
        yol = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.jpg *.jpeg *.png *.bmp")])
        if yol:
            try:
                # Türkçe karakter içeren yolları güvenli okuma yöntemi
                with open(yol, "rb") as f:
                    chunk = f.read()
                arr = np.frombuffer(chunk, dtype=np.uint8)
                self.orjinal_resim = cv2.imdecode(arr, cv2.IMREAD_COLOR)

                if self.orjinal_resim is not None:
                    print(f"Resim yüklendi: {yol}")
                    self.filtre_uygula()
                else:
                    messagebox.showerror("Hata", "Resim dosyası açılamadı!")
            except Exception as e:
                messagebox.showerror("Hata", f"Hata: {e}")

    def trackbar_guncelle(self, val):
        k = int(val)
        if k % 2 == 0: k += 1
        self.kernel_label.config(text=f"Kernel Boyutu: {k}")
        self.filtre_uygula()

    def filtre_uygula(self):
        if self.orjinal_resim is None:
            return

        k = self.trackbar.get()
        if k % 2 == 0: k += 1
        
        mod = self.filtre_var.get()

        if mod == "blur":
            # Averaging (Ortalama) Filtresi [cite: 188, 243]
            self.islenmis_resim = cv2.blur(self.orjinal_resim, (k, k))
        elif mod == "gaussian":
            # Gaussian Filtresi [cite: 250, 252]
            self.islenmis_resim = cv2.GaussianBlur(self.orjinal_resim, (k, k), 0)
        elif mod == "median":
            # Median (Medyan) Filtresi [cite: 264, 266]
            self.islenmis_resim = cv2.medianBlur(self.orjinal_resim, k)
        elif mod == "bilateral":
            # Bilateral (İki Taraflı) Filtre [cite: 277, 283]
            self.islenmis_resim = cv2.bilateralFilter(self.orjinal_resim, k, 75, 75)

        self.resmi_goster(self.islenmis_resim)

    def resmi_goster(self, img):
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