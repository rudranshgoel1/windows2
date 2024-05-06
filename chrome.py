from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests

def login(username, password):
    driver = webdriver.Chrome()  # You may need to specify the path to your ChromeDriver executable
    driver.get("https://app.whatsupleads.com/login")  # URL of the login page
    wait = WebDriverWait(driver, 10)

    # Find and fill in the login form
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys(username)
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_field.send_keys(password)

    # Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
    login_button.click()

    return driver

def navigate_to_users_page(driver):
    # Navigate to the users page
    driver.get("https://app.whatsupleads.com/users")

def admin(driver):
    driver.get("https://app.whatsupleads.com/auth/back_to_admin")
    driver.get("https://app.whatsupleads.com")

def himanshu(driver):
    driver.get("https://app.whatsupleads.com/users/view/65fa7690e530c")
    driver.refresh()

def slimline(driver):
    driver.get("https://app.whatsupleads.com/users/view/6632277b1930d")
    driver.refresh()

def cature(driver):
    driver.get("https://app.whatsupleads.com/users/view/65fe9ba6d6882")
    driver.refresh()

def vd(driver):
    driver.get("https://app.whatsupleads.com/users/view/662105850d40a")
    driver.refresh()
        
def click_at_location2(driver, x, y):
    action = ActionChains(driver)
    action.move_by_offset(x, y).click().perform()

# Example usage
username = "admin"
password = "Ramlala123#"



driver = login(username, password)
driver.maximize_window()
navigate_to_users_page(driver)
driver.implicitly_wait(5)

himanshu(driver)
number_element = driver.find_element(By.CLASS_NAME, "fw-9.fs-30.text-success.d-flex")
himanshunum = number_element.text

admin(driver)
cature(driver)
number_element = driver.find_element(By.CLASS_NAME, "fw-9.fs-30.text-success.d-flex")
caturenum = number_element.text

driver.implicitly_wait(5)

admin(driver)
slimline(driver)
number_element = driver.find_element(By.CLASS_NAME, "fw-9.fs-30.text-success.d-flex")
slimlinenum = number_element.text

admin(driver)
vd(driver)
number_element = driver.find_element(By.CLASS_NAME, "fw-9.fs-30.text-success.d-flex")
vdnum = number_element.text


webhook_url = 'https://hooks.zapier.com/hooks/catch/11132241/3pw7oqg/'  # Replace with your actual webhook URL
data = {
    'Himanshu Industries': himanshunum,
    'Sunlight HARDWARE': slimlinenum,
    'Cature (Abhay Jain)': caturenum,
    'VD International': vdnum
}
response = requests.post(webhook_url, json=data)

print(response)

# Print the text content
print("Himanshu:", himanshunum)
print("Sunlight HARDWARE", slimlinenum)
print("Cature LLP (Abhay Jain):", caturenum)
print("VD International:", vdnum)

driver.get("https://app.whatsupleads.com/auth/logout")

driver.quit()
