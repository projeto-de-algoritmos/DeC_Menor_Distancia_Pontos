import tkinter as tk
from tkinter import ttk, messagebox
import math

class ClosestPairGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menor distância entre pontos")
        self.geometry("400x400")

        self.points = []

        self.instructions = ttk.Label(self, text="Insira um ponto no formato x,y:")
        self.instructions.pack()

        self.point_entry = ttk.Entry(self)
        self.point_entry.pack()

        self.add_button = ttk.Button(self, text="Adicionar ponto", command=self.add_point)
        self.add_button.pack()

        self.calculate_button = ttk.Button(self, text="Calcular menor distância entre pares", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

    def add_point(self):
        point_str = self.point_entry.get()
        try:
            x, y = map(int, point_str.split(","))
            self.points.append((x, y))
            self.result_label["text"] = f"Pontos: {self.points}"
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, insira o ponto no formato x,y")


if __name__ == "__main__":
    app = ClosestPairGUI()
    app.mainloop()
