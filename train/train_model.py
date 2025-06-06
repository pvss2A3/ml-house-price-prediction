import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv('data/house_prices.csv')

# Fill missing values if any
df.fillna(0, inplace=True)

# Encode 'Dimensions' column (text to numbers)
le = LabelEncoder()
df['Dimensions'] = le.fit_transform(df['Dimensions'].astype(str))

# Features (X) and target (y)
X = df[['Dimensions', 'Plot Area']]  # Only numeric columns
y = df['Price (in rupees)']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'app/model.pkl')
# Done
print("Model file created successfully!")
