import telebot
import socket
import threading

def scan_port(ip,port):
    f = open('temp.txt','a')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip,port))
        f.write(str(port)+'\n')
        sock.close()
        f.close()
    except:
         pass

bot = telebot.TeleBot("TOKEN", parse_mode=None)
ports = [i for i in range(1,1001)]
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, этот бот создан для поиска открытых портов в ip адресе\n Для поиска используй команду /ip xxx.xxx.xx.xx")

@bot.message_handler(commands=['ip'])
def mode(message):
    ip = (message.text.split())[1]
    for element in ports:
        t = threading.Thread(target=scan_port, kwargs={'ip':ip,'port': element})

        t.start()
    f = open('temp.txt')
    try:
        bot.reply_to(message, f.read())
    except:
        bot.reply_to(message, 'нет открытых портов')
    f.close()
    f = open('temp.txt','w')
    f.close()
bot.polling()
