import math
import tkinter as tk
from tkinter import ttk

class Arafat(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Area Calculator")
        self.geometry("550x400")
        self.configure(background="#D8BFD8")

        shapes = ["Square", "Rectangle", "Triangle", "Circle", "Trapezoid", "Sector", "Octagon", "Ellipse", "Parallelogram"]
        self.shape_combo = ttk.Combobox(self, values=shapes)
        self.shape_combo.place(x=150, y=20)
        self.shape_combo.current(0)

        self.length_label = tk.Label(self, text="Length:")
        self.length_label.place(x=20, y=50)
        self.length_field = tk.Entry(self)
        self.length_field.place(x=150, y=50)

        self.width_label = tk.Label(self, text="Width:")
        self.width_label.place(x=20, y=80)
        self.width_field = tk.Entry(self)
        self.width_field.place(x=150, y=80)

        self.base_label = tk.Label(self, text="Base:")
        self.base_label.place(x=20, y=110)
        self.base_field = tk.Entry(self)
        self.base_field.place(x=150, y=110)

        self.height_label = tk.Label(self, text="Height:")
        self.height_label.place(x=20, y=140)
        self.height_field = tk.Entry(self)
        self.height_field.place(x=150, y=140)

        self.side_label = tk.Label(self, text="Side:")
        self.side_label.place(x=20, y=170)
        self.side_field = tk.Entry(self)
        self.side_field.place(x=150, y=170)

        self.radius_label = tk.Label(self, text="Radius:")
        self.radius_label.place(x=20, y=200)
        self.radius_field = tk.Entry(self)
        self.radius_field.place(x=150, y=200)

        self.major_axis_label = tk.Label(self, text="Major Axis:")
        self.major_axis_label.place(x=20, y=230)
        self.major_axis_field = tk.Entry(self)
        self.major_axis_field.place(x=150, y=230)

        self.minor_axis_label = tk.Label(self, text="Minor Axis:")
        self.minor_axis_label.place(x=20, y=260)
        self.minor_axis_field = tk.Entry(self)
        self.minor_axis_field.place(x=150, y=260)

        self.input_unit_label = tk.Label(self, text="Input Unit:")
        self.input_unit_label.place(x=20, y=290)
        units = ["m", "in", "ft", "mm", "dm", "km", "yd", "mi", "cm"]
        self.input_unit_combo = ttk.Combobox(self, values=units)
        self.input_unit_combo.place(x=150, y=290)
        self.input_unit_combo.current(0)

        self.output_unit_label = tk.Label(self, text="Output Unit:")
        self.output_unit_label.place(x=220, y=290)
        self.output_unit_combo = ttk.Combobox(self, values=units)
        self.output_unit_combo.place(x=320, y=290)
        self.output_unit_combo.current(0)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_area)
        self.calculate_button.place(x=20, y=320)

        self.result_area = tk.Text(self, width=30, height=5)
        self.result_area.place(x=260, y=50)
        self.result_area.configure(state='disabled')

    def calculate_area(self):
        input_value = 0

        try:
            input_value = float(self.get_selected_text_field().get())
            input_unit = self.input_unit_combo.get()

            if input_unit == "in":
                input_value *= 0.0254
            elif input_unit == "ft":
                input_value *= 0.3048
            elif input_unit == "mm":
                input_value *= 0.001
            elif input_unit == "dm":
                input_value *= 0.1
            elif input_unit == "km":
                input_value *= 1000
            elif input_unit == "yd":
                input_value *= 0.9144
            elif input_unit == "mi":
                input_value *= 1609.34
            elif input_unit == "cm":
                input_value *= 0.01

        except ValueError:
            self.result_area.configure(state='normal')
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, "Invalid input. Please enter a valid number.")
            self.result_area.configure(state='disabled')
            return

        area = 0
        output_unit = self.output_unit_combo.get()
        shape = self.shape_combo.get()

        if shape == "Square":
            area = input_value ** 2
        elif shape == "Rectangle":
            area = float(self.length_field.get()) * float(self.width_field.get())
        elif shape == "Triangle":
            area = 0.5 * float(self.base_field.get()) * float(self.height_field.get())
        elif shape == "Circle":
            area = math.pi * (float(self.radius_field.get()) ** 2)
        elif shape == "Trapezoid":
            area = 0.5 * (float(self.base_field.get()) + float(self.side_field.get())) * float(self.height_field.get())
        elif shape == "Sector":
            area = (float(self.radius_field.get()) ** 2 * float(self.major_axis_field.get())) / 2
        elif shape == "Octagon":
            area = 2 * (1 + math.sqrt(2)) * float(self.side_field.get()) ** 2
        elif shape == "Ellipse":
            area = math.pi * float(self.major_axis_field.get()) * float(self.minor_axis_field.get())
        elif shape == "Parallelogram":
            area = float(self.base_field.get()) * float(self.height_field.get())

        if output_unit == "in":
            area /= 0.0254
        elif output_unit == "ft":
            area /= 0.3048
        elif output_unit == "mm":
            area /= 0.001
        elif output_unit == "dm":
            area /= 0.1
        elif output_unit == "km":
            area /= 1000
        elif output_unit == "yd":
            area /= 0.9144
        elif output_unit == "mi":
            area /= 1609.34
        elif output_unit == "cm":
            area /= 0.01

        self.result_area.configure(state='normal')
        self.result_area.delete(1.0, tk.END)
        self.result_area.insert(tk.END, f"Area: {area} {output_unit}²")
        self.result_area.configure(state='disabled')

    def get_selected_text_field(self):
        selected_shape = self.shape_combo.get()
        if selected_shape in ["Square", "Rectangle", "Parallelogram"]:
            return self.length_field
        elif selected_shape in ["Triangle", "Trapezoid"]:
            return self.base_field
        elif selected_shape in ["Circle", "Sector"]:
            return self.radius_field
        elif selected_shape == "Octagon":
            return self.side_field
        elif selected_shape == "Ellipse":
            return self.major_axis_field
        else:
            return self.length_field

if __name__ == "__main__":
    app = Arafat()
    app.mainloop()
