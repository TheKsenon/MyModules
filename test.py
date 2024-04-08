from telethon import events
import asyncio
from selenium import webdriver
from io import BytesIO

from .. import loader

@loader.tds
class ScreenMod(loader.Module):
    """Модуль для создания скриншота веб-сайта и отправки его в чат.
    
    [📸] Screen

    [🔺] Разработчик: @officialksenon / @XenonModules

    [😚] Скачать модуль:
    [‼️] .dlm https://raw.githubusercontent.com/TheKsenon/Modules/main/screen.py
"""

    strings = {"name": "Screen"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.ratelimit
    async def screencmd(self, message):
        """.screen <url> - сделать скриншот указанного веб-сайта и отправить его в чат."""
        if not message.text[0].isalpha():
            return
        url = message.text.split(" ", 1)
        if len(url) == 1:
            await message.edit("Укажите URL веб-сайта.")
            return
        url = url[1]

        await message.edit("Создание скриншота...")

        driver = webdriver.Chrome()
        driver.get(url)
        await asyncio.sleep(5)  # Даем странице время для загрузки

        screenshot = driver.get_screenshot_as_png()
        driver.quit()

        await message.client.send_file(message.to_id, file=BytesIO(screenshot), caption=f"Скриншот веб-сайта: {url}")

        await message.delete()
