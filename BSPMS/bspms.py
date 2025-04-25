import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

service = Service(executable_path="C:/Users/Teacher/Desktop/Report/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://10.10.99.18:8004/login")

title = driver.title
expected_title = "BSPMS - Balik Scientist Program Management System"

if expected_title != title:
    messagebox.showerror("Login Failed", "Page title doesn't match.")
    raise AssertionError("Login Test Failed")
else:
    print("Login Successfully")

email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
time.sleep(2)
email_input.send_keys("sjjinahon@gmail.com")
password.send_keys("Dost@123")
login_button.click()
time.sleep(3)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(3)

Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
driver.execute_script("arguments[0].click();", Log_Out)
time.sleep(2)

email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')

email_input.send_keys("sjjinahon@gmail.com")
password.send_keys("Dost@123")
login_button.click()
time.sleep(2)


No = driver.find_element(By.XPATH, '//span[contains(@class, "ascending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No)
time.sleep(1)
No1 = driver.find_element(By.XPATH, '//span[contains(@class, "descending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No1)
time.sleep(1)

Name = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name)
time.sleep(1)
Name1 = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name1)
time.sleep(1)

Engagement = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement)
time.sleep(1)
Engagement1 = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement1)
time.sleep(1)

HostI = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI)
time.sleep(1)
HostI1 = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI1)
time.sleep(1)

Status = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status)
time.sleep(1)
Status1 = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status1)
time.sleep(1)

# Click to open the dropdown (optional visual action)
dropdown_element = driver.find_element(By.ID, "council_filter")
dropdown_element.click()
# Then select using Select
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("DOST-CO")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCAARRD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCIEERD")
time.sleep(1)
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("PCHRD")

dropdown1 = driver.find_element(By.ID, 'status_filter')
dropdown1.click()
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approval')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Legal Clearance')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Evaluation')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Request')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Others')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Approved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Disapproved')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Revision')
time.sleep(1)
dropdown_status = Select(dropdown1)
dropdown_status.select_by_visible_text('Status')
time.sleep(1)

search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ñew")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("ÑEW")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("M@%ks*")
time.sleep(2)
search_input.clear()
search_input = driver.find_element(By.ID, 'applications_search')
search_input.send_keys("Christian")
time.sleep(2)

Select_data = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr/td[2]')
driver.execute_script("arguments[0].click();", Select_data)
time.sleep(1)

input("Press Enter to exit and close the browser...")
driver.quit()
