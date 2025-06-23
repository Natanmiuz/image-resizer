import tkinter as tk
from ui.gui import MainWindow

try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
    pass

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
