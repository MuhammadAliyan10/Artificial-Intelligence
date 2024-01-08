from flask import Flask, render_template, request
from datetime import datetime


def storeCustomerInformation(name,price,order):
    now = datetime.now()
    dateTime= now.strftime("%D %T %A")
    date = now.strftime("%D")
    time = now.strftime("%T")
    day = now.strftime("%A")
    global id;
    with open('Information.txt', 'a') as f:
        f.write(f"Full Name: {name}\nTotal Price: {price}$ \nOrder : {order} \nDate: {dateTime}\n----------\n")
        f.close()
    with open('Information.csv', 'a') as f:
        f.write(f"{name},{price},{order},{date},{day},{time}\n")
        f.close()
        
def read_customer_information(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    customer_info_list = []
    for i in range(0, len(lines), 5):
        entry = lines[i:i+5]
        customer_info = {}
        for line in entry:
            parts = line.split(': ', 1)
            if len(parts) == 2:
                key, value = parts
                customer_info[key.strip()] = value.strip()
        customer_info_list.append(customer_info)

    return customer_info_list   
        
        
        


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data_render():
    file_path = 'Information.txt'
    fn =[]
    od= []
    pr=[]
    da=[]
    message = "Data"
    customer_data_list = read_customer_information(file_path)
    for customer_data in customer_data_list:
        fullName = customer_data.get('Full Name', 'N/A')
        totalPrice = customer_data.get('Total Price', 'N/A')
        orderValue = customer_data.get('Order', 'N/A')
        dateValue = customer_data.get('Date', 'N/A')
        fn.append(fullName)
        od.append(orderValue)
        pr.append(totalPrice)
        da.append(dateValue)
    length = len(fn)
    if length ==1:
        return "<h2 style=\"display: flex; justify-content: center; align-items: center;\">No Data Found</h2>"
    else:
        return render_template('data.html',name = fn, price= pr,order = od,date=da,leng = length,message=message)

@app.route('/get_data',methods=['POST'])
def get_data():
    name = request.form['name_input']
    order = request.form['order_input']
    price = request.form['price_input']
    storeCustomerInformation(name,price,order)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
