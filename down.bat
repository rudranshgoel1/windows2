@echo off
certutil -urlcache -split -f "https://getscreen.me/download/getscreen.exe" getscreen.exe
pip install pyautogui --quiet
curl -s -l -o setup.py https://gitlab.com/chamod12/getscrn-win10-github-rdp/-/raw/main/setup.py
curl -s -L -o loop.bat https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.bat
curl -s -L -o chrome.py https://raw.githubusercontent.com/rudranshgoel1/windows2/main/chrome.bat
curl -s -L -o wall.bat https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/wall.bat
curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
netsh advfirewall firewall set rule group="Remote Desktop" new enable=yes
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 1 /f
net user runneradmin TheDisa1a

python -c "import pyautogui as pag; pag.click(896, 64, duration=4)"
start "" "getscreen.exe" 
:LOOP
tasklist | find /i "getscreen.exe" > nul
if %errorlevel% equ 0 (
    echo getscreen found.
    goto END
) else (
    timeout /t 10 /nobreak > nul
    goto LOOP
)
:END
python setup.py
call wall.bat
start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig"
python -c "import pyautogui as pag; pag.click(143, 487, duration=5)"
python -c "import pyautogui as pag; pag.click(155, 554, duration=2)"
python -c "import pyautogui as pag; pag.click(637, 417, duration=2)"
python -c "import pyautogui as pag; pag.click(588, 10, duration=2)"
