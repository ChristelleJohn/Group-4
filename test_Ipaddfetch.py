import pytest
import tkinter as tk
from ip_info_app import IPInfoApp

@pytest.fixture
def app():
    root = tk.Tk()
    yield IPInfoApp(master=root)

def test_fetch_ip_info(app):
    # Test fetching IP information with valid IP address
    app.ip_entry.insert(0, "8.8.8.8")  # Insert a valid IP address
    app.fetch_ip_info()
    assert app.text_widget.get("1.0", "end") != "Invalid IP address format."

def test_invalid_ip_address(app):
    # Test fetching IP information with invalid IP address
    app.ip_entry.insert(0, "invalid_ip")  # Insert an invalid IP address
    app.fetch_ip_info()
    assert app.text_widget.get("1.0", "end") == "Invalid IP address format."

# Add more test cases as needed

if __name__ == "__main__":app.run()
    pytest.main()
