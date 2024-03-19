import os
from .. import loader, utils
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
import requests

API_KEY_GPT35 = 'ddosxd-api-1jq4e9xbzu2ilgn'
headers = {'Authorization': API_KEY_GPT35}

def register(cb):
    cb(UserDataMod())

class UserDataMod(loader.Module):
    """Модуль может изменить ваши данные в Telegram"""
    strings = {'name': 'AI-Bio'}

    async def aibiocmd(self, message):
        """Команда .aibio изменит ваше био, используя ИИ."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit('[🎶] Модуль: ИИ-Био\n\n[😁] ИИ придумает вам описание по вашему промту!\n\n[🥳] Использование:\n.aibio PROMPT — Замените ПРОМПТ на запрос.\n\n[🔮] Разработчик:\n@XenonModules / @officialksenon')
        
        prompt = args + "Напиши био. Максимум букв 70, больше 70 не должно быть"
        data = {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': prompt}]}

        response = requests.post('https://api.ddosxd.ru/v1/chat', headers=headers, json=data)
        if response.status_code == 200:
            bio = response.json().get('generated_text', '').strip()
            if bio:
                await message.client(UpdateProfileRequest(about=bio))
                await message.edit('Био изменено успешно на:\n\n' + bio)
            else:
                await message.edit('ИИ не смог сгенерировать био.')
        else:
            await message.edit('Произошла ошибка при запросе к серверу.')
