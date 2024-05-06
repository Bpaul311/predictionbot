from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import keyboard
from selenium.webdriver.common.keys import Keys

options = Options()
listofteams = ["LIV","AST","TOT","MCI","NEW","EVE","WHU","CHE","CRY","MUN","NOT","FUL","ARS","SHU","BHA","WOL","LUT","BUR","BRE","BOU"]
options.add_argument('--headless=new')
PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
time.sleep(4)
num = 0
data = []
full_results = []
wagered_amount = 100
total_seasonal_profit = []
seasonal_profit = 0
profit_data = []
while num < 1:
    while True:
        try:
            driver = webdriver.Chrome(service=s, options=options)
            driver.get("https://www.betpawa.rw/virtual-sports?virtualTab=upcoming")
            current_time = time.strftime("%H:%M")
            time.sleep(4)
            matches= driver.find_elements(By.CSS_SELECTOR,".events-container")
            tab = driver.find_element(By.CSS_SELECTOR, ".tabs-selector.active")
            try:
                matchday = tab.find_element(By.CSS_SELECTOR, ".round-number").text
            except:
                matchday = tab.find_element(By.CSS_SELECTOR, ".tab-text").text
            matchday_time = tab.find_element(By.CSS_SELECTOR, ".tab-badge").text
            print(matchday, current_time)
            for match in matches[:10]:
                team_names = match.find_element(By.CSS_SELECTOR, ".title").text.split(' - ')
                match_odds = list(map(lambda x: x.text.split('\n')[1], match.find_elements(By.CSS_SELECTOR, ".event-bet-wrapper.bet-price")))
                data.append({'matchday': matchday, 'matchday_time': matchday_time,'team1': team_names[0], 'team2': team_names[1], 'team1odds': match_odds[0], 'drawodds': match_odds[1], 'team2odds': match_odds[2]})
            timer = driver.find_element(By.CSS_SELECTOR, ".kick-off-timer.bold").text
            time_to_sleep = int(timer.split(':')[0]) * 60 + int(timer.split(':')[1])
            time.sleep(time_to_sleep + 120)
            break
        except Exception as e:
            print('first part error', e)
            continue
    while True:
        try:
            if matchday != '1':
                driver1 = webdriver.Chrome(service=s, options=options)
                driver1.get("https://www.betpawa.rw/virtual-sports?virtualTab=results")
                time.sleep(4)
                clickon = driver1.find_elements(By.CSS_SELECTOR,'.tabs-selector.last')
                click_on = list(filter(lambda x: x.text == 'Matchdays', clickon))
                click_on[-1].click()
                time.sleep(2)
                match_day = driver1.find_elements(By.CLASS_NAME,'matchday')
                match_day[int(matchday) - 1].click()
                time.sleep(2)
                results = driver1.find_elements(By.CLASS_NAME,'score')
                results = list(map(lambda x: x.find_elements(By.TAG_NAME,'span')[-1].text.split(' - '), results[:10]))
                matchday_profit = 0
                for i in  range(1, 11):
                    smallest_odd = min(float(data[-i]['team1odds']), float(data[-i]['drawodds']), float(data[-i]['team2odds']))
                    if (float(data[-i]['team1odds']) == smallest_odd and (float(results[-i][0]) - float(results[-i][1])) > 0) or (float(data[-i]['drawodds']) == smallest_odd and (float(results[-i][0]) - float(results[-i][1])) == 0) or (float(data[-i]['team2odds']) == smallest_odd and (float(results[-i][0]) - float(results[-i][1])) < 0):
                        data[-i]['profit'] = wagered_amount * smallest_odd
                        matchday_profit += (wagered_amount * smallest_odd)
                    else:
                        data[-i]['profit'] = 0
                        matchday_profit += 0
                profit_data.append({'matchday': matchday, 'profit': matchday_profit})
                seasonal_profit += (matchday_profit - 1000)
                if matchday == '34':
                    total_seasonal_profit.append(seasonal_profit)
                    print(seasonal_profit)
                    seasonal_profit = 0
                print(matchday ,(matchday_profit - 1000))
            driver.quit()
            break
        except Exception as e:
            print(e)
            continue
        # if matchday != '0':
        #     season = driver1.find_element(By.CSS_SELECTOR, '.season-select').find_elements(By.CSS_SELECTOR, 'option')[1]
        #     season.click()
        #     time.sleep(2)
        #     match_day = driver1.find_element(By.CLASS_NAME,'matchday')
        #     match_day.click()
        #     matchday_url = driver1.current_url
        #     print(matchday_url[-1])
        

