# import os
# from datetime import datetime
# from celery import shared_task
# from telebot import TeleBot
#
#
# @shared_task
# def get_list_habits():
#     """ Получение списка привычек"""
#
#     list_habits = Habit.objects.all()
#
#     for habit in list_habits:
#
#         if habit.time == datetime.now():
#             send_telegram(habit.id)
#
#
# def send_telegram(id_habit):
#     """ Отправка сообщения"""
#
#     habit = Habit.objects.get(pk=id_habit)
#
#     bot = TeleBot(os.getenv('API_TELEGRAM'))
#
#     message = f'Привет, тебе нужно сделать {habit.action} в {habit.place}'
#
#     bot.send_message(habit.user.chat_telegram_id, message)
