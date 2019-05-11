from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import urllib3
import selenium

options = webdriver.ChromeOptions()  
options.binary_location = '/usr/bin/google-chrome-stable'
options.headless = True
driver = webdriver.Chrome(chrome_options=options, executable_path='/opt/google/drivers/chromedriver.exe')
driver.get('http://itispw00051.srv.sydney.edu.au:8080/') 
URL = "http://itispw00051.srv.sydney.edu.au:8080/"
#URL = "http://www.google.com.au/"


def generate_bot():
    bot_base = open("base.txt", "a+")
    data = bot_base.readlines()
    data2 = [x.strip("\n") for x in data]
    ID = str(random.randint(1,999))
    ID = ID.zfill(3)
    while (ID in data2):
        ID = str(random.randint(1,999))
        ID = ID.zfill(3)
    bot_base.write(ID + "\n")
    bot_base.close()
    return ID

def home_page():
    driver.get(URL)

    print("Attempting to access Home Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("HOME")
    webdev.click()
    print("--- Accessed Home Page ---")
    print("Current URL: {}".format(driver.current_url))
    return


def about_page():
    driver.get(URL)

    print("Attempting to access About Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("ABOUT")
    webdev.click()
    print("--- Accessed About Page ---")
    print("Current URL: {}".format(driver.current_url))
    return

def help_page():
    driver.get(URL)
    print("Attempting to access Help Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("HELP")
    webdev.click()
    print("--- Accessed Message Page ---")
    print("Current URL: {}".format(driver.current_url))
    return

def message_page():
    driver.get(URL)
    print("Attempting to access Message Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("MESSAGE_PAGE")
    webdev.click()
    print("--- Accessed Message Page ---")
    print("Current URL: {}".format(driver.current_url))
    return

def login_page():
    driver.get(URL)

    print("Attempting to access Login Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("LOGIN_PAGE")
    webdev.click()
    print("--- Accessed Login Page ---")
    print("Current URL: {}".format(driver.current_url))
    return

def signup_page():
    driver.get(URL)

    print("Attempting to access Register Page...")
    time.sleep(1)
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    webdev = driver.find_element_by_id("SIGNUP_PAGE")
    webdev.click()
    print("--- Accessed Register Page ---")
    print("Current URL: {}".format(driver.current_url))
    return

def test_links():
    driver.get(URL)
    print("Current URL: {}".format(driver.current_url))
    print("Attempting to navigate all content links...")

    #HTML
    time.sleep(1)
    home_page()

    print("Clicking All HTML links...")
    print("1. Clicking Intoduction of HTML links")
    driver.find_element_by_id("HTML")
    time.sleep(1)
    driver.find_element_by_id("IntroductionHTML").click()
    print("--- Accessed Intoduction of HTML via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("2. Clicking Basis of HTML links")
    time.sleep(1)
    driver.find_element_by_id("HTML")
    time.sleep(1)
    driver.find_element_by_id("BasisHTML").click()
    print("--- Accessed Basis of HTML via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("3. Clicking Advanced of HTML links")
    time.sleep(1)
    driver.find_element_by_id("HTML")
    time.sleep(1)
    driver.find_element_by_id("AdvancedHTML").click()
    print("--- Accessed Advanced of HTML via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    print("Going back to homepage...")
    home_page()
    print("--- All HTML clicked! ---")

    #css

    print("Clicking All CSS links...")
    print("1. Clicking Intoduction of CSS links")
    driver.find_element_by_id("CSS")
    time.sleep(1)
    driver.find_element_by_id("IntroductionCSS").click()
    print("--- Accessed Intoduction of CSS via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("2. Clicking Syntax of CSS links")
    time.sleep(1)
    driver.find_element_by_id("CSS")
    time.sleep(1)
    driver.find_element_by_id("SyntaxCSS").click()
    print("--- Accessed Syntax of CSS via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("3. Clicking Colours of CSS links")
    time.sleep(1)
    driver.find_element_by_id("CSS")
    time.sleep(1)
    driver.find_element_by_id("ColoursCSS").click()
    print("--- Accessed Colours of CSS via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    print("Going back to homepage...")
    home_page()
    print("--- All CSS clicked! ---")

    #Javascript

    print("Clicking All JavaScript links...")
    print("1. Clicking Intoduction of JavaScript links")
    driver.find_element_by_id("JavaScript")
    time.sleep(1)
    driver.find_element_by_id("IntroductionJava").click()
    print("--- Accessed Intoduction of JavaScript via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("2. Clicking Syntax of JavaScript links")
    time.sleep(1)
    driver.find_element_by_id("JavaScript")
    time.sleep(1)
    driver.find_element_by_id("SyntaxJava").click()
    print("--- Accessed Syntax of JavaScript via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("3. Clicking Colours of JavaScript links")
    time.sleep(1)
    driver.find_element_by_id("JavaScript")
    time.sleep(1)
    driver.find_element_by_id("ColoursJava").click()
    print("--- Accessed Variables of JavaScript via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    print("Going back to homepage...")
    home_page()
    print("--- All JavaScript clicked! ---")

    #Web server

    print("Clicking All WebServer links...")
    print("1. Clicking PHP of WebServer links")
    driver.find_element_by_id("WebServer")
    time.sleep(1)
    driver.find_element_by_id("PHP").click()
    print("--- Accessed HPH of WebServer via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("2. Clicking SQL of WebServer links")
    time.sleep(1)
    driver.find_element_by_id("WebServer")
    time.sleep(1)
    driver.find_element_by_id("SQL").click()
    print("--- Accessed SQL of WebServer via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)

    print("3. Clicking Bottle of WebServer links")
    time.sleep(1)
    driver.find_element_by_id("WebServer")
    time.sleep(1)
    driver.find_element_by_id("Bottle").click()
    print("--- Accessed Bottle of WebServer via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    print("Going back to homepage...")
    home_page()
    print("--- All WebServer clicked! ---")

    #References
    print("Clicking All References links...")
    print("1. Clicking HTML of References links")
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("HTMLReferences").click()
    print("--- Accessed HTML of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()

    print("2. Clicking CSS of References links")
    time.sleep(1)
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("CSSReferences").click()
    print("--- Accessed CSS of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()

    print("3. Clicking JavaScript of References links")
    time.sleep(1)
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("JavaScriptReferences").click()
    print("--- Accessed JavaScript of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()

    print("4. Clicking PHP of References links")
    time.sleep(1)
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("PHPReferences").click()
    print("--- Accessed PHP of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()

    print("5. Clicking SQL of References links")
    time.sleep(1)
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("SQLReferences").click()
    print("--- Accessed SQL of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()

    print("6. Clicking Bottle of References links")
    time.sleep(1)
    driver.find_element_by_id("References")
    time.sleep(1)
    driver.find_element_by_id("BottleReferences").click()
    print("--- Accessed Bottle of References via link ---")
    print("Current URL: {}".format(driver.current_url))
    time.sleep(1)
    driver.back()
    print("Going back to homepage...")
    home_page()
    print("--- All References clicked! ---")

    #ABOUT
    time.sleep(1)
    driver.about_page()
    time.sleep(1)
    print("Going back to homepage...")
    home_page()

    #help_page
    time.sleep(1)
    driver.help_page()
    time.sleep(1)
    print("Going back to homepage...")
    home_page()

    #log in
    time.sleep(1)
    driver.login_page()
    time.sleep(1)
    print("Going back to homepage...")
    home_page()

    #sign up
    time.sleep(1)
    driver.signup_page()
    time.sleep(1)
    print("Going back to homepage...")
    home_page()

def main():
    # driver.get(URL)
    # print("Current URL: {}".format(driver.current_url))
    # driver.find_element_by_id("LOGIN_PAGE").click()
    # print("Current URL: {}".format(driver.current_url))
#    print("Hello")
#   Testcases
    #value = random.randint(1,x)
    test_links()

    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
