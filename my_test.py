from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Khởi động trình duyệt Chrome
driver = webdriver.Chrome()

# 2. Mở trang đăng nhập
driver.get("http://localhost:8080/login/index.php")

# 3. Tìm ô username và gõ tài khoản "hoang"
username_box = driver.find_element(By.NAME, "username")
username_box.send_keys("hoang")

# 4. Tìm ô password và gõ "123"
password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("123")

# 5. Tìm nút Login và bấm Click
login_btn = driver.find_element(By.NAME, "submit")
login_btn.click()

# Đợi 2 giây để trang load xong
time.sleep(2)

# 6. KIỂM TRA KẾT QUẢ (Assert):
# Vì tài khoản "hoang" là Admin, nên sau khi đăng nhập, URL phải chuyển sang trang /admin/
current_url = driver.current_url
print("URL sau khi đăng nhập:", current_url)

assert "admin" in current_url, "TEST THẤT BẠI: Đăng nhập admin không thành công!"
print("🎉 TEST THÀNH CÔNG: Đã đăng nhập và vào trang Admin thành công!")

# 7. Đóng trình duyệt
driver.quit()
