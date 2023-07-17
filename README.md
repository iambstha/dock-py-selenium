# DOCK SELENIUM

## Python only

This is a startup directory to write the selenium scripts in python along with some customization.

### Steps.
1. `pip install dock-py-selenium`
2. Create a `test.py` file in your root directory and write your test scripts.
3. Always bind any selenium script with the created instance.


## Features

1. Setting a custom wait time for the webdriver `test_instance.wait(5)`
2. Settting the number of times a test should be performed `test_instance.rerun(3, lambda: run())`
3. Getting the title of the page `test_instance.getTitle()`
4. Checking whether the button or input type submit is clickable `test_instance.checkClick("button")` or `test_instance.checkClick("input")`
5. Checking the presence of an element in a webpage `test_instance.checkElement("CLASS_NAME","container")`


<mark> Note that, this project is still experimental and hence does not support the full render wait time for any test actions. </mark>


### Example 
```
    from dock_py_selenium.dock.dock import Driver, options, Keys
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
            dock_instance.checkElement("xpath","/html/body/div[1]/div[2]/div/div/div[2]/button[1]").click()
            dock_instance.send_keys(Keys.ENTER)
        else:
            print("Some error occured.")
    except:
        print("No bill prepared.")

```