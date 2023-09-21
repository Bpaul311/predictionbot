import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Initialize the Edge WebDriver
driver = webdriver.Edge()
# navigate to get the odds and the odds elements
driver.get('https://www.betpawa.rw/virtual-sports?virtualTab=upcoming')
odds_elements = driver.find_elements(
    By.CSS_SELECTOR, 'span.event-odds')
# extract the odds
odds = [odds_element.text for odds_element in odds_elements]
# loop to get the odds
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['game_no', 'home_odds', 'draw_odds', 'away_odds'])
    for j in range(0, 30, 3):
        home_odds, draw_odds, away_odds = tuple(odds[j:j+3])
        game_no = (j//3)+1
        # Write the data to the CSV
        writer.writerow([game_no, home_odds, draw_odds, away_odds])
