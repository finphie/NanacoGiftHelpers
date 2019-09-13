@echo off
cd /d %~dp0
chcp 65001 > nul

rem PowerShellを利用して、クリップボードからギフトIDを取得する。
for /f "usebackq delims=" %%i in (`powershell -ExecutionPolicy Bypass -File GetGiftId.ps1`) do set gifts=%%i

rem ギフトIDが見つからなかった場合は終了する。
if "%gifts%" == "" (
    echo ギフトIDが見つかりませんでした。
    goto END
)

echo ギフトID
echo %gifts%

rem nanaco番号入力
if "%1" == "" (
    for /f "usebackq" %%i in (`powershell -ExecutionPolicy Bypass -File ReadHost.ps1 nanaco番号`) do set number=%%i
) else (
    set number=%1
)

rem パスワード入力
if "%2" == "" (
    for /f "usebackq" %%i in (`powershell -ExecutionPolicy Bypass -File ReadHost.ps1 パスワード`) do set password=%%i
) else (
    set password=%2
)

rem Pythonを利用して、ギフトIDの自動入力処理を実行する。
python nanaco.py %number% %password% %gifts%

:END
cmd /k