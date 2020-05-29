#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import env
# from addresses2 import keys
from addressSearchFolder.addresses_test import keys
from app.BitcoinMethodStarter import BitcoinMethodStarter
import json

starter = BitcoinMethodStarter()
starter.setEnv(env)
starter.setAddressList(set(keys))
starter.start()