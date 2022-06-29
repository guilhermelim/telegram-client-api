async def get_dialogs():
    return { "dialogs": [
                          { "title": "chat 1", "id": 1 },
                          { "title": "chat 2", "id": 2 },
                          { "title": "chat 3", "id": 3 }
                        ]
           }

def connect():
    try:
        print("Fazendo login em sua conta do telegram!")
        print("Login realizado com sucesso!")
    except OSError:
        print('Failed to connect')
