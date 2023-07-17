from dock_py_selenium.dock.dock import Driver, options, Keys,driver
from selenium import webdriver

dock_instance = Driver(driver)

# Starting the dock instance
# This step is compulsory
dock_instance.start()

# Getting the title of the webpage
dock_instance.getTitle()

# Checking whether an element with name = username is present
dock_instance.checkElement("name", "username")
# Checking the title of the webpage
dock_instance.checkTitle("Dock Selenium")

# Add a webdriver wait time
dock_instance.wait(10)

# Check the window's dimension
dock_instance.dimension("h")
dock_instance.dimension("w")
dock_instance.dimension("hw")


