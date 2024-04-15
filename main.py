from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

code = input("Enter Problem Code")
typ= input("Enter problem Sequence")
file_path="C:\\Users\\LENOVO\\Desktop\\vscode\\B_Nene_and_the_Card_Game.cpp"
# data = ""
# print("paste code and press enter")
# while True:
#     line = input()
#     if not line:
#         break
#     data += line + "\n"

# data = data.rstrip("\n")
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://codeforces.com/problemset/problem/"+code+'/'+typ)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Enter"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Enter")
link.click()
# link.clear()
input_email = driver.find_element(By.ID,"handleOrEmail")
input_email.send_keys("bhagrawal24@gmail.com")
input_pass = driver.find_element(By.ID,"password")
input_pass.send_keys("Bh@vy@24"+ Keys.ENTER)
driver.implicitly_wait(10)  # Waits up to 10 seconds

link2 = driver.find_element(By.PARTIAL_LINK_TEXT,"SUBMIT")
link2.click()
driver.implicitly_wait(5)
input_code = driver.find_element(By.XPATH,'//*[@id="pageContent"]/form/table/tbody/tr[5]/td[2]/input')
input_code.send_keys(file_path)
# input_code.send_keys("C:\Users\LENOVO\Desktop\vscode\B_Nene_and_the_Card_Game.cpp")
driver.implicitly_wait(5)
link3 = driver.find_element(By.CLASS_NAME,"submit")
link3.click()
time.sleep(20)
driver.quit()



