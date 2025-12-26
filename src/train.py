import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error


base_path = "./excel/"
excel_file_path = f"{base_path}/data_cleaned.xlsx"

features = ['title', 'description', 'hour_posted', 'has_image']
data = pd.read_excel(excel_file_path)
X = data[features]
y = data['likes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, './data/model.joblib')

predictions = model.predict(X_test)
score = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(f"Shapes: X_train {X_train.shape}, y_train {y_train.shape}, X_test {X_test.shape}, y_test {y_test.shape}")
print(f"R2 Score (Accuracy): {score:.4f}")
print(f"Average Error: {mae:.2f} likes")