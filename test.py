from dock_py_selenium.dock.dock import Driver, options
from selenium import webdriver

driver = webdriver.Chrome(options=options)
dock_instance = Driver(driver)

dock_instance.start()
dock_instance.getTitle()

dock_instance.checkElement("NAME", "username").send_keys("angel1996")
dock_instance.checkElement("NAME", "password").send_keys("123")
dock_instance.checkElement("NAME", "login").click()
dock_instance.checkElement("ID","logout")

