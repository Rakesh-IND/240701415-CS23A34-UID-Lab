import tkinter as tk
from tkinter import messagebox
from common import save_response

TASK_PROMPT = "Please describe one short task or goal you're working on:"


def run_gui():
    root = tk.Tk()
    root.title("Interface Comparison — GUI")
    root.geometry("400x260")

    tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=(10,0))
    name_var = tk.StringVar()
    tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)

    tk.Label(root, text=TASK_PROMPT).pack(anchor="w", padx=10, pady=(10,0))
    desc_text = tk.Text(root, height=5)
    desc_text.pack(fill="both", padx=10)

    tk.Label(root, text="Satisfaction (1-5):").pack(anchor="w", padx=10, pady=(10,0))
    rating_var = tk.IntVar(value=4)
    rating_scale = tk.Scale(root, from_=1, to=5, orient="horizontal", variable=rating_var)
    rating_scale.pack(fill="x", padx=10)

    def submit():
        name = name_var.get().strip() or "(anonymous)"
        desc = desc_text.get("1.0", "end").strip()
        rating = rating_var.get()
        save_response("GUI", name, desc, rating)
        messagebox.showinfo("Saved", "Thanks — response saved.")
        root.destroy()

    tk.Button(root, text="Submit", command=submit).pack(pady=10)
    root.mainloop()


if __name__ == '__main__':
    run_gui()
