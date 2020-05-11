#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import env
from addresses import addresses
from BitcoinStarter import BitcoinStarter

starter = BitcoinStarter()
starter.setEnv(env)
starter.setAddressList(addresses)
starter.start()