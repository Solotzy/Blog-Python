#!/usr/bin/env python3
# -*- coding: utf-8 -*-


################################################################################
#
# Copyright (c) 2016 Jurassic.com, Inc. All Rights Reserved
#
################################################################################
"""
This module provide configure file management service in i18n environment.

Authors: tianzeyu(tianzeyu@jurassic.com.cn)
Date:    2016/10/20 13:23:06
"""

import orm
import asyncio
import sys
import models
#from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = models.User(name='Test5', email='test5@example.com', passwd='123456789032', image='about:blank')
    print(u)
    await u.save()
    print('tested ok...')

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)