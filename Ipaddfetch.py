import requests
import time
from tkinter import Tk, Label, Entry, Button, Text, font, BooleanVar, Checkbutton, Frame
from tkinter import ttk

def get_ip_info(api_key, ip_address=None, fields=None):
    """Fetches IP address information using the specified API and returns a dictionary."""
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
    if ip_address:
        url += f"&ip={ip_address}"
    if fields:
        url += f"&fields={','.join(fields)}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network Error: {e}"}

def display_ip_info(ip_data, text_widget):
    """Displays the provided IP information in a formatted way within the text widget."""
    text_widget.delete("1.0", "end")
    if "error" in ip_data:
        text_widget.insert("end", f"Error: {ip_data['error']}")
    else:
        text_widget.insert("end", "IP Address Information:\n")
        for key, value in ip_data.items():
            text_widget.insert("end", f"  {key}: {value}\n")

def fetch_ip_info(api_key, ip_entry, text_widget, fields):
    """Fetches IP information based on user input or retrieves user's own IP."""
    ip_address = ip_entry.get().strip()
    if ip_address:
        # Validate IP address format
        if not is_valid_ip(ip_address):
            text_widget.delete("1.0", "end")
            text_widget.insert("end", "Invalid IP address format.")
            return
    else:
        ip_address = None

    ip_data = get_ip_info(api_key, ip_address, fields)
    display_ip_info(ip_data, text_widget)

def clear_text_widget(text_widget):
    """Clears the text widget."""
    text_widget.delete("1.0", "end")

def is_valid_ip(ip):
    """Validates the format of an IP address."""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def main():
    api_key = "767d97f0f74e48408bce2b8588833d41"

    window = Tk()
    window.title("IP Address Information")
    window.geometry("650x600")
    window.configure(bg="#f0f0f0")  # Set background color

    # Increase font size for title
    title_font = font.Font(family="Arial", size=16, weight="bold")
    title_label = Label(window, text="IP Address Information", font=title_font, bg="#f0f0f0")
    title_label.pack(pady=10)  # Add padding

    ip_label = Label(window, text="Enter IP Address (optional):", bg="#f0f0f0")
    ip_label.pack()

    # Create custom style for the entry widget to have rounded corners
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Rounded.TEntry', borderwidth=1, relief="solid", padding=5, foreground="black", font=('Arial', 10))
    ip_entry = ttk.Entry(window, style='Rounded.TEntry')
    ip_entry.pack()

    fields_label = Label(window, text="Select fields to display (optional):", bg="#f0f0f0")
    fields_label.pack()

    fields = ['country_code3', 'country_name', 'city', 'state_prov', 'time_zone', 'latitude', 'longitude', 'organization', 'isp', 'asn']
    selected_fields = []
    
    frame = Frame(window, bg="#f0f0f0")
    frame.pack()

    for i, field in enumerate(fields):
        var = BooleanVar()
        var.set(False)
        checkbox = Checkbutton(frame, text=field, variable=var, bg="#f0f0f0")
        checkbox.grid(row=i // 2, column=i % 2, sticky='w')
        selected_fields.append((field, var))

    fetch_button = Button(frame, text="Fetch Info", command=lambda: fetch_ip_info(api_key, ip_entry, text_widget, [field for field, var in selected_fields if var.get()]), bg="#007bff", fg="white")
    fetch_button.grid(row=len(fields) // 2, column=0, sticky='ew', pady=10)

    clear_button = Button(frame, text="Clear", command=lambda: clear_text_widget(text_widget), bg="#dc3545", fg="white")
    clear_button.grid(row=len(fields) // 2, column=1, sticky='ew', pady=10)

    text_widget = Text(window, width=70, height=17)
    text_widget.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
