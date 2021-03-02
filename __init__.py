# Copyright (c) 2020 Romain Thiebaut / wildchron
# The CustomZHeightSupportPlugin is released under the terms of the AGPLv3 or higher.

from . import CustomZHeightSupportPlugin


def getMetaData():
    return {}

def register(app):
    return {"extension": CustomZHeightSupportPlugin.CustomZHeightSupportPlugin()}
