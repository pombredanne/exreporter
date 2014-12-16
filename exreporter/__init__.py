# -*- coding: utf-8 -*-

__author__ = 'Vedarth Kulkarni'
__email__ = 'vedarthk@vedarthz.in'
__version__ = '0.1.2'


# set default logging handler
import logging
try:
    from logging import NullHandler
except:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
