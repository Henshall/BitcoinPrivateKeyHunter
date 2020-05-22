#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import env
from addresses import addresses
from BitcoinFinder import BitcoinFinder
import json

finder = BitcoinFinder()
finder.setEnv(env)
finder.setAddressList(set(addresses))
finder.start()