import webbrowser
import time
import keyboard

url = ["twitch.tv/pokimane", "twitch.tv/sykkuno", "twitch.tv/lilypichu", "twitch.tv/ludwig"]

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
c = webbrowser.get('chrome')

time.sleep(28800)
keyboard.press_and_release('ctrl+w')
x = 1
while x <= 3:
    c.open(url[x])
    if x == 3:
        x = x - 3
    else:
        x = x + 1
    time.sleep(86400)
    keyboard.press_and_release('ctrl+w')

