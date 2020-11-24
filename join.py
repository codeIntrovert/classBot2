from info import *
from selenium import webdriver
import time


def joinEnglish():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(physics)
    time.sleep(60) #seconds
    zoomJoin()
    time.sleep(1800)
    driver.quit()

def joinPhysics():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(physics)
    time.sleep(60) #seconds
    #zoomJoin()
    time.sleep(1800)
    driver.quit()

def joinChem():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(chemistry)
    time.sleep(60) #seconds
    #zoomJoin()
    time.sleep(1800)
    driver.quit()

def joinMaths():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(maths)
    time.sleep(60) #seconds
    #zoomJoin()
    time.sleep(1800)
    driver.quit()

def joinBio():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(biology)
    time.sleep(60) #seconds
    #zoomJoin()
    time.sleep(1800)
    driver.quit()

def dummy():
    driver = webdriver.Chrome('D:\\SERVER\\chromedriver.exe')
    driver.get(dummy)
    time.sleep(60) #seconds
    #zoomJoin()
    time.sleep(1800)
    driver.quit()










def zoomJoin():
    print("inside zoom")