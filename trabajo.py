from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Lista de productos, stock y precios
productos = [
    {"nombre": "Pollo", "descripcion": "Pollo fresco por kg", "precio": 2240, "stock": 0},
    {"nombre": "Carne novillo", "descripcion": "Carne de novillo por kg", "precio": 10000, "stock": 0},
    {"nombre": "Carne cerdo", "descripcion": "Carne de cerdo por kg", "precio": 9000, "stock": 0},
    {"nombre": "Salmon", "descripcion": "Salmon por kg", "precio": 12000, "stock": 0},
    {"nombre": "Gaseosas", "descripcion": "Gaseosas 2lt", "precio": 2500, "stock": 0},
    {"nombre": "Aguas saborizadas", "descripcion": "Aguas saborizadas 2.25lt", "precio": 2200, "stock": 0},
    {"nombre": "Soda", "descripcion": "Soda 1lt", "precio": 1200, "stock": 0},
    {"nombre": "Vino", "descripcion": "Vino 750 ml", "precio": 3300, "stock": 0},
    {"nombre": "Cerveza", "descripcion": "Cerveza 1lt", "precio": 2100, "stock": 0},
    {"nombre": "Champagne", "descripcion": "Champagne 750ml", "precio": 4500, "stock": 0},
    {"nombre": "Galletas", "descripcion": "Galletas por unidad", "precio": 1000, "stock": 0},
    {"nombre": "Chocolate", "descripcion": "Chocolate por unidad", "precio": 1500, "stock": 0},
    {"nombre": "Pastas", "descripcion": "Pastas por unidad", "precio": 1800, "stock": 0},
    {"nombre": "Snacks", "descripcion": "Snacks por unidad", "precio": 1600, "stock": 0},
    {"nombre": "Mani", "descripcion": "Mani por unidad", "precio": 1000, "stock": 0},
    {"nombre": "Papas fritas", "descripcion": "Papas fritas 249g", "precio": 1200, "stock": 0},
    {"nombre": "Aromatizador", "descripcion": "Aromatizador por unidad", "precio": 1400, "stock": 0},
    {"nombre": "Jabon", "descripcion": "Jabon por unidad", "precio": 2000, "stock": 0},
    {"nombre": "Papel Higienico", "descripcion": "Papel higienico pack de 3", "precio": 6000, "stock": 0},
    {"nombre": "Shampoo", "descripcion": "Shampoo por unidad", "precio": 4800, "stock": 0},
]

# iniciar tkinter
aplicacion = Tk()


# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='alice blue', width=27)
etiqueta_titulo.grid(row=0, column=0)

# tamaÃ±o de la ventana
aplicacion.geometry('1920x1080+0+0')

# titulo de la ventana
aplicacion.title("Supermercado - Control de Stock")

# color de fondo de la ventana
aplicacion.config(bg='#778899')

# Funciones
def actualizar_stock():
    producto_seleccionado = producto_var.get()
    cantidad = cantidad_var.get()
    accion = accion_var.get()

    if not cantidad.isdigit() or int(cantidad) <= 0:
        messagebox.showerror("Error", "La cantidad debe ser un nÃºmero positivo.")
        return

    cantidad = int(cantidad)
    producto = next((p for p in productos if p["nombre"] == producto_seleccionado), None)

    if not producto:
        messagebox.showerror("Error", "Producto no encontrado.")
        return

    if accion == "Agregar stock":
        producto["stock"] += cantidad
    elif accion == "Quitar stock":
        if producto["stock"] >= cantidad:
            producto["stock"] -= cantidad
        else:
            messagebox.showerror("Error", "No hay suficiente stock para quitar.")
            return

    messagebox.showinfo("Ã‰xito", f"Stock de {producto_seleccionado} actualizado.")
    actualizar_tabla_stock()

def actualizar_tabla_stock():
    for fila in tabla_stock.get_children():
        tabla_stock.delete(fila)
    for producto in productos:
        tabla_stock.insert("", "end", values=(
            producto["nombre"],
            producto["descripcion"],
            f"$ {producto['precio']:.2f}",
            producto["stock"]
        ))

def resetear():
    cantidad_var.set('')
    accion_var.set('Agregar stock')
    producto_var.set(productos[0]["nombre"])

# variables
producto_var = StringVar()
cantidad_var = StringVar()
accion_var = StringVar()

# panel derecha
panel_derecha = Frame(aplicacion, relief=FLAT, bg='#778899')
panel_derecha.pack(side=RIGHT, padx=80, expand=True)

# Panel de modificar stock
panel_modificar_stock = Frame(panel_derecha, bd=1, relief=FLAT, bg='#778899')
panel_modificar_stock.pack(expand=True, pady=100)

Label(panel_modificar_stock, text="Producto", font=("Dosis", 14), bg='#778899').grid(row=0, column=0, padx=5, pady=5,)
producto_var.set(productos[0]["nombre"])
productos_dropdown = OptionMenu(panel_modificar_stock, producto_var, *[p["nombre"] for p in productos])
productos_dropdown.grid(row=0, column=1, padx=5, pady=5)

Label(panel_modificar_stock, text="Cantidad", font=("Dosis", 14), bg='#778899').grid(row=1, column=0, padx=5, pady=5,)
Entry(panel_modificar_stock, textvariable=cantidad_var, font=("Dosis", 14), width=10).grid(row=1, column=1, padx=5, pady=5)

Label(panel_modificar_stock, text="AcciÃ³n", font=("Dosis", 14), bg='#778899').grid(row=2, column=0, padx=5, pady=5,)
accion_var.set("Agregar stock")
accion_dropdown = OptionMenu(panel_modificar_stock, accion_var, "Agregar stock", "Quitar stock")
accion_dropdown.grid(row=2, column=1, padx=5, pady=5)

Button(panel_modificar_stock, text="Enviar", font=("Dosis", 14), command=actualizar_stock).grid(row=3, column=0, columnspan=2, pady=10)
Button(panel_modificar_stock, text="Resetear", font=("Dosis", 14), command=resetear).grid(row=4, column=0, columnspan=2, pady=10)

# Panel de stock
panel_stock = Frame(aplicacion, relief=FLAT, bg='#778899')
panel_stock.pack(side=LEFT, padx=20)

# Tabla de productos (Stock)
tabla_stock = ttk.Treeview(panel_stock, columns=("Producto", "Descripcion", "Precio", "Stock"), show="headings", height=20)
tabla_stock.pack()

tabla_stock.heading("Producto", text="Producto")
tabla_stock.heading("Descripcion", text="Descripcion")
tabla_stock.heading("Precio", text="Precio")
tabla_stock.heading("Stock", text="Stock")


actualizar_tabla_stock()

aplicacion.mainloop()