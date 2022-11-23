import os
from twilio.rest import Client
import urllib3
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
    
    
     
username = "#######"
password = "##########"

ipaddress = ['http://41.186.195.8', 'http://192.168.10.220']

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

response = os.system("ping -c 1 " + ipaddress[0])
def broadcastthison(useaddress): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    usethisaddress = useaddress + '/home/'
    driver.get(usethisaddress)
    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "#########"
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "###########"
    client = Client(account_sid, auth_token)
    http = urllib3.PoolManager()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "username-input"))).send_keys(username)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "password-input"))).send_keys(password)

    # click login buttons
    driver.find_element(By.CSS_SELECTOR,"button.mat-raised-button").click()
    time.sleep(5)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    time.sleep(5)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    time.sleep(5)
    pickle.load(open("cookies.pkl", "rb"))
    time.sleep(5)
    # NR5
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=NR5&childDashboardId=87244680-4d1b-11ec-8aaf-a717ceed4d4c&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
    # NR4
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=NR4&childDashboardId=37c3ec90-1a56-11ed-937e-37e352202184&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
     # NR18
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=NR18&childDashboardId=cd72f950-4d1c-11ec-8aaf-a717ceed4d4c&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
     # KGC
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=Kigali%20golf%20club&childDashboardId=305af360-4d1d-11ec-8aaf-a717ceed4d4c&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
     # BIGOGWE
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=BIGOGWE&childDashboardId=cacba4a0-1d31-11ed-937e-37e352202184&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
      # MASAKA
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=MASAKA&childDashboardId=7826e250-196c-11ed-937e-37e352202184&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
      # MURINDI-RUSORORO
    driver.get(useaddress+'/iframeView/child?stateId=Projects&dashboardId=bd91d580-4d01-11ec-8aaf-a717ceed4d4c&setAccessToken=false&childStateId=MURINDI-RUSORORO&childDashboardId=2fb139e0-3801-11ed-af80-8faf9b30bf81&childHideDashboardToolbar=false&childSetAccessToken=false')
    time.sleep(10)
    driver.find_elements(By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base.mat-raised-button")[2].click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR,"button.ajs-button.ajs-ok")[0].click()
    time.sleep(5)
    print('success')
    driver.close()


if response == 0:
    useaddress = ipaddress[0]
    broadcastthison(useaddress)
else:
    useaddress = ipaddress[1]
    broadcastthison(useaddress)


