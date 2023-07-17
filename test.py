from dock_py_selenium.dock.dock import Driver, options, Keys
from selenium import webdriver

driver = webdriver.Chrome(options=options)
dock_instance = Driver(driver)

# Starting the dock instance
# This step is compulsory
dock_instance.start()

# Getting the title of the webpage
dock_instance.getTitle()

# Checking whether an element with name = username is present
dock_instance.checkElement("name", "username")

# Checking whether an element with name = fname is present & sending "John" as input
dock_instance.checkElement("name", "fname").send_keys("John")

# Checking whether an element with name = login is present & then clicking the element 
dock_instance.checkElement("name", "login").click()

# Checking the title of the webpage
dock_instance.checkTitle("Dock Selenium")

# Add a webdriver wait time
dock_instance.wait(10)



