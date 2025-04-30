import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
    print("Logged in Successfully")

email_input = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
time.sleep(2)
email_input.send_keys("")
password.send_keys("")
try:
    assert email_input.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"1st attempt Assertion failed: {e}")

login_button.click()
time.sleep(3)

email_input1 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password1 = driver.find_element(By.ID, "password")
login_button1 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input1.send_keys("sjjinahon@gmail.com")
password1.send_keys("")
login_button1.click()
time.sleep(3)
try:
    assert email_input1.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password1.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"2nd attempt Assertion failed: {e}")

email_input1.clear()
email_input2 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password2 = driver.find_element(By.ID, "password")
login_button2 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input2.send_keys("")
password2.send_keys("Dost@123")
login_button2.click()
time.sleep(3)
try:
    assert email_input2.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password2.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"3rd attempt Assertion failed: {e}")

password2.clear()
email_input3 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password3 = driver.find_element(By.ID, "password")
login_button3 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input3.send_keys("jioclyde@gmail.com")
password3.send_keys("Dost@123")
login_button3.click()
time.sleep(3)
try:
    assert email_input3.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password3.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"4th attempt Assertion failed: {e}")

email_input3.clear()
password3.clear()
email_input4 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password4 = driver.find_element(By.ID, "password")
login_button4 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input4.send_keys("sjjinahon@gmail.com")
password4.send_keys("Dost@12345")
login_button4.click()
time.sleep(3)
try:
    assert email_input4.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password4.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"5th attempt Assertion failed: {e}")

email_input4.clear()
password4.clear()
email_input5 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password5 = driver.find_element(By.ID, "password")
login_button5 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input5.send_keys("jioclyde@gmail.com")
password5.send_keys("123456")
login_button5.click()
time.sleep(3)
try:
    assert email_input5.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password5.get_attribute("value") == "Dost@123", "Password input mismatch"
except AssertionError as e:
    print(f"6th attempt Assertion failed: {e}")

email_input5.clear()
password5.clear()
email_input6 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password6 = driver.find_element(By.ID, "password")
login_button6 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input6.send_keys("sjjinahon@gmail.com")
password6.send_keys("Dost@123")
try:
    assert email_input6.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password6.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button6.click()
time.sleep(3)

print("Successfully entered the page.")

try:
    Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
    assert Profile.is_displayed(), "Profile button is not visible."
    driver.execute_script("arguments[0].click();", Profile)
    time.sleep(3)
    print("Navigated to profile page.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Profile: {e}")

print("Navigated to profile page.")

try:
    Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
    assert Change_pass.is_displayed(), "Change Password button is not visible."
    driver.execute_script("arguments[0].click();", Change_pass)
    time.sleep(2)
    print("The Change Password button was clicked.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking Change Password: {e}")

try:
    Close_but = driver.find_element(By.ID, "change_password_modal_close")
    assert Close_but.is_displayed(), "Close button is not visible."
    driver.execute_script("arguments[0].click();", Close_but)
    time.sleep(2)
    print("It closed the close button of the change password modal.")
except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"Error occurred while clicking the close button: {e}")

Change_pas = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pas)
time.sleep(2)
print("The Change Password button was clicked.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Save = driver.find_element(By.XPATH, '//*[@id="save_password_button"]')

Current_pass.send_keys("Dost@12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@12345")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(3)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')

ok = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
driver.execute_script("arguments[0].click();", ok)
time.sleep(2)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(2)

Change_pass = driver.find_element(By.XPATH, '//*[@id="change_password_button"]')
driver.execute_script("arguments[0].click();", Change_pass)
time.sleep(2)
Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Confirm_pass.send_keys("Dost@12")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@1")
New_pass.send_keys("Dost@1")
Confirm_pass.send_keys("A7f$5Lp@9xQ2mZe6sW1vBn8T#pY4dJhVkC5uEoGqRtX1y!Ws12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("")
Confirm_pass.send_keys("Dost@12345")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("")
Save.click()
time.sleep(2)
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.clear()
New_pass.clear()
Confirm_pass.clear()
time.sleep(2)

Current_pass = driver.find_element(By.XPATH, '//*[@id="current_password"]')
New_pass = driver.find_element(By.XPATH, '//*[@id="new_password"]')
Confirm_pass = driver.find_element(By.XPATH, '//*[@id="new_password_confirmation"]')
Current_pass.send_keys("Dost@123")
New_pass.send_keys("Dost@123")
Confirm_pass.send_keys("Dost@123")
try:
    assert Current_pass.get_attribute("value") == "Dost@123", "Current password mismatch"
    assert New_pass.get_attribute("value") == "Dost@123", "New password mismatch"
    assert Confirm_pass.get_attribute("value") == "Dost@123", "Confirm password mismatch"
    print("Change password Successfully")
except AssertionError as e:
    print(f"Password fields assertion failed: {e}")
else:
    print("Password change process completed.")
Save.click()
time.sleep(2)

ok_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='OK']")
ok_button.click()
time.sleep(2)

email_input6 = wait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password6 = driver.find_element(By.ID, "password")
login_button6 = driver.find_element(By.XPATH, '//button[text()="Login"]')
email_input6.send_keys("sjjinahon@gmail.com")
password6.send_keys("Dost@123")
try:
    assert email_input6.get_attribute("value") == "sjjinahon@gmail.com", "Email input mismatch"
    assert password6.get_attribute("value") == "Dost@123", "Password input mismatch"
    print("Logged in Successfully")
except AssertionError as e:
    print(f"7th attempt Assertion failed: {e}")
login_button6.click()
time.sleep(3)

print("Successfully entered the page.")

Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)

assign_to = wait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='assign-menu-item']")))
ActionChains(driver).move_to_element(assign_to).perform()
Alist = wait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='assign-submenu']/div/button[1]")))
print("Found Assign to:", assign_to.text)
driver.execute_script("arguments[0].style.border='2px solid gray'", Alist)
time.sleep(4)
driver.execute_script("arguments[0].style.border=''", assign_to)

Edit = driver.find_element(By.XPATH, '//*[@id="edit-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Edit)
ActionChains(driver).move_to_element(Edit).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Edit)
time.sleep(3)
driver.back()
time.sleep(2)
driver.execute_script("arguments[0].style.border=''", Edit)

Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Track = driver.find_element(By.XPATH, '//*[@id="track-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Track)
ActionChains(driver).move_to_element(Track).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Track)
time.sleep(3)
Close = driver.find_element(By.XPATH, '//*[@id="tracking-modal"]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", Close)
time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Track)

Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Attach = driver.find_element(By.XPATH, '//*[@id="attach-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Attach)
ActionChains(driver).move_to_element(Attach).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Attach)
time.sleep(3)
Close_A = driver.find_element(By.XPATH, '//*[@id="attachments-modal"]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", Close_A)
time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Attach)

Ellipsissss = driver.find_element(By.XPATH, '//*[@id="applications_table"]/tbody/tr[1]/td[6]/div/button')
driver.execute_script("arguments[0].click();", Ellipsissss)
time.sleep(3)
Delete = driver.find_element(By.XPATH, '//*[@id="delete-menu-item"]')
driver.execute_script("arguments[0].style.border='2px solid gray'", Delete)
ActionChains(driver).move_to_element(Delete).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", Delete)
time.sleep(3)
Cancel = driver.find_element(By.XPATH, "//button[@class='swal2-cancel swal2-styled' and text()='Cancel']")
driver.execute_script("arguments[0].click();", Cancel)
time.sleep(3)
driver.execute_script("arguments[0].style.border=''", Delete)

No = driver.find_element(By.XPATH, '//span[contains(@class, "ascending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No)
time.sleep(2)
No1 = driver.find_element(By.XPATH, '//span[contains(@class, "descending") and contains(@class, "icon-[solar--sort-vertical-bold-duotone]")]')
driver.execute_script("arguments[0].click();", No1)
time.sleep(2)

Name = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name)
time.sleep(2)
Name1 = driver.find_element(By.XPATH, '//span[text()="Name"]')
driver.execute_script("arguments[0].click();", Name1)
time.sleep(2)

Engagement = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement)
time.sleep(2)
Engagement1 = driver.find_element(By.XPATH, '//span[text()="Engagement"]')
driver.execute_script("arguments[0].click();", Engagement1)
time.sleep(2)

HostI = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI)
time.sleep(2)
HostI1 = driver.find_element(By.XPATH, '//span[text()="Host Institution"]')
driver.execute_script("arguments[0].click();", HostI1)
time.sleep(2)

Status = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status)
time.sleep(2)
Status1 = driver.find_element(By.XPATH, '//span[text()="Status"]')
driver.execute_script("arguments[0].click();", Status1)
time.sleep(2)


dropdown_element = driver.find_element(By.ID, "council_filter")
dropdown_element.click()
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
time.sleep(1)

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
time.sleep(5)
print("Data had been selected")

original_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    driver.switch_to.window(window)
    if "BSPMS - Balik Scientist Program Management System" in driver.title:
        print("Currently at Selected Profile window.")
        break

driver.get("http://10.10.99.18:8004/applications")

print("Navigated to BSPMS")
time.sleep(3)

Profile = driver.find_element(By.XPATH, '//*[@id="user-menu-button"]')
driver.execute_script("arguments[0].click();", Profile)
time.sleep(3)
print("Navigated to profile page.")

Log_Out = driver.find_element(By.XPATH, '//*[@id="logout-button"]')
driver.execute_script("arguments[0].click();", Log_Out)
time.sleep(2)
print("Logout completed.")

input("Press Enter to exit and close the browser...")
driver.quit()