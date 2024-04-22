import requests
from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = "767d97f0f74e48408bce2b8588833d41"  
    if 'search_history' not in session:
        session['search_history'] = []
    
    ip_data = {}
    if request.method == 'POST':
        ip_address = request.form['ip']
        ip_data = get_ip_info(api_key, ip_address)
        session['search_history'].insert(0, {
            'ip': ip_data.get('ip', 'N/A'),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'city': ip_data.get('city', 'N/A'),
            'country_name': ip_data.get('country_name', 'N/A'),
            'time_zone': ip_data.get('time_zone', {}).get('name', 'N/A'),
            'isp': ip_data.get('isp', 'N/A')
        })
        session.modified = True

    return render_template('index.html', ip_data=ip_data, search_history=session['search_history'])

def get_ip_info(api_key, ip_address=None):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}"
    if ip_address:
        url += f"&ip={ip_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return {}

if __name__ == '__main__':
    app.run(debug=True)
