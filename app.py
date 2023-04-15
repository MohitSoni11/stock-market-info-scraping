from flask import Flask, render_template, request
import requests, json, finnhub

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

finnhub_key = 'cfq45l1r01qmi6j4em8gcfq45l1r01qmi6j4em90'
finnhub_client = finnhub.Client(api_key=finnhub_key)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/get-sec-filing', methods=['GET', 'POST'])
def get_sec_filing():
  if (request.method == 'POST'):
    company_ticker = request.form['ticker']
    start_date = request.form['start-date']
    end_date = request.form['end-date']
    filings_data = finnhub_client.filings(symbol=company_ticker, _from=start_date, to=end_date)
        
    return render_template('show-sec-filings.html', 
                           filings_data=filings_data,
                           ticker=company_ticker,
                           start_date=start_date,
                           end_date=end_date)
  else:
    return render_template('get-sec-filing.html')