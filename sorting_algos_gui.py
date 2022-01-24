from tkinter import *
from tkinter import ttk
import algorithms
from random import sample as samp
import time


# ========== Window ==============
wind = Tk()
wind.title("Sorting Algorithms")
wind.maxsize(1000, 750)
wind.config(bg="gainsboro")

# ========= Variables ==============
selected_algo = StringVar()
algos = [
    "Bubble Sort",
    "Insertion Sort",
    "Binary Insertion Sort",
    "Quick Sort",
    "Merge Sort",
    "Heap Sort",
    "Radix Sort",
    "Shell Sort",
]
arr = []

# ========= Functions ==============
def generate():
    # print(f'Selected Algorthm: {selected_algo.get()}')
    global arr
    try:
        size = int(size_input.get()) if int(size_input.get()) <= 400 else 400
    except:
        size = 20

    arr = samp(range(1, size + 1), size)
    drawList(arr, ["sky blue" for _ in range(int(len(arr)))])


def drawList(arr, colors):
    canv.delete("all")

    height = 530
    width = 1000
    b_width = width / (len(arr) + 0.5)
    pad = 5
    space = 1
    n_arr = [i / max(arr) for i in arr]

    for i, h in enumerate(n_arr):
        x0 = i * b_width + pad + space
        y0 = height - h * 515

        x1 = (i + 1) * b_width + space
        y1 = height

        canv.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        # canv.create_text((x0+x1)//2 -2, y0, anchor = SW, text = str(arr[i]))

    wind.update()


def start():
    global arr
    s = speed.get()
    print(selected_algo.get())
    if selected_algo.get() == algos[0]:
        algorithms.bubble(arr, drawList, s)

    if selected_algo.get() == algos[1]:
        algorithms.insertion(arr, drawList, s)

    if selected_algo.get() == algos[2]:
        algorithms.binary_insertion(arr, drawList, s)

    if selected_algo.get() == algos[3]:
        algorithms.quick(arr, drawList, s)

    if selected_algo.get() == algos[4]:
        algorithms.merge_sort(arr, 0, len(arr) - 1, drawList, s)

    if selected_algo.get() == algos[5]:
        algorithms.heap(arr, drawList, s)

    if selected_algo.get() == algos[6]:
        algorithms.radix(arr, drawList, s)

    if selected_algo.get() == algos[7]:
        algorithms.shell(arr, drawList, s)


# ====================== User Interface =========================
frame = Frame(wind, width=1000, height=200, bg="grey")
frame.grid(row=0, column=0, pady=5)

algo_label = Label(frame, text="Algorithm: ", bg="grey")
algo_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

algo_menu = ttk.Combobox(frame, textvariable=selected_algo, values=algos)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

size_label = Label(frame, text="Size: ", bg="grey")
size_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

size_input = Entry(frame)
size_input.grid(row=1, column=1, padx=5, pady=5, sticky=W)

speed = Scale(
    frame,
    from_=0.01,
    to=0.5,
    length=200,
    digits=2,
    resolution=0.001,
    orient=HORIZONTAL,
    label="Speed (s): ",
)
speed.grid(row=0, column=3, padx=5, pady=5)
speed.set(0.06)

# buttons
gen_list_button = Button(frame, text="Generate List", command=generate, bg="blue")
gen_list_button.grid(row=1, column=2, padx=5, pady=5)

start_button = Button(frame, text="Start Sort", command=start, bg="orange")
start_button.grid(row=0, column=2, padx=5, pady=5)


# =================================================================
canv = Canvas(wind, width=1000, height=530, bg="snow")
canv.grid(row=1, column=0, pady=5)

wind.mainloop()
