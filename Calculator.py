import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")
        self.resizable(0, 0)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        result_entry = tk.Entry(self, textvariable=self.result_var,
								font=('Arial', 20), bd=10,
								insertwidth=2,
								width=14,
								borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button,
					  padx=20,
					  pady=20,
					  font=('Arial', 18),
					  command=button_command).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
            self.result_var.set(self.expression)
            self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
