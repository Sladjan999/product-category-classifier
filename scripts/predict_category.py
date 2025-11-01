import joblib

model = joblib.load("model/product_classifier.pkl")

print("=== AUTOMATSKA KLASIFIKACIJA PROIZVODA ===")
while True:
    text = input("\nUnesi naziv proizvoda (ili 'exit' za kraj): ")
    if text.lower() == 'exit':
        break
    pred = model.predict([text])[0]
    print(f"➡️ Predviđena kategorija: {pred}")