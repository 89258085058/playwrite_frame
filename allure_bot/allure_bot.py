import json
import os

import telebot
from matplotlib import pyplot as plt
from telebot import apihelper
from telebot.types import InputMediaPhoto


class CreateAllure:

    def data_alure_report_artifacts(self):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "allure-report/widgets/summary.json")
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def config_file(self):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "notifications/config.json")
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def data_statistic(self):
        return json.loads(self.data_alure_report_artifacts())["statistic"]

    def data_config(self):
        return json.loads(self.config_file())["base"]

    def create_data(self):
        self.failed = self.data_statistic()['failed']
        self.broken = self.data_statistic()['broken']
        self.passed = self.data_statistic()['passed']
        self.skipped = self.data_statistic()['skipped']
        self.unknown = self.data_statistic()['unknown']
        self.total = self.data_statistic()['total']
        self.name = self.data_config()['project']
        self.proxy = self.data_config()['proxy']
        self.token = self.data_config()['token']
        self.chat = self.data_config()['chat']
        self.reportLink = self.data_config()['reportLink']
        self.environment = self.data_config()['environment']

        testValues = [
            {
                'label': "Успешные",
                'value': self.passed,
                'color': '#228B22',
                'explode': 0.0
            },
            {
                'label': "Упавшие",
                'value': self.failed,
                'color': '#FF0000',
                'explode': 0.1
            },
            {
                'label': "Сломанные",
                'value': self.broken,
                'color': '#FFD700',
                'explode': 0.0
            },
            {
                'label': "Пропущенные",
                'value': self.skipped,
                'color': '#C0C0C0',
                'explode': 0.0
            },
            {
                'label': "Неизвестные",
                'value': self.unknown,
                'color': '#c507cd',
                'explode': 0.0
            }
        ]

        labels = [obj["label"] for obj in testValues if obj["value"] > 0]
        values = [obj["value"] for obj in testValues if obj["value"] > 0]
        colors = [obj["color"] for obj in testValues if obj["value"] > 0]
        explode = [obj["explode"] for obj in testValues if obj["value"] > 0]

        fig, ax = plt.subplots(figsize=(8,5))
        fig.set_facecolor('lightgrey')
        plt.title(f'{self.name}\n', fontdict={'fontweight': 600, 'fontsize': 'xx-large'})
        plt.pie(values, colors=colors, explode=explode, shadow=False,
                        autopct='%1.1f%%', startangle=180, textprops={'size': 'large'}, wedgeprops=dict(width=0.4, edgecolor='w'))
        plt.axis('equal')
        plt.legend(labels=labels, loc="lower right", bbox_to_anchor=(0.2, -0.1, 0, 0))
        plt.savefig('allure_bot/allure.png')

    def send_messege(self):
        try:
            self.create_data()
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  parse_mode='HTML',
                                                                  caption=f'<b>Рабочее окружение:</b> {self.environment}'
                                                                          f'\n'
                                                                          f'\n<b>Всего тестов:</b> {self.total}'
                                                                          f'\n<b>Успешных тестов:</b> {self.passed}'
                                                                          f'\n<b>Упавших тестов:</b> {self.failed}'
                                                                          f'\n<b>Неисправных тестов:</b> {self.broken}'
                                                                          f'\n<b>Пропущенных тестов:</b> {self.skipped}'
                                                                          f'\n'
                                                                          f'\n<b>Отчет:</b> {self.reportLink}')])
        except:
            self.create_data()
            apihelper.proxy = {'https': f'{self.proxy}'}
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  parse_mode='HTML',
                                                                  caption=f'<b>Рабочее окружение:</b> {self.environment}'
                                                                          f'\n'
                                                                          f'\n<b>Всего тестов:</b> {self.total}'
                                                                          f'\n<b>Успешных тестов:</b> {self.passed}'
                                                                          f'\n<b>Упавших тестов:</b> {self.failed}'
                                                                          f'\n<b>Неисправных тестов:</b> {self.broken}'
                                                                          f'\n<b>Пропущенных тестов:</b> {self.skipped}'
                                                                          f'\n'
                                                                          f'\n<b>Отчет:</b> {self.reportLink}')])


messege = CreateAllure()
messege.send_messege()