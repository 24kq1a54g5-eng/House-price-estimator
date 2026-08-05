import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Read the dataset
data = pd.read_csv("dataset.csv")

# Input features
X = data[["Area", "Bedrooms", "Bathrooms", "Age"]]

# Output
y = data["Price"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "house_price_model.pkl")

print("✅ AI model saved successfully!")