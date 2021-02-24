import time
import os
import re
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

#options.binary_location = 'C:\\Program Files (x86)\\Microsoft\\EdgeApplication\\msedge.exe'
driver = Edge(executable_path = 'D:\Programming\Cynthia\Files\edgedriver_win64\msedgedriver.exe')
driver.maximize_window()
driver.get("https://www.google.com")

def a():
    x = input('Enter the command:')

    if 'scroll' in x:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    elif 'kill' in x:
        exit()

    elif 'search' in x:
        domain = input('What do you want to search?:')
        url = 'https://www.google.com/search?q=' + domain
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)

    elif 'back' in x:
        driver.navigate().back();

    elif 'forward' in x:
        driver.navigate().forward();
        
    elif 'close' in x:
        driver.close()
        
    else:
        print('Input again')


while True:
    a()
