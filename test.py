from dock_py_selenium.dock.dock import Driver, options
from selenium import webdriver

driver = webdriver.Chrome(options=options)
dock_instance = Driver(driver)


dock_instance.start()
dock_instance.getTitle()

dock_instance.checkElement("name", "username").send_keys("angel1996")
dock_instance.checkElement("name", "password").send_keys("123")
dock_instance.checkElement("name", "login").click()
dock_instance.checkTitle("Kabeli Kitchen")

cName = dock_instance.checkElement("id","customerName")
cName.send_keys("Bishal Shrestha")
dock_instance.checkElement("id","customerNumber").send_keys("9746959090")
dock_instance.checkElement("id","customerLocation").send_keys("Itahari")
dock_instance.checkElement("id","deliveryCharge").send_keys("40")

dock_instance.checkElement("id","gBill").click()

try:
    billName = dock_instance.checkElement("xpath","/html/body/div[1]/div[2]/div/div/div[1]/p[2]/span")
    if billName.text == cName.text:
        print("Bill is prepared.")
    else:
        print("Some error occured.")
except:
    print("No bill prepared.")


