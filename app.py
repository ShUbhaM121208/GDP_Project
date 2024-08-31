from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')

def index():
   
    country_code = request.form['country']
    gdp_data = fetch_gdp(country_code)
    return render_template('index.html', gdp_data=gdp_data)
    

def fetch_gdp(country_code):
    try:
        response = requests.get(f'https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json')
        data = response.json()
        gdp_value = data[1][0]['value']
        return f'GDP: ${gdp_value:,.2f}'
    except Exception as e:
        return f'Error fetching GDP data: {str(e)}'

if __name__ == '_main_':
    app.run(debug=True)