from decouple import config
from telethon import TelegramClient


api_id = config('API_ID')
api_hash = config('API_HASH')
client = TelegramClient('anon', api_id, api_hash)


async def get_chats():
    # Você pode imprimir todos os diálogos/conversas das quais faz parte:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)


async def get_message_history(chat):
    async for message in client.iter_messages(chat):
        print(message.id, message.text)


async def get_last_message_in_chat(chat):
    # async for message in client.iter_messages(chat, 1):
    async for message in client.iter_messages(chat, min_id=121477):
        print(message.id, message.text)


async def main():
    print(config('APP_NAME'))

    # Obtendo informações sobre você
    me = await client.get_me()
    print(f'Nome: {me.first_name} {me.last_name}')
    print(f'Telefone: +{me.phone}')
    print(f'Nome de Usuário: {me.username}')
    print(f'Id do Usuário: {me.id}')

    # await get_chats()
    await get_message_history('me')
    # await get_last_message_in_chat('me')


with client:
    client.loop.run_until_complete(main())
