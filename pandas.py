import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load the dataset
data = pd.read_csv('combined.csv')

# Step 2: Data Cleaning (if needed)
# You can check for missing values and handle them, and perform any other data cleaning tasks here.

# Step 3: One-Hot Encoding for Categorical Variables (home_team and away_team)
data = pd.get_dummies(data, columns=['home_team', 'away_team'])

# Step 4: Split the data into features (X) and target (y)
# Assuming you want to predict 'home_score' and 'away_score'
X = data.drop(['home_score', 'away_score'], axis=1)
y_home = data['home_score']
y_away = data['away_score']

# Step 5: Split the data into training and testing sets
X_train, X_test, y_home_train, y_home_test, y_away_train, y_away_test = train_test_split(
    X, y_home, y_away, test_size=0.2, random_state=42)

# Now, you have X_train, X_test, y_home_train, y_home_test, y_away_train, y_away_test
# ready for training and testing your machine learning models.
