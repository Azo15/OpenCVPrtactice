import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class FiltreUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Görüntü Yumuşatıcı - 4 Filtre Testi")
        
        self.orjinal_resim = None
        self.islenmis_resim = None
        self.yol = ""

        # Dosya Seçme Butonu [cite: 308]
        self.buton_sec = tk.Button(pencere, text="Gözat (Resim Seç)", command=self.resim_yukle)
        self.buton_sec.pack(pady=10)

        # 4 Yumuşatma Yöntemi Seçimi [cite: 305]
        self.filtre_var = tk.StringVar(value="blur")
        filtre_cerceve = tk.Frame(pencere)
        filtre_cerceve.pack()
        
        # Filtre seçenekleri: Averaging, Gaussian, Median, Bilateral [cite: 181, 250, 264, 277]
        tk.Radiobutton(filtre_cerceve, text="Averaging", variable=self.filtre_var, value="blur", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Gaussian", variable=self.filtre_var, value="gaussian", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Median", variable=self.filtre_var, value="median", command=self.filtre_uygula).pack(side=tk.LEFT)
        tk.Radiobutton(filtre_cerceve, text="Bilateral", variable=self.filtre_var, value="bilateral", command=self.filtre_uygula).pack(side=tk.LEFT)

        # Kernel boyutu ayarı [cite: 305]
        self.kernel_label = tk.Label(pencere, text="Kernel Boyutu (Tek Sayı): 5")
        self.kernel_label.pack()
        
        # Hatalı olan kısım burada düzeltildi: px=20 -> padx=20
        self.trackbar = tk.Scale(pencere, from_=1, to=51, orient=tk.HORIZONTAL, command=self.trackbar_guncelle)
        self.trackbar.set(5)
        self.trackbar.pack(fill=tk.X, padx=20)

        self.panel = tk.Label(pencere)
        self.panel.pack(padx=10, pady=10)

    def resim_yukle(self):
        self.yol = filedialog.askopenfilename()
        if self.yol:
            self.orjinal_resim = cv2.imread(self.yol)
            self.filtre_uygula()

    def trackbar_guncelle(self, val):
        k = int(val)
        if k % 2 == 0: k += 1
        self.kernel_label.config(text=f"Kernel Boyutu (Tek Sayı): {k}")
        self.filtre_uygula()

    def filtre_uygula(self):
        if self.orjinal_resim is None: return
        k = self.trackbar.get()
        if k % 2 == 0: k += 1
        
        mod = self.filtre_var.get()
        if mod == "blur":
            self.islenmis_resim = cv2.blur(self.orjinal_resim, (k, k)) [cite: 249]
        elif mod == "gaussian":
            self.islenmis_resim = cv2.GaussianBlur(self.orjinal_resim, (k, k), 0) [cite: 261]
        elif mod == "median":
            self.islenmis_resim = cv2.medianBlur(self.orjinal_resim, k) [cite: 274]
        elif mod == "bilateral":
            # Bilateral filtre gürültüyü azaltırken kenarları korur 
            self.islenmis_resim = cv2.bilateralFilter(self.orjinal_resim, k, 75, 75) [cite: 283]

        self.resmi_goster(self.islenmis_resim)

    def resmi_goster(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((600, 600))
        img_tk = ImageTk.PhotoImage(img_pil)
        self.panel.config(image=img_tk)
        self.panel.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = FiltreUygulamasi(root)
    root.mainloop()