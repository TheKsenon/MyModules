from .. import loader, utils
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
import requests

class AIBioMod(loader.Module):
    """AI Bio Module"""
    strings = {'name': 'AIBio'}

    async def client_ready(self, client, db):
        self.client = client

    async def aibiocmd(self, message):
        """Generate AI bio for user."""
        # Начальное сообщение при скачивании модуля
        start_msg = """
        [🎶] Модуль: ИИ-Био

        [😁] ИИ придумает вам описание по вашему промту!

        [🥳] Использование:
        .aibio PROMPT — Замените ПРОМПТ на запрос.

        [🔮] Разработчик:
        @XenonModules / @officialksenon
        """

        await message.edit(start_msg)

        API_KEY_GPT35 = 'ddosxd-api-1jq4e9xbzu2ilgn' 
        headers = {'Authorization': API_KEY_GPT35} 

        prompt = utils.get_args_raw(message)
        if not prompt:
            await message.edit('[🚫] Ошибка: Нет аргументов.')
            return

        data = {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': prompt + "Напиши био. Максимум букв 70, больше 70 не должно быть"}]}

        response = requests.post('https://api.ddosxd.ru/v1/chat', headers=headers, json=data)
        if response.status_code == 200:
            try:
                bio = response.json()['messages'][0]['content']
                await self.client(UpdateProfileRequest(about=bio))
                await message.edit('[🎉] Био успешно изменено!')
            except KeyError:
                await message.edit('[🚫] Ошибка: Не удалось получить био от сервера.')
        else:
            await message.edit(f'[🚫] Ошибка: {response.text}')
