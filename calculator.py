import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")

        self.entry = tk.Entry(root, width=25, font=("Arial", 18))
        self.entry.pack(pady=20)

        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack()

        # Define buttons
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'log',
            '0', '.', '=', '+', 'sin',
            'cos', 'tan', 'C'
        ]

        row, col = 0, 0
        for btn in buttons:
            action = lambda x=btn: self.on_button_click(x)
            tk.Button(button_frame, text=btn, width=8, height=2,
                      command=action).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'sqrt':
            try:
                value = float(self.entry.get())
                result = math.sqrt(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char == 'pow':
            self.entry.insert(tk.END, '**')
        elif char == 'log':
            try:
                value = float(self.entry.get())
                result = math.log10(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        elif char in ['sin', 'cos', 'tan']:
            try:
                value = float(self.entry.get())
                radians = math.radians(value)
                if char == 'sin':
                    result = math.sin(radians)
                elif char == 'cos':
                    result = math.cos(radians)
                elif char == 'tan':
                    result = math.tan(radians)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {e}")
        else:
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    calc = AdvancedCalculator(root)
    root.mainloop()
