import joblib
import pandas


# Load the trained model from the saved file
model_filename = 'our_gaussian_naive_bayes_model.pkl'
model = joblib.load(model_filename)

# Tuyiha home_odds, draw_odds, away_odds, home_wins, draw_no, away_wins
new_data = pandas.DataFrame({
    'home_odds': [2.8],
    'draw_odds': [3.35],
    'away_odds': [2.80],
    'home_wins': [1],
    'draws_no': [2],
    'away_wins': [0],
})

prediction = model.predict(new_data)

print(prediction)
