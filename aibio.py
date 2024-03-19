import os
import requests
from .. import loader, utils
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest

API_KEY_GPT35 = 'ddosxd-api-1jq4e9xbzu2ilgn'
headers = {'Authorization': API_KEY_GPT35}

def register(cb):
    cb(AiBioMod())

class AiBioMod(loader.Module):
    """[🎶] AI Bio
    
    [😁] ИИ придумает за вас био!
    
    [🐍] Разработчик:
    @XenonModules / @officialksenon
    Код для изменения данных пользователя в Telegram."""
    strings = {'name': 'AiBio'}
    
    async def aibiocmd(self, message):
        """Команда .aibio изменит ваше био."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit('Нет аргументов.')
        await message.edit('[✅] Запрос на био отправлен. Ваш запрос: {}'.format(args))
        
        data = {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': args + "<— Из этого напиши био для аккаунта в мессенджер. Максимум символов(букв) 70 букв. Придумай био, но оно не должен быть больше чем 70 букв. Используй свою фантазию. На каком языке тебе написали, на том и пиши био. Можешь использовать эмоджи."}]}
        response = requests.post('https://api.ddosxd.ru/v1/chat', headers=headers, json=data)
        
        if response.status_code == 200:
            try:
                reply = response.json().get('reply')
                if reply:
                    bio = reply.strip('"')
                    await message.client(UpdateProfileRequest(about=bio))
                    await message.edit('🔮 Био изменилось на "{}"'.format(bio))
                else:
                    await message.edit('❌ ИИ не отправил текст для био.')
            except KeyError as e:
                await message.edit(f'❌ Ошибка при обработке ответа: {e}')
        else:
            await message.edit(f'❌ Ошибка при отправке запроса: {response.status_code}')
