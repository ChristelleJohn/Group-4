import pytest
import tkinter as tk
from ip_info_app import IPInfoApp
from ip_info_app import get_ip_info, is_valid_ip

@pytest.fixture
def app():
    root = tk.Tk()
    yield IPInfoApp(master=root)

def test_fetch_ip_info(app):
    # Test fetching IP information with valid IP address
    ip_address = "8.8.8.8"
    ip_data = get_ip_info(ip_address)
    assert isinstance(ip_data, dict)

def test_invalid_ip_address():
    # Test validating an invalid IP address
    invalid_ip = "invalid_ip"
    assert not is_valid_ip(invalid_ip)

def test_valid_ip_address():
    # Test validating a valid IP address
    valid_ip = "192.168.0.1"
    assert is_valid_ip(valid_ip)
