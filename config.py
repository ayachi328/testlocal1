#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "c92153b7-2d98-489f-b880-228688c68e13")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "g4j8Q~r8FInvZOcJrMC3IBpHexi4JbZjOGRS0bvM")
    LUIS_APP_ID = os.environ.get("LuisAppId", "344ec82a-9bb8-40cc-a18c-5e6b86ae28b2")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "124604c7b30c4a24874fb88553d7652f")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "f291a401-109a-4de2-941d-39077f0a0f8b"
    )
