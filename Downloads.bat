@echo off
choco install anydesk -y --ignore-checksums --force --no-progress --pre
powershell -Command "Invoke-WebRequest https://gitlab.com/chamod12/anydesk-windows-rdp/-/raw/main/start.bat -OutFile start.bat"
pip install pyautogui --quiet
pip install psutil --quiet
pip install requests --quiet
pip install selenium --quiet
curl -s -L -o timelimit.js https://gitlab.com/chamod12/anydesk-windows-rdp/-/raw/main/timelimit.js
curl -s -L -o time.py https://gitlab.com/chamod12/anydesk-windows-rdp/-/raw/main/timelimit.py
curl -s -L -o chrome.py https://raw.githubusercontent.com/rudranshgoel1/windows2/main/chrome.py
curl -s -L -o aisensy.py https://raw.githubusercontent.com/rudranshgoel1/windows2/main/aisensy.py
curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" > errormsg.txt 2>&1
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" > errormsg.txt 2>&1
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel" /v "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" /t REG_DWORD /d 0 /f
tzutil /s "Sri Lanka Standard Time"
