from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r"C:/Programs/Tor Browser/Browser/firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
driver.profile.set_preference('network.proxy.type', 1)
driver.profile.set_preference('network.proxy.socks', '127.0.0.1')
driver.profile.set_preference('network.proxy.socks_port', 9051)
driver.get("http://stackoverflow.com")