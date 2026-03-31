import pandas as pd

# Load dataset
df = pd.read_csv("log_data.csv")

# Extract hour from time
df['hour'] = df['time'].str.split(':').str[0].astype(int)

# Rule-based anomaly detection
def detect_anomaly(row):
    if row['hour'] < 6 or row['login_attempts'] > 4 or row['location'] == 'Unknown':
        return "Anomaly"
    else:
        return "Normal"

df['status'] = df.apply(detect_anomaly, axis=1)

print(df)

import matplotlib.pyplot as plt

df['status'].value_counts().plot(kind='bar')
plt.title("Anomaly Detection Result")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()