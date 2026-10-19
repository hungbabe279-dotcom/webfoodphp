"""
KỊCH BẢN KIỂM THỬ: THÊM SẢN PHẨM VÀO GIỎ HÀNG (ADD TO CART)
-----------------------------------------------------------
1. Mở trang chủ website.
2. Tìm nút 'Thêm vào giỏ' của sản phẩm đầu tiên và click.
3. Chuyển đến trang giỏ hàng (cart.php).
4. Kiểm tra xem giỏ hàng có hiển thị dòng sản phẩm đã thêm hay không.
"""

import time
from selenium.webdriver.common.by import By
from driver_factory import get_driver

HOME_URL = "http://localhost:8080/index.php"
CART_URL = "http://localhost:8080/cart.php?type_id=1"

def test_add_to_cart():
    print("\n--- BẮT ĐẦU TEST: Thêm sản phẩm vào giỏ hàng ---")
    driver = get_driver(headless=False)
    try:
        # Bước 1: Mở trang chủ
        driver.get(HOME_URL)
        time.sleep(2)

        # Bước 2: Tìm nút "Thêm vào giỏ" đầu tiên
        add_to_cart_btn = driver.find_element(By.CLASS_NAME, "add-to-cart-btn")
        print("-> Đã tìm thấy nút 'Thêm vào giỏ'")
        
        # Cuộn chuột và click bằng Javascript (để không bị vướng hiệu ứng hover của carousel)
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", add_to_cart_btn)
        print("-> Đã click nút 'Thêm vào giỏ'")
        time.sleep(2)

        # Bước 3: Vào trang giỏ hàng
        driver.get(CART_URL)
        time.sleep(2)

        # Bước 4: Kiểm tra xem trong giỏ hàng có hàng mục nào (dòng .cart_item) không
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        print(f"-> Số lượng sản phẩm tìm thấy trong bảng giỏ hàng: {len(cart_items)}")
        
        assert len(cart_items) > 0, "Lỗi: Không tìm thấy sản phẩm nào trong giỏ hàng!"
        print("✅ TEST CASE THÀNH CÔNG: Đã thêm sản phẩm vào giỏ hàng thành công!")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("=" * 60)
    print("CHẠY KIỂM THỬ SELENIUM CHO CHỨC NĂNG GIỎ HÀNG")
    print("=" * 60)
    test_add_to_cart()
