#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import telebot

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Cli script for send message to telegram.')

    parser.add_argument('-m', '--message', dest='message', required=True,
                        help='message we want to send')
    parser.add_argument('-t', '--token', dest='bot_token', required=True,
                        help='telegram bot token geted from botfather')
    parser.add_argument('-d', '--destanation', dest='destanation',
                        required=True,
                        help='message destanation (channel or user)')
    args = parser.parse_args()

    bot = telebot.TeleBot(args.bot_token)

    bot.send_message(args.destanation, args.message)
