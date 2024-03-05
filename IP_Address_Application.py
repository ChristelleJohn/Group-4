import requests
import time
from tkinter import Tk, Label, Entry, Button, Text, font

def get_ip_info(api_key, ip_address=None):
  """Fetches IP address information using the specified API and returns a dictionary."""
  url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
  if ip_address:
    url += f"&ip={ip_address}"
  try:
    response = requests.get(url)
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
    text_widget.insert("end", f"  IP (v4): {ip_data.get('ip')}\n")
    text_widget.insert("end", f"  IP (v6): {ip_data.get('ipv6')}\n")
    text_widget.insert("end", f"  Country Code: {ip_data.get('country_code')}\n")
    text_widget.insert("end", f"  Country Name: {ip_data.get('country_name')}\n")
    text_widget.insert("end", f"  City: {ip_data.get('city')}\n")
    text_widget.insert("end", f"  Region: {ip_data.get('region')}\n")
    text_widget.insert("end", f"  Timezone: {ip_data.get('time_zone')}\n")
    text_widget.insert("end", f"  Organization: {ip_data.get('organization')}\n")
    text_widget.insert("end", f"  ISP: {ip_data.get('isp')}\n")
    text_widget.insert("end", f"  ASN: {ip_data.get('asn')}\n")
  else:
    text_widget.delete("1.0", "end")  
    text_widget.insert("end", "Failed to retrieve IP information.")

def fetch_ip_info(api_key, ip_entry, text_widget):
  """Fetches IP information based on user input or retrieves user's own IP."""
  ip_address = ip_entry.get()
  print("Fetching information...")
  time.sleep(1) 

  ip_data = get_ip_info(api_key, ip_address)
  display_ip_info(ip_data, text_widget)

def main():
  api_key = "767d97f0f74e48408bce2b8588833d41"

  window = Tk()
  window.title("IP Address Information")
  window.geometry("500x300")  # Set window size

  # Increase font size for title
  title_font = font.Font(family="Arial", size=16, weight="bold")
  title_label = Label(window, text="IP Address Information", font=title_font)
  title_label.pack(pady=10)  # Add padding

  
  ip_label = Label(window, text="Enter IP Address (optional):")
  ip_label.pack()

  ip_entry = Entry(window)
  ip_entry.pack()
 
  fetch_button = Button(window, text="Fetch Info", command=lambda: fetch_ip_info(api_key, ip_entry, text_widget))
  fetch_button.pack()

  text_widget = Text(window, width=50, height=15)
  text_widget.pack()

  window.mainloop()

if __name__ == "__main__":
  main()
