@echo off
setlocal

rem Uncomment the variables by removing the 'rem' in front
rem and set the values according to your needs

rem set "MSW_HOST=127.0.0.1"
rem set "MSW_PORT=25565"
rem set "MSW_WEBHOOK_URL=https://..."
rem set "MSW_ONLINE_THUMB_URL=https://..."
rem set "MSW_OFFLINE_THUMB_URL=https://..."
rem set "MSW_ONLINE_COLOR=30c030"
rem set "MSW_OFFLINE_COLOR=ff4040"
rem set "MSW_STATUS_TITLE=Status"
rem set "MSW_STATUS_ONLINE_VALUE=Online"
rem set "MSW_STATUS_OFFLINE_VALUE=Offline"
rem set "MSW_ADDRESS_TITLE=Address"
rem set "MSW_ADDRESS_VALUE=example.com"

mc-status-webhook %*
