import pytest
import tkinter as tk
from ip_info_app import IPInfoApp
from ip_info_app_controller import IPInfoAppController

@pytest.fixture
def app():
    root = tk.Tk()
    yield IPInfoApp(master=root)

@pytest.fixture
def controller(app):
    return IPInfoAppController(app)

def test_fetch_ip_info(app, controller):
    # Test fetching IP information with valid IP address
    ip_address = "8.8.8.8"
    selected_fields = ['country_code3', 'country_name', 'city']  # Example selected fields
    ip_data = controller.fetch_ip_info(ip_address, selected_fields)
    app.display_ip_info(ip_data)
    assert app.text_widget.get("1.0", "end") != "Invalid IP address format."

def test_invalid_ip_address(app, controller):
    # Test fetching IP information with invalid IP address
    ip_address = "invalid_ip"
    selected_fields = ['country_code3', 'country_name', 'city']  # Example selected fields
    ip_data = controller.fetch_ip_info(ip_address, selected_fields)
    app.display_ip_info(ip_data)
    assert app.text_widget.get("1.0", "end") == "Invalid IP address format."
