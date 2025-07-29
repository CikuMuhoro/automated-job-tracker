import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Jobboard:
    def __init__(self,site,title,requirements,dateposted):
        self.site = site
        self.title = title
        self.requirements = requirements
        self.dateposted = dateposted
                
        
    #start your browser and type in your search
    def start_browser(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get =("https://duckduckgo.com/")
        self.search_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        
    
    #close browser
    def close_browser(self):
        self.driver.quit()
        
    #open serach boards and search for python jobs
    def job_board_search(self):
        self.boards = ["myjobmag","arcdev","pythonorg","remotive"]
        
        for board in self.boards:
            #search for job board
            self.search_box.send_keys("board" + Keys.ENTER)
            time.sleep(5)
            
            #open the first  and open
            first_result = self.driver.find_element(By.CSS_SELECTOR, 'a')
            
            #
            
            
            
           
        
    