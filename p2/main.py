from concurrent.futures import thread
import telebot
import threading

global threads

bot = telebot.TeleBot('5758695644:AAHPNj1KMxFbQba4AKRAd0qubLq7coPXoD8')
threads = list()

@bot.message_handler(content_types=['text'])
def start(message):
    print(message.text, message.from_user.first_name)
    
    if message.text == "s":
        bot.send_message(message.from_user.id, "Reg ur code")
        thread_name = message.from_user.id
        t1 = threading.Thread(target=bot.register_next_step_handler, args=(message, send_ms), name=thread_name)
        print("Creating", message.from_user.first_name, t1.name, "thread")
        threads.append(t1)
        t1.start()

def send_ms(message):
    u_code = message.text
    
    bot.send_message(message.from_user.id, "still " + u_code)
    bot.register_next_step_handler(message, send_ms2)

def send_ms2(message):
    for th in threads:
        print(th)
        if str(message.from_user.id) == str(th.name):
            print(th.name, " thread is closing")
            th.join()
    
    bot.send_message(message.from_user.id, "?")

    

if "__main__" == __name__:
    
    bot.polling(none_stop=True, interval=0)
    
