import joblib

model = joblib.load("svm.pkl")

def predict(pesan):
    predict = model.predict([pesan])
    if 0 in predict:
        return "SMS Normal"
    elif 1 in predict:
        return "Penipuan"
    else:
        return "Promosi"

