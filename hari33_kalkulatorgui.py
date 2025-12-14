import tkinter as tk

root=tk.Tk()
root.title("kalkulator")

entry = tk.Entry(root, width=20, font=("arial",16))
entry.grid(row=0, column=0, columnspan=4)

def klik(tombol):
    if tombol == "=":
        try:
            hasil = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, hasil)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for t in tombol_list:
    tk.Button(root, text=t, width=5, height=2, command=lambda x=t: klik(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()