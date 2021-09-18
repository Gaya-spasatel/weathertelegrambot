import telebot
from weather_response import parse_weather
from weather_response import get_weather
from weather_response import parse_weather_codes
from weather_response import BadRequestException
from secret import TELEGRAM_KEY
import data_validator

bot = telebot.TeleBot(TELEGRAM_KEY)
weather_codes = parse_weather_codes('./files/wwoConditionCodes.txt')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши имя города на английском, погоду в котором ты хочешь узнать "
                                               "сейчас")
    elif data_validator.find_city(message.text) != "":
        try:
            bot.send_message(message.from_user.id, parse_weather(get_weather(data_validator.find_city(message.text)), weather_codes))
        except BadRequestException:
            bot.send_message(message.from_user.id, "Некорректный запрос")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
