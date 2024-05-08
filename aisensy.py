import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests


def login(username, password):
    driver = webdriver.Chrome()  # You may need to specify the path to your ChromeDriver executable
    driver.get("https://www.app.aisensy.com/login")  # URL of the login page
    wait = WebDriverWait(driver, 10)

    # Find and fill in the login form
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    username_field.send_keys(username)
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_field.send_keys(password)

    return driver


def project(driver):
    driver.get("https://www.app.aisensy.com/projects/636fc59193c9600eb723c1ae/campaigns/api/view/663228425b4a170bfaea96d3")


def lclick(driver, x, y):
    action = ActionChains(driver)
    action.move_by_offset(x, y).click().perform()

def dclick(driver, x, y):
    action = ActionChains(driver)
    action.move_by_offset(x, y).double_click().perform()
    

username = "app.whatsupleads@gmail.com"
password = "Createpwd123#"


driver = login(username, password)
driver.maximize_window()

continueb = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div/div/div/button')
continueb.click()

time.sleep(5)

driver.get("https://www.app.aisensy.com/projects/636fc59193c9600eb723c1ae/dashboard")
time.sleep(10)

money = driver.find_element(By.XPATH, '//*[@id="route-container"]/div/div[3]/div/div[2]/div/div[2]/div/div[5]/h3')
moneytext = money.text
cleaned_string = moneytext.replace("₹", "").replace(" ", "")

driver.implicitly_wait(100)
driver.switch_to.new_window('tab')
project(driver)

time.sleep(5)
dropdown = driver.find_element(By.XPATH, '//*[@id="route-container"]/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div/div/button')
dropdown.click()

todayt = driver.find_element(By.XPATH, "//*[text()='Today']")
todayt.click()

time.sleep(2)

value = driver.find_element(By.XPATH, '//*[@id="route-container"]/div/div[2]/div[1]/div[3]/div[2]/div/div[4]/div[2]/p[2]')
valuetext = value.text

print("The extracted value is:", valuetext)
print("Money Left in account is:", cleaned_string)


webhook_url = 'https://hooks.zapier.com/hooks/catch/11132241/3j2149l/'  # Replace with your actual webhook URL
data = {
    'Value': valuetext,
    'Money Left': cleaned_string
}
response = requests.post(webhook_url, json=data)

driver.quit()
