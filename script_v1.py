# Python automation page for checking Cathay Pacific 
# Award return flight
# This script is not currently working
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.calpassplus.org/LaunchBoard/Student-Success-Metrics.aspx")
driver.fullscreen_window()

wait = WebDriverWait(driver, 30)

time.sleep(3)

# Click `All Students`
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="journeyBox5"]/div[2]/h2')))
students_group = driver.find_element(By.XPATH, '//*[@id="journeyBox5"]/div[2]/h2')
students_group.click()

# Click College Radio button
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="collegeFilterBtn"]')))
college_button = driver.find_element(By.XPATH, '//*[@id="collegeFilterBtn"]')
college_button.click()

# Click Drill Down and select Race/Ethnicity
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectionContainer"]/div/div[4]/span/span[1]/span')))
drill_down = driver.find_element(By.XPATH, '//*[@id="selectionContainer"]/div/div[4]/span/span[1]/span')
drill_down.click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[2]/ul/li[2]/ul/li[1]')))
race_eth = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]/ul/li[1]')
race_eth.click()

# Click `export`
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]')))
export_button = driver.find_element(By.XPATH, '//*[@id="export"]')
export_button.click()

time.sleep(10)

# Now loop through the rest of 119 schools (We downloaded first one already)
schools = 120
for i in range(1,schools+1):

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectionContainer"]/div/div[2]/span/span[1]/span')))
    college_box = driver.find_element(By.XPATH, '//*[@id="selectionContainer"]/div/div[2]/span/span[1]/span')
    college_box.click()
    
    time.sleep(2)

    # 2. Iterate one down
    college_box.send_keys(Keys.DOWN, Keys.ENTER)

    time.sleep(5)

    # 3. Click refresh button
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view"]')))
    refresh_button = driver.find_element(By.XPATH, '//*[@id="view"]')
    refresh_button.click()

    time.sleep(5)

    # 4. Click Export
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]')))
    export_button = driver.find_element(By.XPATH, '//*[@id="export"]')
    export_button.click()

    time.sleep(15)

driver.close()