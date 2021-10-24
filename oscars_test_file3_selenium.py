import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import psw

# Start the session
session = requests.Session()
TabId = psw.counter[30]
print(TabId)
login_url= (f"https://vms.workforcelogiq.com/Login/Login?TabId={TabId}")
dashboard_url = (f"https://vms.workforcelogiq.com/Home/dashboard?TabId={TabId}")
req_url = (f"https://vms.workforcelogiq.com/Requisition/StaffAugReqList?TabId={TabId}")
print("-------------------------------------------------------")
# Create the payload
payload = {'username': psw.username,
           'password': psw.password}

with requests.Session() as s:
    r = s.post(login_url, headers=psw.headers, params=psw.params, data=psw.data)
    time.sleep(10)
    r2 = s.get(dashboard_url)
    time.sleep(10)
    r3 = s.get(req_url)
    time.sleep(10)
    soup = BeautifulSoup(r3.content, "html.parser")
    print(soup.prettify())
    print("THIS IS IT-------------------------------")
    # print(soup.findAll("Log In"))
