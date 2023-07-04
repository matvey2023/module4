import telebot
token ="5948785044:AAGBGf7nFapa0oRWdfwb0edZo05Ox4cqpWY"
bot=telebot.TeleBot(token)

# def my_func():
#     print("я работаю!")
#
# def my_decorator(func_to_decorated):
#     def decorated_func():
#         print("я начинаю работать")
#         func_to_decorated()
#         print("я отработал")
#     return decorated_func
#
# @my_decorator
# def my_func():
#     print("я работаю!")
# my_func()
#
# my_func=my_decorator(my_func)
# my_func()
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
   welcome_text="""Привет! Я умею рассказывать стихи,знаю много интересных фактов и могу показать фото милых котиков."""
   bot.send_message(message.chat.id, welcome_text)

# @bot.message_handler(commands=["poem"])
# def send_fucts(message):
