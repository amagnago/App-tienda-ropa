import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd

def agregar_prenda():
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    tipo = entry_tipo.get()
    talle = entry_talle.get()
    color = entry_color.get()
    precio = entry_precio.get()

    if marca and modelo and tipo and talle:
        conn = sqlite3.connect('tienda_ropa.db')
        c = conn.cursor()
        c.execute("INSERT INTO prendas (marca, modelo, tipo, talle, color, precio) VALUES (?, ?, ?, ?, ?, ?)",
                  (marca, modelo, tipo, talle, color, precio))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Prenda agregada correctamente")
        entry_marca.delete(0, tk.END)
        entry_modelo.delete(0, tk.END)
        entry_tipo.delete(0, tk.END)
        entry_talle.delete(0, tk.END)
        entry_color.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Complete los campos obligatorios (marca, modelo, tipo, talle)")

def exportar_a_excel():
    try:
        conn = sqlite3.connect('tienda_ropa.db')
        df = pd.read_sql_query("SELECT * FROM prendas", conn)
        df.to_excel("prendas_tienda.xlsx", index=False)
        conn.close()
        messagebox.showinfo("Éxito", "Datos exportados a 'prendas_tienda.xlsx'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar: {e}")

root = tk.Tk()
root.title("Gestión de Prendas")

tk.Label(root, text="Marca:").grid(row=0, column=0, padx=10, pady=10)
entry_marca = tk.Entry(root)
entry_marca.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Modelo:").grid(row=1, column=0, padx=10, pady=10)
entry_modelo = tk.Entry(root)
entry_modelo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Tipo:").grid(row=2, column=0, padx=10, pady=10)
entry_tipo = tk.Entry(root)
entry_tipo.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Talle:").grid(row=3, column=0, padx=10, pady=10)
entry_talle = tk.Entry(root)
entry_talle.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Color:").grid(row=4, column=0, padx=10, pady=10)
entry_color = tk.Entry(root)
entry_color.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Precio:").grid(row=5, column=0, padx=10, pady=10)
entry_precio = tk.Entry(root)
entry_precio.grid(row=5, column=1, padx=10, pady=10)

tk.Button(root, text="Agregar Prenda", command=agregar_prenda).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Exportar a Excel", command=exportar_a_excel).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()