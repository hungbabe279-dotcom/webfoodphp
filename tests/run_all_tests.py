"""
MASTER TEST RUNNER - CHẠY TẤT CẢ CÁC BÀI TEST SELENIUM
"""
import sys
import os

# Thêm thư mục tests vào sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from test_login import test_login_admin_success, test_login_wrong_password
from test_search import test_search_product
from test_cart import test_add_to_cart

def run():
    print("=" * 70)
    print("     HỆ THỐNG KIỂM THỬ TỰ ĐỘNG BẰNG SELENIUM (CHROME / EDGE)")
    print("     Dự án: Website Bán Đồ Ăn Trực Tuyến")
    print("=" * 70)

    test_cases = [
        ("TC01 - Đăng nhập quyền Admin thành công (hoang/123)", test_login_admin_success),
        ("TC02 - Đăng nhập thất bại khi nhập sai mật khẩu", test_login_wrong_password),
        ("TC03 - Tìm kiếm sản phẩm theo từ khóa (Kiwi)", test_search_product),
        ("TC04 - Thêm sản phẩm vào giỏ hàng", test_add_to_cart),
    ]

    results = []

    for name, test_func in test_cases:
        try:
            test_func()
            results.append((name, "PASSED ✅"))
        except Exception as e:
            print(f"❌ THẤT BẠI: {e}")
            results.append((name, f"FAILED ❌ ({e})"))

    print("\n" + "=" * 70)
    print("                 BẢNG TỔNG HỢP KẾT QUẢ KIỂM THỬ")
    print("=" * 70)
    for name, status in results:
        print(f" {name:<55} | {status}")
    print("=" * 70)

if __name__ == "__main__":
    run()
