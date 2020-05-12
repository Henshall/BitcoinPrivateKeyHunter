#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import env
from addresses import addresses
from BitcoinFinder import BitcoinFinder

finder = BitcoinFinder()
finder.setEnv(env)
finder.setNumTimes(1000)
finder.setAddressList(addresses)
finder.start()