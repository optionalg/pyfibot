# -*- coding: utf-8 -*-

import re

def command_aff(bot, user, channel, args):
    """.aff [Amazon url] - Adds MFC affiliate code to an Amazon item page"""
    asin = re.search('/([A-Z0-9]{10})',args)
    bot.say(channel, ("Affiliated'd! - http://www.amazon.com/dp" + asin.group() + "/?tag=mefightclub-20"))