# coding: utf-8

import pytest


pytest_plugins = "xprocess"


def pytest_configure(config):
    def preparefunc(cwd):
        return ('Started', ['dae', 'service', 'serve'])

    xprocess_plugin = config.pluginmanager.getplugin('xprocess')
    xprocess = xprocess_plugin.XProcess(config)
    xprocess.ensure('jagare', preparefunc)


def pytest_unconfigure(config):
    xprocess_plugin = config.pluginmanager.getplugin('xprocess')
    xprocess = xprocess_plugin.XProcess(config)
    info = xprocess.getinfo('jagare')
    if info.pid:
        # info.kill()  # need xprocess 0.8
        import py
        tw = py.io.TerminalWriter()
        xprocess_plugin.do_xkill(info, tw)
