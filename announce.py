#!/usr/bin/env python
from selenium import webdriver
import time, requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from gi.repository import Notify as nt

username  = ""
pwd = ""

driver = webdriver.PhantomJS()

driver.get("http://skillrack.com/faces/ui/profile.xhtml")
time.sleep(3)
emailid = driver.find_element_by_name("j_username").send_keys(username)

password = driver.find_element_by_name("j_password").send_keys(pwd)

signin=driver.find_element_by_name('j_id_s').click()

driver.get("http://skillrack.com/faces/candidate/testlist.xhtml?TT=MCQ")

source_code = driver.page_source

test_name = bs(source_code,"lxml").find("table",{"class":"table table-striped table-hover"}).findAll("td")[1].text

nt.init("App Name")
nt.Notification.new(test_name).show()