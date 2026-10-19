"""
KỊCH BẢN KIỂM THỬ: TÌM KIẾM SẢN PHẨM (SEARCH)
---------------------------------------------
1. Test Case: Nhập từ khóa 'Kiwi' vào thanh tìm kiếm ở trang chủ.
2. Nhấn nút 'Tìm'.
3. Kiểm tra xem trang kết quả (result.php) có hiển thị sản phẩm chứa chữ 'Kiwi' hay không.
"""

import time
from selenium.webdriver.common.by import By
from driver_factory import get_driver

HOME_URL = "http://localhost:8080/index.php"

def test_search_product():
    print("\n--- BẮT ĐẦU TEST: Tìm kiếm sản phẩm với từ khóa 'Kiwi' ---")
    driver = get_driver(headless=False)
    try:
        # Bước 1: Mở trang chủ website
        driver.get(HOME_URL)
        time.sleep(1)

        # Bước 2: Tìm ô input keyword và gõ từ 'Kiwi'
        search_box = driver.find_element(By.NAME, "keyword")
        search_box.clear()
        search_box.send_keys("Kiwi")
        print("-> Đã nhập từ khóa 'Kiwi' vào ô tìm kiếm")

        # Bước 3: Tìm nút Tìm (button có class search-btn) và click
        search_btn = driver.find_element(By.CLASS_NAME, "search-btn")
        search_btn.click()
        print("-> Đã bấm nút Tìm kiếm, đang chờ kết quả...")
        time.sleep(2)

        # Bước 4: Kiểm tra kết quả trả về
        current_url = driver.current_url
        print(f"-> URL hiện tại: {current_url}")
        assert "result.php" in current_url, f"Lỗi: Không chuyển đến trang result.php! URL là: {current_url}"

        # Kiểm tra xem trên trang có tên sản phẩm 'Kiwi' hay không
        page_content = driver.page_source
        assert "Kiwi" in page_content, "Lỗi: Không tìm thấy sản phẩm Kiwi trong danh sách kết quả!"
        print("✅ TEST CASE THÀNH CÔNG: Tìm kiếm sản phẩm hoạt động chính xác, đã tìm thấy sản phẩm 'Kiwi'!")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("=" * 60)
    print("CHẠY KIỂM THỬ SELENIUM CHO CHỨC NĂNG TÌM KIẾM")
    print("=" * 60)
    test_search_product()
