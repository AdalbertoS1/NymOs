import telepot


TOKEN = "5065076505:AAGraKeWqHa6dsWge7-F-wvBphZ5leUzqMM"
Bot = telepot.Bot(TOKEN)


def MSG(msg):
    # Debug - Dados do usuario
    try:
        chatID = msg['chat']['id']
        user = msg['chat']['first_name']
        text = msg['text'].lower()
        idMsg = msg['message_id']
    except:
        pass

    # Comandos - Telegram
    send_text = Bot.sendMessage
    edit_text = Bot.editMessageText
    
    # Comandos "Principais"
    if text == '/start':
        send_text(chatID, 'Seja bem-vindo {}, sou o Nymos!'.format(user), reply_to_message_id=idMsg)

    # Comandos 'send'
    text_oie = ['oi', 'ola', 'oie', 'ei']
    if text in text_oie:
        send_text(chatID, 'Olá {}!'.format(user))

    print('''
Nome: {}
chat ID: {}
IdMSG: {}
MSG: "{}"'''.format(user, chatID, idMsg, text))
    
a = Bot.message_loop({'chat': MSG,       
                       })



print('Nym-Os iniciado...')


while True:
    pass
