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

        delete_button = ttk.Button(
            item_frame, text="X", width=3, command=delete_item)
        delete_button.pack(side='left')

        label = ttk.Label(item_frame, text=item_name, anchor='w')
        label.pack(side='left', fill='x', expand=True)

        count = 0
        count_label = ttk.Label(
            item_frame, text=str(count), width=5, anchor='e')
        count_label.pack(side='right')

        def increment():
            nonlocal count
            count += 1
            count_label.config(text=str(count))

        def decrement():
            nonlocal count
            count -= 1
            count_label.config(text=str(count))
        minus_button = ttk.Button(
            item_frame, text="-", width=2, command=decrement)
        minus_button.pack(side='right')
        plus_button = ttk.Button(item_frame, text="+",
                                 width=2, command=increment)
        plus_button.pack(side='right')

        item_entry.delete(0, tk.END)
        update_item_order()


def toggle_topmost():
    root.attributes('-topmost', topmost_var.get())


def update_item_order():
    for i, child in enumerate(items_frame.winfo_children()):
        child.lift()


def reset_counters():
    for item_frame in items_frame.winfo_children():
        count_label = item_frame.winfo_children()[2]
        count_label.config(text="0")


root = tk.Tk()
root.title("카운터 프로그램")

# 최상위 표시 체크박스 및 초기화 버튼 프레임
top_frame = ttk.Frame(root, padding=5)
top_frame.pack(fill='x')

reset_button = ttk.Button(top_frame, text="카운터 숫자 초기화", command=reset_counters)
reset_button.pack(side='left')

topmost_var = tk.BooleanVar()
topmost_check = ttk.Checkbutton(
    top_frame, text="항상 위", variable=topmost_var, command=toggle_topmost)
topmost_check.pack(side='right')

# 항목 추가 입력 부분
add_frame = ttk.Frame(root, padding=10)
add_frame.pack()

item_label = ttk.Label(add_frame, text="항목 이름:")
item_label.pack(side='left')

item_entry = ttk.Entry(add_frame, width=20)
item_entry.pack(side='left')

add_button = ttk.Button(add_frame, text="추가", command=add_item)
add_button.pack(side='left')

# 항목 표시 부분
items_frame = ttk.Frame(root, padding=10)
items_frame.pack(fill='both', expand=True)

root.mainloop()
