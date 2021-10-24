from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'_username': '[oscarkav@gmail.com]',
           '_password': '[OSC741@ooooo]'}

# Post the payload to the site to log in
s = session.post("https://vms.workforcelogiq.com/login/login?TabId=4", data=payload)

# Navigate to the next page and scrape the data
s2 = session.get('https://vms.workforcelogiq.com/Requisition/StaffAugReqList?TabId=1')
# print(s2)
soup = BeautifulSoup(s.text, 'html.parser')
outF = open("myOutFile.txt", "w")
for line in soup:
    # write line to output file
    outF.write(line)
    outF.write("\n")
outF.close()
# soup.find('img')['src']
