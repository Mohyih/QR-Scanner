import customtkinter as ctk
import json
import os
from datetime import datetime

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

data = []

USERNAME = "admin"
PASSWORD = "admin"

app = ctk.CTk()
app.title("QR Scanner Viewer")
app.geometry("640x480")

def load_data(filter_text="", selected_sort=""):
    global data
    for widget in left_frame.winfo_children():
        widget.destroy()

    try:
        if not os.path.exists("scanned_data.json"):
            return

        with open("scanned_data.json", "r") as f:
            data = json.load(f)

        if selected_sort == "Newest to Oldest":
            data.sort(key=lambda x: datetime.strptime(x["scanDate"], "%Y-%m-%d"), reverse=True)
        elif selected_sort == "Oldest to Newest":
            data.sort(key=lambda x: datetime.strptime(x["scanDate"], "%Y-%m-%d"))

        for entry in data:
            name = entry.get("content", "")
            timestamp = entry.get("scanDate", "")

            if filter_text.lower() in name.lower():
                display_text = f"{name} | {timestamp}"
                btn = ctk.CTkButton(left_frame, text=display_text, anchor="w", command=lambda e=entry: show_details(e))
                btn.pack(fill="x", padx=10, pady=2)
    except Exception as e:
        print(f"Error loading data: {e}")

def show_details(entry):
    detail_textbox.configure(state="normal")
    detail_textbox.delete("1.0", ctk.END)
    detail_textbox.insert(ctk.END, json.dumps(entry, indent=4))
    detail_textbox.configure(state="disabled")

def search_data():
    filter_text = search_entry.get()
    selected_sort = sort_dropdown.get()
    load_data(filter_text, selected_sort)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:

        login_frame.pack_forget()
        show_main_window()
    else:
        error_label.configure(text="Invalid username or password.", text_color="red")


def show_main_window():

    search_frame = ctk.CTkFrame(app)
    search_frame.pack(side="top", fill="x", padx=10, pady=10)

    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    global left_frame
    left_frame = ctk.CTkFrame(main_frame, width=200)
    left_frame.pack(side="left", fill="y", padx=10)

    right_frame = ctk.CTkFrame(main_frame)
    right_frame.pack(side="left", fill="y", expand=True, padx=10)

    global search_entry, sort_dropdown, detail_textbox
    search_entry = ctk.CTkEntry(search_frame, width=300, placeholder_text="Search by name...")
    search_entry.pack(side="right", padx=10)

    search_button = ctk.CTkButton(search_frame, text="Search", command=search_data)
    search_button.pack(side="right", padx=10)

    sort_options = ["Newest to Oldest", "Oldest to Newest"]
    sort_dropdown = ctk.CTkOptionMenu(search_frame, values=sort_options)
    sort_dropdown.pack(side="right", padx=10)

    detail_textbox = ctk.CTkTextbox(right_frame, width=300, height=150)
    detail_textbox.pack(pady=10)
    detail_textbox.configure(state="disabled")

    load_data()  

login_frame = ctk.CTkFrame(app)
login_frame.pack(fill="both", expand=True, padx=10, pady=10)

username_label = ctk.CTkLabel(login_frame, text="Username:")
username_label.pack(pady=10)

username_entry = ctk.CTkEntry(login_frame)
username_entry.pack(pady=5)

password_label = ctk.CTkLabel(login_frame, text="Password:")
password_label.pack(pady=10)

password_entry = ctk.CTkEntry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = ctk.CTkButton(login_frame, text="Login", command=validate_login)
login_button.pack(pady=10)

error_label = ctk.CTkLabel(login_frame, text="", text_color="red")
error_label.pack(pady=5)

app.mainloop()
