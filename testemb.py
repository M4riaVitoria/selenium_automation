import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
navegador = webdriver.Chrome()

navegador.get("https://sistemas.grupocoutinho.com/")

for i in range(13):
    pyautogui.press("tab")

pyautogui.write("")
pyautogui.press("tab")
pyautogui.write("")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enterrrr")

pyautogui.press("tab")
pyautogui.press("enterrrr")
