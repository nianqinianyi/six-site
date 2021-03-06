"""
Copyright (c) [2019] [sixlab.cn]
[https://github.com/PatrickRoot/six-site] is licensed under the Mulan PSL v1.
You can use this software according to the terms and conditions of the Mulan PSL v1.
You may obtain a copy of Mulan PSL v1 at:
    http://license.coscl.org.cn/MulanPSL
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
PURPOSE.
See the Mulan PSL v1 for more details.
"""
import telegram

from config.db import select_one


def set_token():
    site_config = select_one('''
    select * from site_config
    where config_key = ?
    ''', ('telegram.token',))

    if site_config:
        return telegram.Bot(token=site_config['config_val'])


bot = set_token()


def send_msg(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)


def send_btns(chat_id, text, btns):
    bot.send_message(chat_id=chat_id, text=text)
