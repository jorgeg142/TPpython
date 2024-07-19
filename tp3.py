from turtle import *
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import pickle
from abc import ABC, abstractmethod
import partefuncional  # Importamos nuestro módulo partefuncional.py

# Clase base para las formas que implementa Drawable
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Shape(Drawable):
    def __init__(self, sides):
        self.sides = sides
        self.side_length = 600 / sides
        self.colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
                       'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
        self.shape_color = random.choice(self.colors)
        self.border_color = random.choice(self.colors)
        self.border_size = (sides % 20) + 1

    @abstractmethod
    def draw(self):
        pass

class Polygon(Shape):
    def __init__(self, sides):
        super().__init__(sides)
        self.name = f"Polígono de {sides} lados"

    def draw(self):
        try:
            clear()
            angle = 360 / self.sides
            shape("turtle")
            pencolor(self.border_color)
            fillcolor(self.shape_color)
            pensize(self.border_size)

            begin_fill()
            for _ in range(self.sides):
                forward(self.side_length)
                left(angle)
            end_fill()
        except Exception as e:
            messagebox.showerror("Error al dibujar el polígono", str(e))

class PolygonInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de Polígonos")
        self.create_widgets()
        self.polygons = []

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)

        polygons = [("Triángulo", 3), ("Cuadrado", 4), ("Pentágono", 5), 
                    ("Hexágono", 6), ("Heptágono", 7), ("Octágono", 8)]

        for name, sides in polygons:
            button = tk.Button(frame, text=name, command=lambda s=sides: self.create_polygon(s))
            button.pack(side=tk.LEFT, padx=5, pady=5)

        custom_button = tk.Button(frame, text="Personalizado", command=self.custom_polygon)
        custom_button.pack(side=tk.LEFT, padx=5, pady=5)

        save_button = tk.Button(frame, text="Guardar", command=self.save_polygons)
        save_button.pack(side=tk.LEFT, padx=5, pady=5)

        load_button = tk.Button(frame, text="Cargar", command=self.load_polygons)
        load_button.pack(side=tk.LEFT, padx=5, pady=5)

    def determinar_par_impar(self, num_sides):
        comando = f"swipl -s verificar_par_impar.pl -g \"verificar_par_impar({num_sides}), halt.\" -t halt."
        resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)
        salida_prolog = resultado.stdout.strip()
        return salida_prolog
#yo intente usar pydatalog pero me daba muchos errores y luego probe prolog pero no podia importar pyswip me daba errores, recurri a este metodo.
    def create_polygon(self, num_sides):
        polygon = Polygon(num_sides)
        self.polygons.append(polygon)
        polygon.draw()
        resultado = self.determinar_par_impar(num_sides)
        info = (f"Tipo de polígono: {polygon.name}\n"
                f"Color del borde: {polygon.border_color}\n"
                f"Color del interior: {polygon.shape_color}\n"
                f"El número {num_sides} es {resultado}.\n"
                f"Número total de diagonales: {partefuncional.calcular_diagonales(num_sides)}\n"
                f"Medida total de ángulos interiores: {partefuncional.calcular_angulos_interiores(num_sides)} grados\n"
                f"Medida de los ángulos exteriores: {partefuncional.calcular_angulos_exteriores(num_sides)} grados")
        messagebox.showinfo("Información del Polígono", info)

    def custom_polygon(self):
        num_sides = simpledialog.askinteger("Personalizado", "Ingrese el número de lados, más de 3 para continuar:")
        if num_sides and num_sides >= 3:
            self.create_polygon(num_sides)
        else:
            messagebox.showerror("Advertencia", "Número de lados inválido o cancelado")

    def save_polygons(self):
        with open('polygons.pkl', 'wb') as f:
            pickle.dump(self.polygons, f)
        messagebox.showinfo("Guardado", "Polígonos guardados.")

    def load_polygons(self):
        try:
            with open('polygons.pkl', 'rb') as f:
                self.polygons = pickle.load(f)
                messagebox.showinfo("Cargado", "Polígonos cargados correctamente.")
                for polygon in self.polygons:
                    sides = polygon.sides
                    shape_name = f"Polígono de {sides} lados"
                    info = (f"Tipo de polígono: {shape_name}\n"
                            f"Color del borde: {polygon.border_color}\n"
                            f"Color del interior: {polygon.shape_color}\n"
                            f"El número {sides} es {self.determinar_par_impar(sides)}.\n"
                            f"Número total de diagonales: {partefuncional.calcular_diagonales(sides)}\n"
                            f"Medida total de ángulos interiores: {partefuncional.calcular_angulos_interiores(sides)} grados\n"
                            f"Medida de los ángulos exteriores: {partefuncional.calcular_angulos_exteriores(sides)} grados")
                    messagebox.showinfo("Información del Polígono", info)
                    polygon.draw()  # Dibujar el polígono después de mostrar la información

        except FileNotFoundError:
            messagebox.showerror("Advertencia", "No se encontró ningún archivo guardado.")
# Llamada a la clase principal para ejecutar el programa
if __name__ == "__main__":
    setup(width=800, height=800)
    screensize(800, 800)
    PolygonInterface()
    done()
