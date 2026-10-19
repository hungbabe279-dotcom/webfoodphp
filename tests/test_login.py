"""
KỊCH BẢN KIỂM THỬ: ĐĂNG NHẬP (LOGIN)
---------------------------------------------
1. Test Case 1: Đăng nhập Admin thành công (hoang / 123) -> Chuyển hướng vào trang Admin.
2. Test Case 2: Đăng nhập Khách hàng thành công (huy / 123) -> Chuyển hướng vào trang chủ.
3. Test Case 3: Đăng nhập thất bại (Sai mật khẩu) -> Giữ nguyên trang đăng nhập.
"""

import time
from selenium.webdriver.common.by import By
from driver_factory import get_driver

BASE_URL = "http://localhost:8080/login/index.php"

def test_login_admin_success():
    print("\n--- BẮT ĐẦU TEST: Đăng nhập Admin thành công (hoang/123) ---")
    driver = get_driver(headless=False)
    try:
        # Bước 1: Mở trang đăng nhập
        driver.get(BASE_URL)
        time.sleep(1) # Dừng 1 giây để bạn kịp quan sát

        # Bước 2: Tìm ô nhập username và nhập 'hoang'
        username_input = driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys("hoang")
        print("-> Đã điền username: hoang")

        # Bước 3: Tìm ô nhập password và nhập '123'
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys("123")
        print("-> Đã điền password: 123")

        # Bước 4: Nhấn nút Login
        login_button = driver.find_element(By.NAME, "submit")
        login_button.click()
        print("-> Đã bấm nút Login, đang đợi chuyển hướng...")
        time.sleep(2)

        # Bước 5: Kiểm tra kết quả (Assert)
        current_url = driver.current_url
        print(f"-> URL hiện tại sau khi đăng nhập: {current_url}")
        
        # Mong đợi URL chứa từ 'admin'
        assert "admin" in current_url.lower(), f"Lỗi: Không chuyển vào trang admin! URL hiện tại là: {current_url}"
        print("✅ TEST CASE 1 THÀNH CÔNG: Đăng nhập quyền Admin chuyển vào trang Admin chính xác!")

    finally:
        driver.quit()


def test_login_wrong_password():
    print("\n--- BẮT ĐẦU TEST: Đăng nhập thất bại khi sai mật khẩu ---")
    driver = get_driver(headless=False)
    try:
        # Bước 1: Mở trang đăng nhập
        driver.get(BASE_URL)
        time.sleep(1)

        # Bước 2: Nhập username đúng nhưng password sai
        driver.find_element(By.NAME, "username").send_keys("hoang")
        driver.find_element(By.NAME, "password").send_keys("sai_mat_khau_123")
        print("-> Đã nhập username: hoang, password: sai_mat_khau_123")

        # Bước 3: Bấm nút Login
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)

        # Bước 4: Kiểm tra kết quả
        current_url = driver.current_url
        print(f"-> URL hiện tại: {current_url}")

        # Mong đợi vẫn ở trang login, không được vào admin
        assert "admin" not in current_url.lower(), "Lỗi: Mật khẩu sai nhưng lại được vào trang admin!"
        assert "login" in current_url.lower(), f"Lỗi: URL không ở trang login! URL hiện tại: {current_url}"
        print("✅ TEST CASE 2 THÀNH CÔNG: Hệ thống chặn đúng khi nhập sai mật khẩu!")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("=" * 60)
    print("CHẠY KIỂM THỬ SELENIUM CHO CHỨC NĂNG ĐĂNG NHẬP")
    print("=" * 60)
    test_login_admin_success()
    test_login_wrong_password()
    print("\n🎉 TẤT CẢ TEST CASES ĐÃ HOÀN TẤT THÀNH CÔNG!")
