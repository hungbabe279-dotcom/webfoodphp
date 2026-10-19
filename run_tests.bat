@echo off
chcp 65001 > nul
echo =======================================================
echo    ĐANG KHỞI CHẠY KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM...
echo =======================================================
echo.
py tests/run_all_tests.py
echo.
pause
