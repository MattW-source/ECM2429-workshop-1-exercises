import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self, title="Calculator"):
        super().__init__()
        self.title(title)

        self.exp = ""

        bton1 = tk.Button(self, text =' 1 ', font="lucida 20 bold", 
        command = lambda: self.input(1), height = 1, width = 7)
        bton1.grid(row = 2, column = 0, ipady = 4 , ipadx = 2)
        bton2 = tk.Button(self, text = ' 2 ', font="lucida 20 bold",
        command = lambda: self.input(2), height = 1, width = 7)
        bton2.grid(row = 2, column = 1, ipady = 4 , ipadx = 2)
        bton3 = tk.Button(self, text = ' 3 ', font="lucida 20 bold",
        command = lambda: self.input(3), height = 1, width = 7)
        bton3.grid(row = 2, column = 2, ipady = 4 , ipadx = 2)
        bton4 = tk.Button(self, text = ' 4 ', font="lucida 20 bold",
        command = lambda: self.input(4), height = 1, width = 7)
        bton4.grid(row = 3, column = 0, ipady = 4 , ipadx = 2)
        bton5 = tk.Button(self, text = ' 5 ', font="lucida 20 bold",
        command = lambda: self.input(5), height = 1, width = 7)
        bton5.grid(row = 3, column = 1, ipady = 4 , ipadx = 2)
        bton6 = tk.Button(self, text = ' 6 ', font="lucida 20 bold",
        command = lambda: self.input(6), height = 1, width = 7)
        bton6.grid(row = 3, column = 2, ipady = 4 , ipadx = 2)
        bton7 = tk.Button(self, text = ' 7 ', font="lucida 20 bold",
        command = lambda: self.input(7), height = 1, width = 7)
        bton7.grid(row = 4, column = 0, ipady = 4 , ipadx = 2)
        bton8 = tk.Button(self, text = ' 8 ', font="lucida 20 bold",
        command = lambda: self.input(8), height = 1, width = 7)
        bton8.grid(row = 4, column = 1, ipady = 4 , ipadx = 2)
        bton9 = tk.Button(self, text = ' 9 ', font="lucida 20 bold",
        command = lambda: self.input(9), height = 1, width = 7)
        bton9.grid(row = 4, column = 2, ipady = 4 , ipadx = 2)
        bton10 = tk.Button(self, text = ' 0 ', font="lucida 20 bold",
        command = lambda: self.input(0), height = 1, width = 7)
        bton10.grid(row = 5, column = 0, ipady = 4 , ipadx = 2)
        plus = tk.Button(self, text=' + ', font="lucida 20 bold",
        command = lambda: self.input("+"), height=1, width=7)
        plus.grid(row = 2, column = 3, ipady = 4 , ipadx = 2)
        minus = tk.Button(self, text = ' - ', font="lucida 20 bold",
        command = lambda: self.input("-"), height = 1, width = 7)
        minus.grid(row = 3, column = 3, ipady = 4 , ipadx = 2)
        multiply = tk.Button(self, text = ' * ', font="lucida 20 bold",
        command = lambda: self.input("*"), height = 1, width = 7)
        multiply.grid(row = 4, column = 3, ipady = 4 , ipadx = 2)
        divide = tk.Button(self, text=' / ', font="lucida 20 bold",
        command = lambda: self.input("/"), height = 1, width = 7)
        divide.grid(row = 5, column = 3, ipady = 4 , ipadx = 2)
        equal = tk.Button(self, text=' = ', font="lucida 20 bold",
        command = self.solve, height = 1, width = 7)
        equal.grid(row = 5, column = 2, ipady = 4 , ipadx = 2)
        clear = tk.Button(self, text = 'clear', font="lucida 20 bold", 
        command = self.clear, height = 1, width = 7)
        clear.grid(row = 5, column = 0, ipady = 4 , ipadx = 2)
        Decimal = tk.Button(self, text='.', font="lucida 20 bold",
        command = lambda: self.input('.'), height = 1, width = 7)
        Decimal.grid(row = 5, column = 1, ipady = 4 , ipadx = 2)

    def input(self, ch):
        self.exp += str(ch)
        print(self.exp)

    def clear(self):
        self.exp = ""

    def solve(self):
        print("solving... ", self.exp)
        self.exp = ""

    def keyboard(self, inkey):
        ''' Handle keyboard input here.
        Is this the right choice?  Also have the option to bind to individual keys.
        '''
        print(inkey)

if __name__ == "__main__":
    calc = Calculator()
    calc.bind('<Key>', calc.keyboard)
    calc.mainloop()
