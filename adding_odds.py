import pandas as pd

# Define the file paths for the input files
training_set_file = 'training_set.csv'
combined_data_file = 'combined_data.csv'

# Load the training set CSV file to extract team names
training_data = pd.read_csv(training_set_file)

# Load the combined data CSV file
combined_data = pd.read_csv(combined_data_file)

# Iterate through rows in the training set
for index, row in training_data.iterrows():
    home_team = row['Home_team']
    away_team = row['Away_team']

    # Check if the game is already present in the combined data
    game_exists = ((combined_data['Home_team'] == home_team) & (combined_data['Away_team'] == away_team)) | \
                  ((combined_data['Home_team'] == away_team) &
                   (combined_data['Away_team'] == home_team))

    if not game_exists.any():
        # If the game is not present, create a new row with odds and add it to the combined data
        new_game = {
            'Home_team': home_team,
            'Away_team': away_team,
            'home_odds': row['home_odds'],
            'draw_odds': row['draw_odds'],
            'away_odds': row['away_odds'],
            # You may need to add more columns based on your data
        }

        combined_data = combined_data.append(new_game, ignore_index=True)

# Save the updated combined data to the same file
combined_data.to_csv(combined_data_file, index=False)

print("Games and odds from the training set have been added to the combined data.")
