import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the CSV file
file_path = '/mnt/data/fictional_bank_transactions.csv'
df = pd.read_csv(file_path)

# Data Preprocessing
# Converting 'TransactionType' from categorical to numerical using LabelEncoder
label_encoder = LabelEncoder()
df['TransactionType'] = label_encoder.fit_transform(df['TransactionType'])

# Splitting the dataset into features (X) and target (y)
X = df.drop(['TransactionID', 'Date', 'AccountBalance', 'Expenses', 'CashFlow', 'NetWorth', 'CreditScore'], axis=1)
y = df['TransactionType']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating and training a RandomForestClassifier model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predicting on the test set
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Displaying the results
print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)
