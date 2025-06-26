import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from core.core import ImageResizer

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Redimensionador de Imágenes")
        self.root.geometry("400x300")
        
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.width = tk.IntVar()
        self.height = tk.IntVar()
        self.scale = tk.DoubleVar(value=1.0)
        self.quality = tk.IntVar(value=85)

        self.create_widgets()
    
    def create_widgets(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Permitir que las columnas se expandan
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=0)

        tk.Label(main_frame, text="Imagen de origen:").grid(row=0, column=0, sticky="w")
        tk.Entry(main_frame, textvariable=self.input_path, width=30).grid(row=0, column=1, sticky="ew")
        tk.Button(main_frame, text="Examinar", command=self.browse_input).grid(row=0, column=2, sticky="ew")

        options_frame = tk.LabelFrame(main_frame, text="Opciones", padx=10, pady=10)
        options_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="we")
        options_frame.grid_columnconfigure(1, weight=1)

        tk.Checkbutton(options_frame, text="Ancho:", variable=self.width, onvalue=800, offvalue=0).grid(row=0, column=0, sticky="w")
        tk.Entry(options_frame, textvariable=self.width, width=8).grid(row=0, column=1, sticky="ew")
        
        tk.Checkbutton(options_frame, text="Alto:", variable=self.height, onvalue=600, offvalue=0).grid(row=1, column=0, sticky="w")
        tk.Entry(options_frame, textvariable=self.height, width=8).grid(row=1, column=1, sticky="ew")
        
        tk.Label(options_frame, text="Escala:").grid(row=2, column=0, sticky="w")
        tk.Entry(options_frame, textvariable=self.scale, width=8).grid(row=2, column=1, sticky="ew")
        
        tk.Label(options_frame, text="Calidad:").grid(row=3, column=0, sticky="w")
        tk.Scale(options_frame, from_=1, to=100, variable=self.quality, orient=tk.HORIZONTAL).grid(row=3, column=1, sticky="ew")

        tk.Button(main_frame, text="Redimensionar", command=self.resize).grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
    
    def browse_input(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.webp")]
        )
        if filepath:
            self.input_path.set(filepath)
            path = Path(filepath)
            self.output_path.set(str(path.parent / f"{path.stem}_resized{path.suffix}"))
    
    def resize(self):
        try:
            new_width, new_height = ImageResizer.resize_image(
                input_path=self.input_path.get(),
                output_path=self.output_path.get(),
                width=self.width.get() or None,
                height=self.height.get() or None,
                scale=self.scale.get() or None,
                quality=self.quality.get()
            )
            messagebox.showinfo("Éxito", f"Imagen redimensionada a {new_width}x{new_height}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo redimensionar:\n{str(e)}")