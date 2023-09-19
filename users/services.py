import os

from django.conf import settings
from django.core.mail import send_mail
from telebot import TeleBot
from telebot.apihelper import ApiTelegramException


def welcome_send_telegram(chat_telegram_id=None):
    """ Отправка сообщения при регистрации в telegram """
    bot = TeleBot(os.getenv('API_TELEGRAM'))
    message = 'Привет, поздравляем тебя с регистрацией на нашем сайте!!!'
    if chat_telegram_id:
        try:
            bot.send_message(chat_telegram_id, message)
        except ApiTelegramException as e:
            print(f'Ошибка отправки сообщения в telegram {chat_telegram_id}:'
                  f'{e}')


def welcome_send_mail(email=None):
    """ Отправка сообщения при регистрации на email"""
    if email:
        try:
            send_mail(
                'Регистрация',
                "Поздравляем с регистрацией",
                settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
        except Exception as e:
            print(f'Ошибка отправки сообщения на email address {email}:'
                  f'{e}')
