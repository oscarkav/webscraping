from time import sleep

import requests
import codecs
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
mypath = 'C:\\Users\\malin\\OneDrive\\Dokument\\Python\\webscraping\\week45'
# download the html files using add-on to chrome (DownThemAll) and put them on a path as above
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)
print(len(onlyfiles))
for n in range(len(onlyfiles)):
    print(n)
    f = codecs.open(mypath+"\\"+onlyfiles[n], encoding='utf-8')
    s = f.read()
    #soup = BeautifulSoup(f,"lxml")

    soup = BeautifulSoup(s, 'html.parser')
    #div1=soup.find()
    detail_all_html = soup.find("div", {"id": "VendorReqDetail"})
#    print(detail_all_html)
    detail1 = detail_all_html.find("div", {"class": "alert alert-warning"})
#    #print(detail1)
    deadline_time = detail1.find("span", {"id": "warningText"}).find_next(text=True)
#    print("-------------------")
#    print(deadline_time)
    f = open("myfile_w45.html", "a")
    f.write("\n"+"\n"+"<hr>"+"------------"+"\n")
    f.write(str(deadline_time)+"------------"+"\n")
    sleep(1)
    f.close()
    req_name = detail_all_html.find("div", {"class": "caption"}).find_next(text=True)
#    print("-----------------------")
#    print(req_name)
    f = open("myfile_w45.html", "a")
    f.write("<br> <br> ")
    f.write("\n"+str(req_name)+"\n"+"<br>")
    sleep(1)
    f.close()


    description1 = detail_all_html.find("li", {"class": "span11 no-margin"}).find_next(text=True)
    description2 = detail_all_html.find("li", {"class": "span11 no-margin"}).find_all(text=True)
    description_all = detail_all_html.find("li", {"class": "span11 no-margin"})
#    print("-------------------------------")
#    print(description1)
#    print(description2)
#    print("-----------------------------------")
#    #print(description_all)
    requirements_all = detail_all_html.find_all("li", {"class": "span11 no-margin"})
#    print(requirements_all)
    f = open("myfile_w45.html", "a")
    sleep(1)
    f.write("\n"+str(requirements_all)+"\n")
    sleep(2)
    f.close()
