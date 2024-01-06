from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

df = pd.read_csv('./Data/TotalData.csv')

x_train,x_test,y_train,y_test =train_test_split(df.Message,df.Category,test_size=0.2)


v = CountVectorizer()
x_train_count = v.fit_transform(x_train.values)

model = MultinomialNB()
model.fit(x_train_count,y_train)
x_test_counts = v.transform(x_test)
model.score(x_test_counts,y_test)

def email_checker(email):
    ec = v.transform(email)
    result = model.predict(ec)
    result = result[0]
    if result == 'ham':
        return "Email"
    elif result == 'spam':
        return "Spam"



    
     

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    final_result = email_checker([user_input])
    result = final_result
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
