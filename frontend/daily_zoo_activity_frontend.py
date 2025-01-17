import tkinter as tk
from tkinter import ttk
import backend.daily_zoo_activity_backend as dza


def clear_entity_tab_fields(tab):
    for widget in tab.winfo_children():
        widget.destroy()


def update_daily_zoo_activity_tab_content(ae):
    selected_tab = notebook.nametowidget(notebook.select())
    clear_entity_tab_fields(selected_tab)

    listbox = tk.Listbox(selected_tab)

    if ae == "Attractions":
        #dza.view_attractions_attendance_and_revenue()

        attractions_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='ATR_ID')
        attractions_id_label.pack()
        attractions_id = tk.StringVar()
        attractions_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attractions_id)
        attractions_id_entry.pack()

        attractions_name_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Name')
        attractions_name_label.pack()
        attractions_name = tk.StringVar()
        attractions_name_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attractions_name)
        attractions_name_entry.pack()

        attraction_show_label = ttk.Label(notebook.nametowidget(notebook.select()), text='R_ID')
        attraction_show_label.pack()
        attraction_show = tk.StringVar()
        attraction_show_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attraction_show)
        attraction_show_entry.pack()

        attendance_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Attendance')
        attendance_label.pack()
        attendance = tk.StringVar()
        attendance_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attendance)
        attendance_entry.pack()

        revenue_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Revenue')
        revenue_label.pack()
        revenue = tk.StringVar()
        revenue_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=revenue)
        revenue_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:dza.insert_attractions_attendance_and_revenue(attractions_id,attractions_name,attraction_show,attendance,revenue))
        button.pack()
    elif ae == "Concessions":
        #dza.view_concessions_daily_revenue()

        r_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='R_ID')
        r_id_label.pack()
        r_id = tk.StringVar()
        r_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=r_id)
        r_id_entry.pack()

        product_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Product')
        product_label.pack()
        product = tk.StringVar()
        product_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=product)
        product_entry.pack()

        daily_revenue_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Daily_Revenue')
        daily_revenue_label.pack()
        daily_revenue = tk.StringVar()
        daily_revenue_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=daily_revenue)
        daily_revenue_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:dza.insert_concessions_daily_revenue(r_id,product,daily_revenue))
        button.pack()
    elif ae == "Attendance":
        #dza.view_attendance_numbers_and_revenue()

        attendance_id_label = ttk.Label(notebook.nametowidget(notebook.select()), text='ATD_ID')
        attendance_id_label.pack()
        attendance_id = tk.StringVar()
        attendance_id_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attendance_id)
        attendance_id_entry.pack()

        attendance_type_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Type')
        attendance_type_label.pack()
        attendance_type = tk.StringVar()
        attendance_type_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=attendance_type)
        attendance_type_entry.pack()

        numbers_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Numbers')
        numbers_label.pack()
        numbers = tk.StringVar()
        numbers_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=numbers)
        numbers_entry.pack()

        revenue_label = ttk.Label(notebook.nametowidget(notebook.select()), text='Revenue')
        revenue_label.pack()
        revenue = tk.StringVar()
        revenue_entry = ttk.Entry(notebook.nametowidget(notebook.select()), textvariable=revenue)
        revenue_entry.pack()

        button = ttk.Button(selected_tab, text='Insert', command=lambda:dza.insert_attendance_numbers_and_revenue(attendance_id,attendance_type,numbers,revenue))
        button.pack()

    listbox.pack(side=tk.LEFT, fill='both', expand=True)

    sb = tk.Scrollbar(selected_tab)
    sb.pack(side=tk.RIGHT, fill='y')

    listbox.config(yscrollcommand=sb.set)


def switch_daily_zoo_activity_tab(event):
    selected_entity_tab = notebook.tab(notebook.select(), "text")
    update_daily_zoo_activity_tab_content(selected_entity_tab)


def daily_zoo_window_content(aw):
    aw.title('Daily Zoo Activity')

    global notebook
    notebook = ttk.Notebook(aw)
    notebook.pack(fill='both', expand=True)

    asset_entities = ["Attractions", "Concessions", "Attendance"]
    for ae in asset_entities:
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=ae)

    notebook.bind("<<NotebookTabChanged>>", switch_daily_zoo_activity_tab)

