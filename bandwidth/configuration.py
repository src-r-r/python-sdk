# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from enum import Enum
from bandwidth.api_helper import APIHelper
from bandwidth.http.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0
    CUSTOM = 1


class Server(Enum):
    """An enum for API servers"""
    DEFAULT = 0
    MESSAGINGDEFAULT = 1
    TWOFACTORAUTHDEFAULT = 2
    VOICEDEFAULT = 3
    WEBRTCDEFAULT = 4


class Configuration(object):
    """A class used for configuring the SDK by a user.
    """

    @property
    def http_client(self):
        return self._http_client

    @property
    def timeout(self):
        return self._timeout

    @property
    def max_retries(self):
        return self._max_retries

    @property
    def backoff_factor(self):
        return self._backoff_factor

    @property
    def environment(self):
        return self._environment

    @property
    def base_url(self):
        return self._base_url

    @property
    def messaging_basic_auth_user_name(self):
        return self._messaging_basic_auth_user_name

    @property
    def messaging_basic_auth_password(self):
        return self._messaging_basic_auth_password

    @property
    def two_factor_auth_basic_auth_user_name(self):
        return self._two_factor_auth_basic_auth_user_name

    @property
    def two_factor_auth_basic_auth_password(self):
        return self._two_factor_auth_basic_auth_password

    @property
    def voice_basic_auth_user_name(self):
        return self._voice_basic_auth_user_name

    @property
    def voice_basic_auth_password(self):
        return self._voice_basic_auth_password

    @property
    def web_rtc_basic_auth_user_name(self):
        return self._web_rtc_basic_auth_user_name

    @property
    def web_rtc_basic_auth_password(self):
        return self._web_rtc_basic_auth_password

    def __init__(self, timeout=60, max_retries=3, backoff_factor=0,
                 environment=Environment.PRODUCTION,
                 base_url='https://www.example.com',
                 messaging_basic_auth_user_name='TODO: Replace',
                 messaging_basic_auth_password='TODO: Replace',
                 two_factor_auth_basic_auth_user_name='TODO: Replace',
                 two_factor_auth_basic_auth_password='TODO: Replace',
                 voice_basic_auth_user_name='TODO: Replace',
                 voice_basic_auth_password='TODO: Replace',
                 web_rtc_basic_auth_user_name='TODO: Replace',
                 web_rtc_basic_auth_password='TODO: Replace'):
        # The value to use for connection timeout
        self._timeout = timeout

        # The number of times to retry an endpoint call if it fails
        self._max_retries = max_retries

        # A backoff factor to apply between attempts after the second try.
        # urllib3 will sleep for:
        # `{backoff factor} * (2 ** ({number of total retries} - 1))`
        self._backoff_factor = backoff_factor

        # Current API environment
        self._environment = environment

        # base_url value
        self._base_url = base_url

        # The username to use with basic authentication
        self._messaging_basic_auth_user_name = messaging_basic_auth_user_name

        # The password to use with basic authentication
        self._messaging_basic_auth_password = messaging_basic_auth_password

        # The username to use with basic authentication
        self._two_factor_auth_basic_auth_user_name = two_factor_auth_basic_auth_user_name

        # The password to use with basic authentication
        self._two_factor_auth_basic_auth_password = two_factor_auth_basic_auth_password

        # The username to use with basic authentication
        self._voice_basic_auth_user_name = voice_basic_auth_user_name

        # The password to use with basic authentication
        self._voice_basic_auth_password = voice_basic_auth_password

        # The username to use with basic authentication
        self._web_rtc_basic_auth_user_name = web_rtc_basic_auth_user_name

        # The password to use with basic authentication
        self._web_rtc_basic_auth_password = web_rtc_basic_auth_password

        # The Http Client to use for making requests.
        self._http_client = self.create_http_client()

    def clone_with(self, timeout=None, max_retries=None, backoff_factor=None,
                   environment=None, base_url=None,
                   messaging_basic_auth_user_name=None,
                   messaging_basic_auth_password=None,
                   two_factor_auth_basic_auth_user_name=None,
                   two_factor_auth_basic_auth_password=None,
                   voice_basic_auth_user_name=None,
                   voice_basic_auth_password=None,
                   web_rtc_basic_auth_user_name=None,
                   web_rtc_basic_auth_password=None):
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        environment = environment or self.environment
        base_url = base_url or self.base_url
        messaging_basic_auth_user_name = messaging_basic_auth_user_name or self.messaging_basic_auth_user_name
        messaging_basic_auth_password = messaging_basic_auth_password or self.messaging_basic_auth_password
        two_factor_auth_basic_auth_user_name = two_factor_auth_basic_auth_user_name or self.two_factor_auth_basic_auth_user_name
        two_factor_auth_basic_auth_password = two_factor_auth_basic_auth_password or self.two_factor_auth_basic_auth_password
        voice_basic_auth_user_name = voice_basic_auth_user_name or self.voice_basic_auth_user_name
        voice_basic_auth_password = voice_basic_auth_password or self.voice_basic_auth_password
        web_rtc_basic_auth_user_name = web_rtc_basic_auth_user_name or self.web_rtc_basic_auth_user_name
        web_rtc_basic_auth_password = web_rtc_basic_auth_password or self.web_rtc_basic_auth_password

        return Configuration(
            timeout=timeout, max_retries=max_retries,
            backoff_factor=backoff_factor, environment=environment, base_url=base_url,
            messaging_basic_auth_user_name=messaging_basic_auth_user_name,
            messaging_basic_auth_password=messaging_basic_auth_password,
            two_factor_auth_basic_auth_user_name=two_factor_auth_basic_auth_user_name,
            two_factor_auth_basic_auth_password=two_factor_auth_basic_auth_password,
            voice_basic_auth_user_name=voice_basic_auth_user_name,
            voice_basic_auth_password=voice_basic_auth_password,
            web_rtc_basic_auth_user_name=web_rtc_basic_auth_user_name,
            web_rtc_basic_auth_password=web_rtc_basic_auth_password
        )

    def create_http_client(self):
        return RequestsClient(timeout=self.timeout,
                              max_retries=self.max_retries,
                              backoff_factor=self.backoff_factor)

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'api.bandwidth.com',
            Server.MESSAGINGDEFAULT: 'https://messaging.bandwidth.com/api/v2',
            Server.TWOFACTORAUTHDEFAULT: 'https://mfa.bandwidth.com/api/v1/',
            Server.VOICEDEFAULT: 'https://voice.bandwidth.com',
            Server.WEBRTCDEFAULT: 'https://api.webrtc.bandwidth.com/v1'
        },
        Environment.CUSTOM: {
            Server.DEFAULT: '{base_url}',
            Server.MESSAGINGDEFAULT: '{base_url}',
            Server.TWOFACTORAUTHDEFAULT: '{base_url}',
            Server.VOICEDEFAULT: '{base_url}',
            Server.WEBRTCDEFAULT: '{base_url}'
        }
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "base_url": {'value': self.base_url, 'encode': False},
        }

        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters
        )
