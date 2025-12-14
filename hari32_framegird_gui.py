import tkinter as tk 

root = tk.Tk()
root.title("login form")

frame = tk .Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="username:").grid(row=0, column=0)
tk.Label(frame, text="password:").grid(row=1, column=0)

user = tk.Entry(frame)
user.grid(row=0 , column=1)
pwd = tk.Entry(frame, show="*")
pwd.grid(row=1, column=1)

def login():
    username = user.get()
    password = pwd.get()
    print(f"username: {username}, password: {password}")
    
    if username == "admin" and password == "12345":
        print("login berhasil")
    else:
        print("login gagal")
    

tk.Button(frame, text="login", command=login).grid(row=2, columnspan=2, pady=5)

root.mainloop()