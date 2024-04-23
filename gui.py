import tkinter as tk
from tkinter import ttk
from tkinter import Label, Button, Text, font, BooleanVar, Checkbutton, Frame, Entry

class IPInfoApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("IP Address Information")
        self.pack(fill="both", expand=True)

        title_font = font.Font(family="Arial", size=16, weight="bold")
        title_label = Label(self, text="IP Address Information", font=title_font, bg="#f0f0f0")
        title_label.pack(pady=10)

        self.ip_label = Label(self, text="Enter IP Address (optional):", bg="#f0f0f0")
        self.ip_label.pack()

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Rounded.TEntry', borderwidth=1, relief="solid", padding=5, foreground="black", font=('Arial', 10))
        self.ip_entry = ttk.Entry(self, style='Rounded.TEntry')
        self.ip_entry.pack()

        self.fields_label = Label(self, text="Select fields to display (optional):", bg="#f0f0f0")
        self.fields_label.pack()

        self.fields = ['country_code3', 'country_name', 'city', 'state_prov', 'time_zone', 'latitude', 'longitude', 'organization', 'isp', 'asn']
        self.selected_fields = []

        self.frame = Frame(self, bg="#f0f0f0")
        self.frame.pack()

        for i, field in enumerate(self.fields):
            var = BooleanVar()
            var.set(False)
            checkbox = Checkbutton(self.frame, text=field, variable=var, bg="#f0f0f0")
            checkbox.grid(row=i // 2, column=i % 2, sticky='w')
            self.selected_fields.append((field, var))

        self.fetch_button = Button(self.frame, text="Fetch Info", command=self.fetch_ip_info, bg="#007bff", fg="white")
        self.fetch_button.grid(row=len(self.fields) // 2, column=0, sticky='ew', pady=10)

        self.clear_button = Button(self.frame, text="Clear", command=self.clear_text_widget, bg="#dc3545", fg="white")
        self.clear_button.grid(row=len(self.fields) // 2, column=1, sticky='ew', pady=10)

        self.text_widget = Text(self, width=70, height=17)
        self.text_widget.pack()

        self.test_button = Button(self.frame, text="Test", command=self.test_ip_info_fetching)
        self.test_button.grid(row=len(self.fields) // 2 + 1, column=0, columnspan=2, sticky='ew', pady=10)

    def fetch_ip_info(self):
        pass

    def clear_text_widget(self):
        pass

    def test_ip_info_fetching(self):
        pass
