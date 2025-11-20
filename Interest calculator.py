import tkinter as tk

def calculate():
  
        p = float(principal.get())
        r = float(rate.get())
        t = float(time.get())
        si = (p * r * t) / 100
        amount = p * (1 + r/100) ** t
        ci = amount - p

        result.configure(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x400")
root.configure(bg="#FFECA1")
tk.Label(root, text="Principal:",bg="#EFC3CA").pack()
principal = tk.Entry(root)
principal.pack()

tk.Label(root, text="Rate (%):",bg="#EFC3CA").pack()
rate = tk.Entry(root)
rate.pack()

tk.Label(root, text="Time (years):",bg="#EFC3CA").pack()
time = tk.Entry(root)
time.pack()

tk.Button(root, text="Calculate", command=calculate,bg="#EFC3CA").pack(pady=15)

result = tk.Label(root, text="Simple Interest:\nCompound Interest:",bg="#E7DDFF")
result.pack()

root.mainloop()