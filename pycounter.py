import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


def add_item():
    item_name = item_entry.get()
    if item_name:
        item_frame = ttk.Frame(items_frame, padding=5)
        item_frame.pack(fill='x')

        def delete_item():
            if messagebox.askokcancel("삭제 확인", f"{item_name} 항목을 삭제하시겠습니까?"):
                item_frame.destroy()
                update_item_order()

        trash_icon = "🗑️"
        delete_button = ttk.Button(
            item_frame, text=f"{trash_icon} {item_name}", command=delete_item)
        delete_button.pack(side='left', padx=1, ipadx=5)

        count = 0
        count_label = ttk.Label(item_frame, text=str(
            count), width=5, font=('Helvetica', 12), foreground='darkgray', anchor='e')
        count_label.pack(side='right', padx=5)
        item_frame.count = count  # Store count in item_frame

        def update_count_label():
            if item_frame.count == 0:
                count_label.config(font=('Helvetica', 12),
                                   foreground='darkgray')
            elif item_frame.count < 0:
                count_label.config(
                    font=('Helvetica', 12, 'bold'), foreground='blue')
            else:
                count_label.config(
                    font=('Helvetica', 12, 'bold'), foreground='red')

        def increment():
            item_frame.count += 1
            count_label.config(text=str(item_frame.count))
            update_count_label()

        def decrement():
            item_frame.count -= 1
            count_label.config(text=str(item_frame.count))
            update_count_label()

        minus_button = ttk.Button(
            item_frame, text="-", width=0.1, command=decrement)
        minus_button.pack(side='right', padx=1)
        plus_button = ttk.Button(item_frame, text="+",
                                 width=0.1, command=increment)
        plus_button.pack(side='right', padx=1)

        count_label.pack(side='right', padx=5)  # Reposition count label

        item_entry.delete(0, tk.END)
        update_item_order()


def toggle_topmost():
    root.attributes('-topmost', topmost_var.get())


def update_item_order():
    for i, child in enumerate(items_frame.winfo_children()):
        child.lift()


def reset_all_counts():
    for child in items_frame.winfo_children():
        for widget in child.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("width") == 5:
                widget.config(text="0", font=('Helvetica', 12),
                              foreground='darkgray')
                widget.master.count = 0  # Reset the count variable


def reset_all_items():
    for child in items_frame.winfo_children():
        child.destroy()


def on_enter_key(event):
    add_item()


root = tk.Tk()
root.title("평가 카운터")

topmost_var = tk.BooleanVar(value=True)
root.attributes('-topmost', True)

# 최상위 표시 체크박스 및 카운트 초기화 버튼
top_frame = ttk.Frame(root, padding=1)
top_frame.pack(fill='x')

reset_button = ttk.Button(top_frame, text="카운트 초기화", command=reset_all_counts)
reset_button.pack(side='left', padx=(10, 3))

clear_items_button = ttk.Button(
    top_frame, text="항목 초기화", command=reset_all_items)
clear_items_button.pack(side='left', padx=(3, 10))

topmost_check = ttk.Checkbutton(
    top_frame, text="항상 위", variable=topmost_var, command=toggle_topmost)
topmost_check.pack(side='right', padx=(10, 10))

# 항목 추가 입력 부분
add_frame = ttk.Frame(root, padding=10)
add_frame.pack(padx=5)

item_label = ttk.Label(add_frame, text="항목 명:")
item_label.pack(side='left')

item_entry = ttk.Entry(add_frame, width=20)
item_entry.pack(side='left')
item_entry.bind('<Return>', on_enter_key)

add_button = ttk.Button(add_frame, text="+", command=add_item)
add_button.pack(side='left', padx=(1))

# 항목 표시 부분
items_frame = ttk.Frame(root, padding=10)
items_frame.pack(fill='both', expand=True)

root.mainloop()
