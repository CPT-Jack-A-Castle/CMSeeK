#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2019 Tuhinshubhra

# Concrete5 CMS version detection
# Rev 1

import cmseekdb.basic as cmseek
import re

def start(ga_content):
    regex = re.findall(r'concrete5 - (.*)', ga_content)
    if regex != []:
        version = regex[0]
        cmseek.success('Concrete5 CMS version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
