from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Browserni to‘liq ochish
# options.add_argument("--headless")       # Agar brauzer ko‘rinmas bo‘lishini istasangiz

driver = webdriver.Chrome(options=options)

driver.get("https://your-ecommerce-demo-site.com/product/1")

add_btn = driver.find_element(By.ID, "add-to-cart")
add_btn.click()

time.sleep(1)

driver.get("https://your-ecommerce-demo-site.com/cart")

product_name = driver.find_element(By.CLASS_NAME, "product-title").text
assert "Product 1" in product_name

driver.quit()


# Verify order success
success = driver.find_element(By.ID, "success-message").text
assert "Order Successful" in success

driver.quit()
