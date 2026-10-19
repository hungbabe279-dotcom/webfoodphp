@echo off
chcp 65001 > nul
echo =======================================================
echo   Đang khởi động hệ thống Web Bán Đồ Ăn (Docker)...
echo =======================================================
echo.
docker compose up -d --build
if %errorlevel% neq 0 (
    echo.
    echo [LỖI] Không thể chạy Docker. Vui lòng đảm bảo bạn đã mở Docker Desktop!
    echo.
) else (
    echo.
    echo =======================================================
    echo   Đã khởi động thành công!
    echo   - Trang chủ Web:          http://localhost:8080
    echo   - phpMyAdmin (Quản lý DB): http://localhost:8081
    echo =======================================================
)
echo.
pause
