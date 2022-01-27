from selenium.webdriver import Chrome

web = Chrome()
web.get("https://www.shipudong.com")

print(web.title)
