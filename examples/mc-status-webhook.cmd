@echo off
setlocal

set "MSW_HOST=127.0.0.1"
set "MSW_PORT=25565"
set "MSW_WEBHOOK_URL=https://..."
set "MSW_THUMBNAIL_URL=https://..."
set "MSW_ONLINE_COLOR=30c030"
set "MSW_OFFLINE_COLOR=ff4040"
set "MSW_STATUS_TITLE=Status"
set "MSW_STATUS_ONLINE_VALUE=Online"
set "MSW_STATUS_OFFLINE_VALUE=Offline"
set "MSW_ADDRESS_TITLE=Address"
set "MSW_ADDRESS_VALUE=example.com"

python mc_status_webhook.py
