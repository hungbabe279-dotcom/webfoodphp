@echo off
chcp 65001 > nul
echo Đang tắt các dịch vụ Docker...
docker compose down
echo Đã tắt hoàn tất!
pause
