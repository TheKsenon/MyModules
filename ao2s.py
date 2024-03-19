import os
from .. import loader, utils
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest


def register(cb):
    cb(UserDataMod())

class UserDataMod(loader.Module):
    """Модуль может изменить ваши данные в Telegram"""
    strings = {'name': 'UserData'}
    
    async def biocmd(self, message):
        """Команда .bio изменит ваше био."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit('Нет аргументов.')
        await message.client(UpdateProfileRequest(about=args))
        await message.edit('Био изменено успешно!')
      
