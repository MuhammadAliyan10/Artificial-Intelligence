from flask import Flask,request,jsonify
import requests

app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    sourse_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name'] 
    finalResult = converter(sourse_currency, amount, target_currency )       
    responce = {
        'fulfillmentText' : f"{amount} {sourse_currency} is {finalResult} {target_currency} "
    }
    return jsonify(responce) 


def converter(sourse_currency,amount,target_currency):
    url = f'https://api.fastforex.io/convert?from={sourse_currency}&to={target_currency}&amount={amount}&api_key=60561289fd-ceb0e5e3e6-s4q6ix'
    responce = requests.get(url)
    data = responce.json()
    return data['result'][target_currency]
if __name__ == '__main__':
    app.run(debug=True)