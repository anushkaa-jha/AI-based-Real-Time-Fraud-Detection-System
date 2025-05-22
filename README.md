# AI-based Real-Time Fraud Detection System

This project implements a machine learning model to detect fraudulent transactions in real-time. It uses supervised learning techniques and integrates a simple API for live predictions.

## Features

- Supervised machine learning model (Logistic Regression)
- Real-time fraud detection using Flask API
- Clean and modular Python code
- Dataset preprocessing and feature engineering
- Easy to understand and extend

## Project Structure

- `data/`: Contains the sample transaction dataset
- `models/`: Stores the serialized trained model
- `src/`: Core Python scripts for preprocessing, training, and prediction
- `app/`: Flask-based API for real-time fraud prediction

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
````

## How to Run

### 1. Train the Model

```bash
python src/train_model.py
```

This will save a model file in the `models/` directory.

### 2. Start the API Server

```bash
python app/app.py
```

Access the API at `http://127.0.0.1:5000/predict`

### 3. Send a Prediction Request

Use `curl` or Postman to POST JSON:

```json
{
  "amount": 250.00,
  "oldbalanceOrg": 1000.00,
  "newbalanceOrig": 750.00,
  "type": "TRANSFER"
}
```

## Example Response

```json
{
  "prediction": "Fraudulent"
}
```

## Future Improvements

* Model explainability using SHAP or LIME
* More advanced algorithms (XGBoost, Random Forest)
* Secure authentication for the API
* Integration with a front-end dashboard

## License

This project is created for academic purposes. Free to use with credit.
