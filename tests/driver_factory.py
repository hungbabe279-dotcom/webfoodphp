from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(headless=False):
    """
    Khởi tạo WebDriver: Ưu tiên Chrome, nếu không được sẽ dùng Microsoft Edge.
    - headless=False: Trình duyệt sẽ mở cửa sổ trực quan để bạn thấy nó tự động thao tác.
    - headless=True: Trình duyệt chạy ngầm không hiện cửa sổ (nhanh hơn).
    """
    try:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver
    except Exception as e:
        print(f"Không mở được Chrome ({e}), chuyển sang Microsoft Edge...")
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        return driver
