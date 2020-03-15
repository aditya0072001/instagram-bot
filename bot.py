from selenium import webdriver
from time import sleep
import random

class InstaBot:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome("C:\\Users\\aditya\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.username=username
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)
        
    def like(self):
        driver=self.driver
        hashtag_list = ['programming', 'sketch', 'meme','love','instagood','photooftheday','fashion','beautiful','happy','cute','tbt','like4like','followme','picoftheday','follow','meselfie','summer','art','instadaily','friends','repost','nature','girl','fun','style','smile','food']
        tag=-1
        liked=0
        for hashtag in hashtag_list:
            tag+=1
            driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
            sleep(5)
            first_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]')
            first_thumbnail.click()
            liked+=1
            sleep(2)
            liked=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
            sleep(random.randint(1,2)) 
            
        print("Liked ",liked)    
        
hehe=InstaBot('your username','your password')  
hehe.like()
