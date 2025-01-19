import tkinter as tk
from tkinter import ttk


def add_item():
    item_name = item_entry.get()
    if item_name:
        item_frame = ttk.Frame(items_frame, padding=5)
        item_frame.pack(fill='x')

        label = ttk.Label(item_frame, text=item_name, width=20)
        label.pack(side='left')

        count = 0
        count_label = ttk.Label(item_frame, text=str(count), width=5)
        count_label.pack(side='left')

        def increment():
            nonlocal count
            count += 1
            count_label.config(text=str(count))

        def decrement():
            nonlocal count
            count -= 1
            count_label.config(text=str(count))

        plus_button = ttk.Button(item_frame, text="+",
                                 width=3, command=increment)
        plus_button.pack(side='left')

        minus_button = ttk.Button(
            item_frame, text="-", width=3, command=decrement)
        minus_button.pack(side='left')

        item_entry.delete(0, tk.END)


def toggle_topmost():
    root.attributes('-topmost', topmost_var.get())


root = tk.Tk()
root.title("카운터 프로그램")

# 최상위 표시 체크박스
topmost_var = tk.BooleanVar()
topmost_check = ttk.Checkbutton(
    root, text="항상 위", variable=topmost_var, command=toggle_topmost)
topmost_check.pack(pady=(5, 5), padx=(0, 10), anchor='e')  # 왼쪽 정렬 및 좌우 패딩 추가

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
