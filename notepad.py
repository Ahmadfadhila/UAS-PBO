import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            text = text_area.get("1.0", tk.END)
            file.write(text)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", text)

def undo():
    try:
        text_area.edit_undo()
    except tk.TclError:
        messagebox.showinfo("Undo", "Nothing more to undo")

def redo():
    try:
        text_area.edit_redo()
    except tk.TclError:
        messagebox.showinfo("Redo", "Nothing more to redo")

def find_text():
    find_popup = tk.Toplevel(root)
    find_popup.title("Find")
    
    find_entry = tk.Entry(find_popup)
    find_entry.pack()
    
    def find():
        search_text = find_entry.get()
        start_pos = "1.0"
        while True:
            start_pos = text_area.search(search_text, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_text)}c"
            text_area.tag_add("found", start_pos, end_pos)
            start_pos = end_pos
        text_area.tag_config("found", background="red")
    
    find_button = tk.Button(find_popup, text="Find", command=find)
    find_button.pack()

def insert_date():
    now = tk.StringVar()
    now.set(tk.Tk().strftime("%Y-%m-%d %H:%M:%S"))
    text_area.insert(tk.END, now.get())

root = tk.Tk()
root.title("Notepad Kelompok 2")

text_area = scrolledtext.ScrolledText(root, wrap="word")
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Date", command=insert_date)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()
