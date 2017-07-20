from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login(driver,username,password):
    driver.get("https://www.walmart.com/account/login?tid=0&vid=2&returnUrl=%2Fsignin%3Fredirect%3D%252Faccount")
    try:
        for element in driver.find_elements_by_tag_name('input'):
            if element.get_attribute('data-tl-id') == "signin-email-input":
                element.send_keys(username)
            else:
                element.send_keys(password)
    except Exception as ex:
        print('Something went wrong ',ex)
        pass
    for element in driver.find_elements_by_tag_name('button'):
        if element.get_attribute('data-automation-id') == "signin-submit-btn":
            element.click()
            break

def NavigateFoods(driver,category,subcategory):
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_9Ev-K")))
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-automation-id='NavigationBtn']")))
    # driver.implicitly_wait(4)

    for element in driver.find_elements_by_tag_name('button'):
        if element.get_attribute('data-automation-id') == "NavigationBtn":
            element.click()
            break

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_13KEL._1wnQZ")))
    driver.find_element_by_css_selector("button[data-automation-id='{}']".format(category)).click()
    driver.implicitly_wait(2)
    driver.find_element_by_css_selector("a[data-automation-id='{}']".format(subcategory)).click()

def AddToCart(driver,name,qty):
    # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(name))))
    # WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), '{}')]".format(name))))
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-automation-id='productTile']")))

    el = driver.find_elements_by_xpath('''//*[contains(text(), "{}")]'''.format(name))
    if el:
        try:
            ele = el[0].find_element_by_xpath('..')
            elem = ele.find_element_by_xpath('following-sibling::div')
            eleme = elem.find_element_by_xpath("descendant::button")
            eleme.click()
            driver.implicitly_wait(2)
        except Exception as ex:
            print('Silly exceptions', ex)
            pass
        for i in range(1,qty):
            driver.find_element_by_css_selector("button[data-automation-id='incrementBtn']").click()

def search(driver,term):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-automation-id='searchField']")))
    search = driver.find_element_by_css_selector("input[data-automation-id='searchField']")
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(Keys.DELETE)
    search.send_keys(term)
    search.send_keys(Keys.RETURN)
    search.send_keys(Keys.RETURN)
    

def WalmartShop():
    driver = webdriver.Firefox(executable_path=r'C:\Users\Tanner\Desktop\geckodriver-v0.16.1-win64\geckodriver.exe')
    login(driver,"","")

    NavigateFoods(driver,"ProduceBtn","FreshFruitLink")

    AddToCart(driver,"Bananas, 1 lb (approximately 2 bananas)",4)
    AddToCart(driver,"Fuji Apples, 3 lbs Bag",0)
    AddToCart(driver,"Green Grapes Seedless,  2 lb bag",0)

    NavigateFoods(driver,"ProduceBtn","FreshVegetablesLink")


    AddToCart(driver,"Tomatoes on the Vine, 1 lb",0)
    AddToCart(driver,"Yellow Onions, 1 lb (approximately 1 - 2 onions)",0)

    search(driver,"salad dressing")

    AddToCart(driver,'''Brianna's Asiago Caesar Dressing, 12 fl oz''',0)

    NavigateFoods(driver,"ProduceBtn","SaladGreens&HerbsLink")

    AddToCart(driver,"Marketside Premium Romaine Salad, 9 oz",2)

    NavigateFoods(driver,"MeatBtn","ChickenLink")

    AddToCart(driver,"Tyson Boneless Skinless Fresh Chicken Thighs, 1.5-2.0 lbs.",0)

    NavigateFoods(driver,"Eggs&DairyBtn","MilkLink")

    AddToCart(driver,"Great Value Vitamin D Milk, 1 gal",0)

    search(driver,"greek yogurt")

    AddToCart(driver,"Great Value Blended Whole Milk Plain Greek Yogurt, 32 oz",0)

    search(driver,"cottage cheese")

    AddToCart(driver,"Great Value Small Curd Cottage Cheese, 24 oz",0)

    search(driver,"sara lee bread")

    AddToCart(driver,"Sara Lee 100% Whole Wheat Bakery Bread With Honey, 20 oz",0)

    AddToCart(driver,"Sara Lee Cinnamon with Raisins Bread, 16 oz",0)

    NavigateFoods(driver,"PantryBtn","Rice,Grains&DriedBeansLink")
    AddToCart(driver,"Mahatma Natural Long Grain Rice Brown, 28 oz",0)
    AddToCart(driver,"Great Value Dried Pinto Beans, 32 oz",0)

    NavigateFoods(driver,"PantryBtn","InternationalFoodsLink")
    AddToCart(driver,'Sriracha Hot Chili Sauce, 9 oz',0)
    search(driver,"frozen shrimp cooked")
    AddToCart(driver,"Small Cooked Shrimp: peeled, deveined, tail-off, 1lb",0)
    search(driver,"spagetti noodles")
    AddToCart(driver,"Skinner Long Spaghetti, 12 oz",2)
    search(driver,"whole tomatoes")
    AddToCart(driver,"Great Value Whole Tomatoes, 28 oz",2)
    search(driver,"tuna")
    AddToCart(driver,"Bumble Bee Albacore Solid White In Water 5 oz Tuna, 4 ct",0)

    driver.implicitly_wait(2)



WalmartShop()
