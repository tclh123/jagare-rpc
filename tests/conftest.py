# coding: utf-8

import os
import sys
import pytest

from jagare_client import Jagare as JagareClient
from jagare.mock import Jagare as JagareMock


# FIXME: python devserver.py

# pytest_plugins = "xprocess"
# APPROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 
# 
# def pytest_configure(config):
#     def preparefunc(cwd):
#         return ('Started', [sys.executable, os.path.join(APPROOT,
#                                                          'devserver.py')])
# 
#     xprocess_plugin = config.pluginmanager.getplugin('xprocess')
#     xprocess = xprocess_plugin.XProcess(config)
#     # jagare: name of the external process,
#     #   used for caching info across test runs.
#     # xprocess.ensure('jagare', preparefunc)  # FIXME: why blocked
# 
# 
# def pytest_unconfigure(config):
#     xprocess_plugin = config.pluginmanager.getplugin('xprocess')
#     xprocess = xprocess_plugin.XProcess(config)
#     info = xprocess.getinfo('jagare')
#     if info.pid:
#         # info.kill()  # need xprocess 0.8
#         import py
#         tw = py.io.TerminalWriter()
#         xprocess_plugin.do_xkill(info, tw)


@pytest.fixture(scope="module",
                params=[JagareClient, JagareMock])
def Jagare(request):
    return request.param
