from telethon.errors import ChatAdminRequiredError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from .. import loader

@loader.tds
class DeleteMessagesMod(loader.Module):
    """Модуль удаляет все сообщения от указанного пользователя.
    
    [💀] Пример: .deleteall @username
    """

    strings = {"name": "DeleteMessages"}

    async def deleteallcmd(self, message):
        """Удалить все сообщения от указанного пользователя."""

        if len(message.mentions) == 0:
            return await message.edit("[DeleteMessages] Укажите пользователя в формате: .deleteall @username")

        user = message.mentions[0]

        try:
            # Проверяем наличие прав администратора
            reply = await message.client(GetParticipantRequest(message.chat_id, user.id))
            if isinstance(reply.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
                count = 0
                async for msg in message.client.iter_messages(message.to_id, from_user=user.id):
                    await message.client.delete_messages(message.to_id, msg)
                    count += 1

                await message.edit(f"[✅] Удалено {count} сообщений от пользователя {user.first_name if user.first_name else user.username}")
            else:
                await message.edit("[🚫] У вас нет прав чтобы удалять сообщения. Причина: Нет прав администратора")
        
        except ChatAdminRequiredError:
            await message.edit("[🚫] У вас нет прав чтобы удалять сообщения. Причина: Нет прав администратора")
