from selenium import webdriver
import time
import csv
import json 

import bs4 as BeautifulSoup
import requests
from selenium.webdriver.common.by import By

######################################################################################
### Please make sure you read readme_Automater_py before.                      #####
### This file defines the bot to be used by the developers to get content online #####
### depending on the website you might want to secure your cerdentials in the    #####
### before scarpping the content.                                                #####
######################################################################################


class Automater():
    
    ### Initiation the class
    def __init__(self,cred_file,default_delay = 8):
        self.file = cred_file
        self.credentials = self.get_credentials()
        # Use self.browser = webdriver.Chrome() if not
        self.browser = webdriver.Chrome(executable_path="D:\Sauvegarde\2021-2022\Python Scripting\Web_Scrapping\chromedriver.exe")
        self.delay = default_delay
        
    #############################################
    ######## get credentials from file ##########
    ######## a file for secure login to #########
    ######## website to be scrapped     #########
    #############################################
    
    def get_credentials(self):
        credentials = list()
        with open(self.file) as credentials_File:
            for item in credentials_File:
                str_itm = str(item)
                #str_itm = str_itm.lstrip("\n")
                _,str_itm = str_itm.split(":")
                credentials.append(str_itm.strip("\n"))
        
        return credentials
      
    ###########################################################################################
    ### For this method, the bot gets results form google while using the research keyword ####
    ###########################################################################################

    def googling (self,research,delay): 
        self.browser.get("https://google.com")
        time.sleep(self.delay)
        button=browser.find_element_by_css_selector("#L2AGLb")
        time.sleep(self.delay)
        button.click()
        time.sleep(self.delay)
        input=browser.find_element_by_css_selector(".gLFyf.gsfi")
        input.send_keys(research)
        time.sleep(self.delay)
        input1=browser.find_element_by_css_selector(".gNO89b")
        time.sleep(self.delay)
        input1.click()
        time.sleep(self.delay)
        open1=browser.find_element_by_css_selector(".LC20lb.DKV0Md")
        time.sleep(self.delay)
        open1.click()
        time.sleep(self.delay)
    #############################################################
    ###### Connects the bot to url if login is necessary    #####
    ###### input : (string) url                             #####
    ############################################################# 
    
    def connect(self,url):
        browser = self.browser
        #browser = webdriver.Chrome()
        time.sleep(self.delay)
        browser.get("https://impactcentrechretien.elvanto.eu/login/")
        time.sleep(self.delay)
        elvanto_login = browser.find_element(By.CLASS_NAME, "form-control")
        time.sleep(self.delay)
        elvanto_login.send_keys(self.credentials[0])
        time.sleep(self.delay)
        elvanto_pw = browser.find_element(By.ID, "member_password")
        time.sleep(self.delay)
        elvanto_pw.send_keys(self.credentials[1])
        time.sleep(self.delay)
        connexion_btn = browser.find_element(By.CLASS_NAME, "btn.btn-submit.btn-block")
        time.sleep(8)
        connexion_btn.click()
        
        print("Bot says : Connected !")
        
        return True
    
    def get_content(self):
        
        browser = self.browser
        
        return
        
        
    
if __name__ == "__main__":
    
    test_bot = Automater("elvanto_credentials.txt")
    bots_con = test_bot.connect()
