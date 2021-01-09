import webbrowser
import time
import keyboard

url = "twitch.tv/sykkuno"

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
c = webbrowser.get('chrome')

time.sleep(10800)
keyboard.press_and_release('ctrl+w')
c.open(url)