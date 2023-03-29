#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration """

    ## Azure Bot Service ##

    PORT = 8000
    APP_ID = os.environ.get("APP_ID", "")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "")
    
    ## Luis Service ##
    LUIS_APP_ID = os.environ.get("LUISAPPID", "")
    LUIS_API_KEY = os.environ.get("LUISAPIKEY", "")
    LUIS_API_HOST_NAME = os.environ.get("LUIS_API_HOST_NAME", "")
    LUIS_API_ENDPOINT = os.environ.get("LUIS_API_ENDPOINT", "")

    ## App Insight Service ##
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "APPINSIGHTSINSTRUMENTATIONKEY", "")
    
    
   
