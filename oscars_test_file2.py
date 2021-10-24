from time import sleep

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
print(login_url)
print(dashboard_url)
print(req_url)
print(psw.counter)
print("-------------------------------------------------------")
# Create the payload
payload = {'username': psw.username,
           'password': psw.password}

with requests.Session() as s:
    r = s.post(login_url, headers=psw.headers, params=psw.params, data=psw.data)
    sleep(10)
    r2 = s.get(dashboard_url)
    sleep(10)
    r3 = s.get(req_url)
    sleep(10)
    soup = BeautifulSoup(r3.content, "html.parser")
    print(soup.prettify())
    print("THIS IS IT-------------------------------")
    # print(soup.findAll("Log In"))
