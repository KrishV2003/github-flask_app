from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))
@app.route('/')
def home():
    result = ''
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict():
    data1 = float(request.form['sepal_length'])
    data2  = float(request.form['sepal_width'])
    data3 = float(request.form['petal_length'])
    data4 = float(request.form['petal_width'])
    result = model.predict([[data1, data2, data3, data4]])[0]
    return render_template('after.html',data = result)
if __name__ == '__main__':
    app.run(debug=True)