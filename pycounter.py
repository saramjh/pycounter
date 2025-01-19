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

        label = ttk.Label(item_frame, text=item_name,
                          width=15)  # label width 수정
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
        update_item_order()


def toggle_topmost():
    root.attributes('-topmost', topmost_var.get())


def on_drag_start(event):
    widget = event.widget
    widget._drag_start_y = event.y
    widget._drag_start_index = items_frame.winfo_children().index(widget)


def on_drag_motion(event):
    widget = event.widget
    y = event.y - widget._drag_start_y
    if abs(y) > 5:  # 최소 이동 거리
        index = items_frame.winfo_children().index(widget)
        new_index = index + (1 if y > 0 else -1)
        if 0 <= new_index < len(items_frame.winfo_children()):
            items_frame.winfo_children()[index].pack_forget()
            items_frame.winfo_children()[index].pack(
                before=items_frame.winfo_children()[new_index], fill='x')
            widget._drag_start_y = event.y


def update_item_order():
    for i, child in enumerate(items_frame.winfo_children()):
        child.lift()


root = tk.Tk()
root.title("카운터 프로그램")

# 최상위 표시 체크박스
topmost_var = tk.BooleanVar()
topmost_check = ttk.Checkbutton(
    root, text="항상 위", variable=topmost_var, command=toggle_topmost)
topmost_check.pack(pady=(5, 5), padx=(10, 10), anchor='w')

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

root.bind("<B1-Motion>", on_drag_motion)
root.bind("<ButtonPress-1>", on_drag_start)

root.mainloop()
