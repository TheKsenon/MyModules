import requests
from .. import loader, utils

# Метаданные модуля
@loader.tds
class AIBioMod(loader.Module):
    """AI Bio Module"""
    strings = {
        "name": "AI Bio",
        "bio": "🎶 Модуль: ИИ-Био

"
               "😁 ИИ придумает вам описание по вашему промту!

"
               "🥳 Использование:
"
               ".aibio PROMPT — Замените ПРОМПТ на запрос.

"
               "🔮 Разработчик:
"
               "@XenonModules / @officialksenon"
    }

    # Команда .aibio
    @loader.unretr_cmd(
        "aibio ((?!
).*)?"
    )
    async def aibio(self, message):
        """Генерация био с помощью ИИ"""
        prompt = utils.get_args_raw(message)
        if not prompt:
            await utils.answer(message, self.strings("bio", message))
            return

        # Отправка запроса на API
        api_key = "ddosxd-api-1jq4e9xbzu2ilgn"
        headers = {"Authorization": api_key}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{prompt} Напиши био. Максимум букв 70, больше 70 не должно быть"}]
        }
        response = requests.post("https://api.ddosxd.ru/v1/chat", headers=headers, json=data)

        # Обработка ответа
        if response.status_code == 200:
            bio = response.json()["choices"][0]["message"]["content"].strip()
            await message.client(UpdateProfileRequest(about=bio))
            await utils.answer(message, f"📝 Новое био: {bio}")
        else:
            await utils.answer(message, f"❌ Ошибка: {response.text}")
