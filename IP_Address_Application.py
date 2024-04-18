import requests
import time
from tkinter import Tk, Label, Entry, Button, Text, font, BooleanVar, Checkbutton, Frame

def get_ip_info(api_key, ip_address=None, fields=None):
    """Fetches IP address information using the specified API and returns a dictionary."""
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
    if ip_address:
        url += f"&ip={ip_address}"
    if fields:
        url += f"&fields={','.join(fields)}"
    try:
        print("API URL:", url)
        response = requests.get(url)
        print("API Response:", response.text)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None

def display_ip_info(ip_data, text_widget):
    """Displays the provided IP information in a formatted way within the text widget."""
    if ip_data:
        text_widget.delete("1.0", "end")
        text_widget.insert("end", "IP Address Information:\n")
        for key, value in ip_data.items():
            text_widget.insert("end", f"  {key}: {value}\n")
    else:
        text_widget.delete("1.0", "end")
        text_widget.insert("end", "Failed to retrieve IP information.")

def fetch_ip_info(api_key, ip_entry, text_widget, fields):
    """Fetches IP information based on user input or retrieves user's own IP."""
    ip_address = ip_entry.get()
    print("Fetching information for IP:", ip_address)
    print("Selected Fields:", fields)
    time.sleep(1)

    ip_data = get_ip_info(api_key, ip_address, fields)
    display_ip_info(ip_data, text_widget)

def main():
    api_key = "767d97f0f74e48408bce2b8588833d41"

    window = Tk()
    window.title("IP Address Information")
    window.geometry("650x600")

    # Increase font size for title
    title_font = font.Font(family="Arial", size=16, weight="bold")
    title_label = Label(window, text="IP Address Information", font=title_font)
    title_label.pack(pady=10)  # Add padding

    ip_label = Label(window, text="Enter IP Address (optional):")
    ip_label.pack()

    ip_entry = Entry(window)
    ip_entry.pack()

    fields_label = Label(window, text="Select fields to display (optional):")
    fields_label.pack()

    fields = ['country_code3', 'country_name', 'city', 'state_prov', 'time_zone', 'latitude', 'longitude', 'organization', 'isp', 'asn']
    selected_fields = []
    
    frame = Frame(window)
    frame.pack()
    for i, field in enumerate(fields):
        var = BooleanVar()
        var.set(False)
        checkbox = Checkbutton(frame, text=field, variable=var)
        checkbox.grid(row=i // 2, column=i % 2, sticky='w')
        selected_fields.append((field, var))

    fetch_button = Button(window, text="Fetch Info", command=lambda: fetch_ip_info(api_key, ip_entry, text_widget, [field for field, var in selected_fields if var.get()]))
    fetch_button.pack()

    text_widget = Text(window, width=70, height=17)
    text_widget.pack()

    window.mainloop()

if __name__ == '__main__':
  main()