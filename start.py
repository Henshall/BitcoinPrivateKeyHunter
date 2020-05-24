#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import env
from addresses import addresses
from app.BitcoinMethodStarter import BitcoinMethodStarter
import json

starter = BitcoinMethodStarter()
starter.setEnv(env)
starter.setAddressList(set(addresses))
starter.start()