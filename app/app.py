from flask import Flask, request, jsonify
from src.predict import predict_fraud

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    type_mapping = {'TRANSFER': 0, 'CASH_OUT': 1, 'PAYMENT': 2, 'DEBIT': 3, 'CASH_IN': 4}
    data['type'] = type_mapping.get(data['type'].upper(), 0)
    result = predict_fraud(data)
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
