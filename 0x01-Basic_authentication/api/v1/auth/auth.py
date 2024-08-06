#!/usr/bin/env python3
"""auth.py
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.
        :param path: The path to check
        :param excluded_paths:list of paths not require authentication
        :return: False (default implementation)
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        :param request: The request object
        :return: None (default implementation)
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Retrieves the current user from the request.
        :param request: The request object
        :return: None (default implementation)
        """
        return None
