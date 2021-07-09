import telebot
import socket
import threading
a = []
def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        a.append(port)
        sock.close()
    except:
         pass

bot = telebot.TeleBot("TOKEN", parse_mode=None)
ports = [i for i in range(1,1001)]
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, этот бот создан для поиска открытых портов\nДля поиска используй команду /ip xxx.xxx.xx.xx")

@bot.message_handler(commands=['ip'])
def mode(message):
    ip = '178.214.255.29'
    try:
        ip = (message.text.split())[1]
    except:
        bot.reply_to(message, 'Возникла ошибка, попробуй еще раз!')
        pass
    for element in ports:
        t = threading.Thread(target=scan_port, kwargs={'ip':ip,'port': element})

        t.start()

    try:
        if len(a)!=0:
            bot.reply_to(message,'Открытые порты: '+str(a))
            a.clear()
        else:
            bot.reply_to(message, 'Нет открытых портов')
    except:
        bot.reply_to(message, 'Возникла ошибка, попробуй еще раз!')

bot.polling()
