from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
url = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'F:\Web Scraping\Golabal\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(url)
press_on_button = driver.find_element(By.CSS_SELECTOR,'[analytics-event="All matches"]')
press_on_button.click()

all_tables = driver.find_elements(By.CSS_SELECTOR,'.panel-body table')
table = all_tables[0]
date = table.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(1)')

team_1 = table.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(2)')

score = table.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(3)')

team_2 = table.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(4)')

dates, teams_1, scores, teams_2 = [],[],[],[]

for i in range(len(date)):
    dates.append(date[i].text)
    teams_1.append(team_1[i].text)
    scores.append(str(score[i].text))
    teams_2.append(team_2[i].text)

driver.quit()
data = {"Date":dates, "Team_1":teams_1, "Score":scores, "Team_2":teams_2}
df = pd.DataFrame(data)
df.to_csv("Matches.csv", index=False)

