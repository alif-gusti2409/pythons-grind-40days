import tkinter as tk

root=tk.Tk()
root.title("belajar tkinter")
root.geometry("300x200")

label = tk.Label(root,text="halo, dunia", font=("time news roman ", 14))
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

def sapa():
    nama = entry.get()
    label.config(text=f"halo {nama}, selamat datang!")

btn = tk.Button(root, text="klik aku", command=sapa)
btn.pack(pady=5)

btn_quit = tk.Button(root, text="keluar", command=root.quit)
btn_quit.pack(pady=5)
root.mainloop()