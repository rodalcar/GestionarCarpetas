import os
import tkinter as tk
from tkinter import filedialog, messagebox

def ocultar_carpeta():
    ruta = entry_ruta.get()
    if not ruta:
        messagebox.showwarning("Advertencia", "Por favor selecciona una carpeta.")
        return

    if os.name == 'nt':
        try:
            resultado = os.system(f'attrib +h +s "{ruta}"')
            if resultado == 0:
                messagebox.showinfo("Éxito", f"La carpeta '{ruta}' ahora está oculta.")
            else:
                messagebox.showerror("Error", "No se pudo ocultar la carpeta.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Sistema no compatible", "Este programa solo funciona en Windows.")

def mostrar_carpeta():
    ruta = entry_ruta.get()
    if not ruta:
        messagebox.showwarning("Advertencia", "Por favor selecciona una carpeta.")
        return

    if os.name == 'nt':
        try:
            resultado = os.system(f'attrib -h -s "{ruta}"')
            if resultado == 0:
                messagebox.showinfo("Éxito", f"La carpeta '{ruta}' ahora es visible.")
            else:
                messagebox.showerror("Error", "No se pudo mostrar la carpeta.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Sistema no compatible", "Este programa solo funciona en Windows.")

def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Selecciona una carpeta")
    if ruta:
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, ruta)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestor de Carpetas")
ventana.geometry("500x200")
ventana.resizable(False, False)

# Widgets
label = tk.Label(ventana, text="Ruta de la carpeta:")
label.pack(pady=5)

entry_ruta = tk.Entry(ventana, width=60)
entry_ruta.pack()

btn_seleccionar = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta)
btn_seleccionar.pack(pady=5)

frame = tk.Frame(ventana)
frame.pack(pady=10)

btn_ocultar = tk.Button(frame, text="Ocultar", bg="tomato", fg="white", width=15, command=ocultar_carpeta)
btn_ocultar.pack(side=tk.LEFT, padx=10)

btn_mostrar = tk.Button(frame, text="Mostrar", bg="mediumseagreen", fg="white", width=15, command=mostrar_carpeta)
btn_mostrar.pack(side=tk.LEFT, padx=10)

ventana.mainloop()
