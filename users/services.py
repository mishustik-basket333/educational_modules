import os

from django.conf import settings
from django.core.mail import send_mail
from telebot import TeleBot


def welcome_send_telegram(chat_telegram_id=None):
    """ Отправка сообщения при регистрации в telegram """
    bot = TeleBot(os.getenv('API_TELEGRAM'))
    message = 'Привет, поздравляем тебя с регистрацией на нашем сайте!!!'
    if chat_telegram_id:
        bot.send_message(chat_telegram_id, message)


def welcome_send_mail(email=None):
    """ Отправка сообщения при регистрации на email"""
    if email:
        send_mail(
            'Регистрация',
            "Поздравляем с регистрацией",
            settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
