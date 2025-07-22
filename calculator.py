#simple calculator 
import tkinter as tk
import math


def click(event):
    text = event.widget.cget("text")  
    current_text = entry.get()

    if text == "=":
        try:
            
            expression = current_text.replace("^", "**").replace("√", "math.sqrt").replace("%", "/100")
            
            
            result = str(eval(expression, {"__builtins__": None}, {"math": math}))
            
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    elif text == "C":
        entry.delete(0, tk.END)  

    elif text == "⌫":
        if current_text:  # Avoid error if empty
            entry.delete(len(current_text)-1, tk.END)  

    else:
        entry.insert(tk.END, text)  



root = tk.Tk()
root.title("Calculator by Aditi")
root.geometry("400x500")
root.resizable(0, 0)
root.configure(bg="light pink")


entry = tk.Entry(root, font=("Arial", 50), justify="right", bd=10, relief="flat")
entry.pack(fill=tk.BOTH, ipadx=10, ipady=14, pady=(10, 20), padx=10)

# Define buttons (rows)
buttons = [
    ["C", "⌫", "^", "√"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+", "="]
]


button_frame = tk.Frame(root, bg="lightgray")
button_frame.pack()


for row in buttons:
    row_frame = tk.Frame(button_frame, bg="lightgray")
    row_frame.pack(fill="both", expand=True)

    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), 
                        bg="#333", fg="white", bd=4, relief="raised")
        btn.pack(side="left", fill="both", expand=True, padx=6, pady=6)
        btn.bind("<Button-1>", click)  


root.mainloop()
