import requests
import time
from flask import Flask, render_template, request, json
import pytz

app = Flask(__name__)

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
        timezone_dict = ip_data.get('time_zone')
        if timezone_dict:
            timezone = timezone_dict.get('name')
            if timezone:
                try:
                    timezone_obj = pytz.timezone(timezone)
                    timezone = timezone_obj.zone
                except pytz.UnknownTimeZoneError:
                    timezone = "Unknown Timezone"
            else:
                timezone = "N/A"
        else:
            timezone = "N/A"

        return f"""
        <p>IP Address Information:</p>
        <ul>
            <li>IP (v4): {ip_data.get('ip')}</li>
            <li>IP (v6): {ip_data.get('ipv6')}</li>
            <li>Country Code: {ip_data.get('country_code')}</li>
            <li>Country Name: {ip_data.get('country_name')}</li>
            <li>City: {ip_data.get('city')}</li>
            <li>Region: {ip_data.get('region')}</li>
            <li>Timezone: {timezone}</li>
            <li>Organization: {ip_data.get('organization')}</li>
            <li>ISP: {ip_data.get('isp')}</li>
            <li>ASN: {ip_data.get('asn')}</li>
        </ul>
        """
    else:
        return "<p>Failed to retrieve IP information.</p>"

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = "767d97f0f74e48408bce2b8588833d41"
    ip_address = None
    if request.method == 'POST':
        ip_address = request.form['ip']
        ip_data = get_ip_info(api_key, ip_address)
        return render_template('index.html', ip_data=display_ip_info(ip_data, None))
    return render_template('index.html', ip_data=display_ip_info(None, None))

if __name__ == '__main__':
    app.run(debug=True)