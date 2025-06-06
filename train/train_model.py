import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import os

# Load data
df = pd.read_csv("data/house_prices.csv")

# Fill missing values if any
df.fillna(0, inplace=True)

# Encode 'Dimensions' column (text to numbers)
le = LabelEncoder()
df['Dimensions'] = le.fit_transform(df['Dimensions'].astype(str))

# Features (X) and target (y)
X = df[['Dimensions', 'Plot Area']]  # Only numeric columns
y = df['Price (in rupees)']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
os.makedirs("app", exist_ok=True)
joblib.dump(model, "app/model.pkl")

print("✅ Model trained and saved to app/model.pkl")
