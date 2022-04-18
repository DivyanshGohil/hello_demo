from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.irctc.com/")
print("Name : ",driver.name)
print("Application title is : ",driver.title)
print("Application url is : ",driver.current_url)
print("current_window_handle : ",driver.current_window_handle)
print("application_cache : ",driver.application_cache)
print("file_detector : ",driver.file_detector)
print("desired_capabilities : ",driver.desired_capabilities)
print("log_types : ",driver.log_types)
print("Mobile : ",driver.mobile)
print(" ")