import tkinter as tk
from tkinter import messagebox

def percent_to_mgml():
    try:
        percent = float(entry_percent.get())
        density = float(entry_density.get() or 1.0)
        result = percent * 10 * density
        label_result.config(text=f"{percent}% = {result} mg/ml")
    except ValueError:
        messagebox.showerror("Error", "Numbers only bro 💀")

def mgml_to_percent():
    try:
        mgml = float(entry_mgml.get())
        density = float(entry_density2.get() or 1.0)
        result = mgml / (10 * density)
        label_result2.config(text=f"{mgml} mg/ml = {result}%")
    except ValueError:
        messagebox.showerror("Error", "Numbers only broski")

root = tk.Tk()
root.title("Skincare Converter by Qurisha")
root.geometry("400x400")
root.config(bg="#F5E6FF")

tk.Label(root, text="SKINCARE CONVERTER", font=("Arial", 16, "bold"), bg="#F5E6FF").pack(pady=10)

frame1 = tk.Frame(root, bg="#E0BBFF", padx=10, pady=10)
frame1.pack(pady=10, padx=20, fill="x")
tk.Label(frame1, text="% → mg/ml", bg="#E0BBFF").pack()
entry_percent = tk.Entry(frame1); entry_percent.pack()
entry_density = tk.Entry(frame1); entry_density.insert(0, "1.0"); entry_density.pack()
tk.Button(frame1, text="CONVERT", command=percent_to_mgml, bg="#9B59B6", fg="white").pack(pady=5)
label_result = tk.Label(frame1, text="", bg="#E0BBFF"); label_result.pack(pady=5)

frame2 = tk.Frame(root, bg="#D2B4DE", padx=10, pady=10)
frame2.pack(pady=10, padx=20, fill="x")
tk.Label(frame2, text="mg/ml → %", bg="#D2B4DE").pack()
entry_mgml = tk.Entry(frame2); entry_mgml.pack()
entry_density2 = tk.Entry(frame2); entry_density2.insert(0, "1.0"); entry_density2.pack()
tk.Button(frame2, text="CONVERT", command=mgml_to_percent, bg="#8E44AD", fg="white").pack(pady=5)
label_result2 = tk.Label(frame2, text="", bg="#D2B4DE"); label_result2.pack(pady=5)

root.mainloop()