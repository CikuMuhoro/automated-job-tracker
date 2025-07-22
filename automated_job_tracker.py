import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

MyJobMag = "https://www.myjobmag.co.ke/jobs-by-field/information-technology"
Arcdev = "https://arc.dev/remote-jobs" 
PythonJobBoard = "https://www.python.org/jobs/"
Remotiveio  = "https://remotive.com/remote-jobs/software-dev"

driver.get("https://duckduckgo.com/")

# wait for search bar and type 
search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q")))
# TYPE IN THE SERCH BAR AND
search_box.send_keys(MyJobMag + Keys.ENTER)
time.sleep(5)
#scroll to load more result
#find all result container
#Extract title link and snipet from the conainers
#close the driver

driver.get(Arcdev)

# wait for search bar and type 
# TYPE IN THE SERCH BAR AND 
#scroll to load more result
#find all result container
#Extract title link and snipet from the conainers
#close the driver

driver.get(PythonJobBoard)

# wait for search bar and type 
# TYPE IN THE SERCH BAR AND 
#scroll to load more result
#find all result container
#Extract title link and snipet from the conainers
#close the driver

driver.get(Remotiveio)

# wait for search bar and type 
# TYPE IN THE SERCH BAR AND 
#scroll to load more result
#find all result container
#Extract title link and snipet from the conainers
#close the driver