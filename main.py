import tkinter as tk
import math

equation = ""
window = tk.Tk()      #Create Tkinter object
#window.geometry("800x500")      #Create tk window this size
window.resizable(True, True)   #Users can resize the window
window.title("Calculatinator")
window.config(bg='#7C3030')

input_txt = tk.Text(window, height=1, width=16, font=("Arial", 24), relief=tk.SUNKEN)  # Create text box
input_txt.grid(row=0, columnspan=7, pady=30, padx=30)  # Place text box at top of window with x-axis autoscale
input_txt.config(bg="#C2B280")

def add_to_calculation(symbol):
    global equation
    equation += str(symbol)  #Convert to string, then append
    input_txt.delete(1.0, "end")  # delete contents of text field
    input_txt.insert(1.0, equation)  #Insert new contents

def evaluate_calculation():
    global equation
    try:
        equation = str(eval(equation))  #Major Security vulnerability!  ###### Fix before any hosting!
        input_txt.delete(1.0, "end")
        input_txt.insert(1.0, equation)
    except:
        clear_field()
        input_txt.insert(1.0, "Error")

def clear_field():          #C button
    global equation
    equation = ""
    input_txt.delete(1.0, "end")

def run():
    window.mainloop()

def delete():
    global equation
    input_txt.delete("end-2c", "end") #Delete last character in input_txt
    equation = equation[:-1] #Delete last character in equation string

      ##########     Row 1
btn_c = tk.Button(window, text="c", command=clear_field, width=10)
btn_c.grid(column=0, row=1)
btn_del = tk.Button(window, text="del", command=delete, width=10)
btn_del.grid(row=1, column=1)
btn_eq = tk.Button(window, text="=", command=evaluate_calculation, width=10)
btn_eq.grid(row=1, column=2)
btn_fp = tk.Button(window, text="(", command=lambda: add_to_calculation("("), width=10)
btn_fp.grid(row=1, column=3)
btn_sp = tk.Button(window, text=")", command=lambda: add_to_calculation(")"), width=10)
btn_sp.grid(row=1, column=4)
            ############   Row 2
btn_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=10)
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=10)
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=10)
btn_9.grid(row=2, column=2)
btn_div = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width=10)
btn_div.grid(row=2, column=3)
btn_mult = tk.Button(window, text="X", command=lambda: add_to_calculation("*"), width=10)
btn_mult.grid(row=2, column=4)
           ############    Row 3
btn_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=10)
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=10)
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=10)
btn_6.grid(column=2, row=3)
btn_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=10)
btn_plus.grid(row=3, column=3)
btn_min = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=10)
btn_min.grid(row=3, column=4)
             ############ Row 4
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=10)
btn_1.grid(row=4, column=0)
btn_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=10)
btn_2.grid(row=4, column=1)
btn_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=10)
btn_3.grid(row=4, column=2)
btn_exp = tk.Button(window, text="^", command=lambda: add_to_calculation("**"), width=10)
btn_exp.grid(row=4, column=3)
btn_mod = tk.Button(window, text="mod", command=lambda: add_to_calculation("%"), width=10)
btn_mod.grid(row=4, column=4)
             ########### Row 5
btn_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=10)
btn_0.grid(row=5, column=0)
btn_dot = tk.Button(window, text=".", command=lambda: add_to_calculation("."), width=10)
btn_dot.grid(row=5, column=1)
btn_pi = tk.Button(window, text="π", command=lambda: add_to_calculation(math.pi), width=10)
btn_pi.grid(row=5, column=2)
btn_sqrt = tk.Button(window, text="sqrt", command=lambda: add_to_calculation("math.sqrt("), width=10)
btn_sqrt.grid(row=5, column=3)
btn_log = tk.Button(window, text="log", command=lambda: add_to_calculation("math.log("), width=10)
btn_log.grid(row=5, column=4)


if __name__ == '__main__':
    run()