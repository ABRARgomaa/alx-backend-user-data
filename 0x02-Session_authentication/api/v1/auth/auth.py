#!/usr/bin/env python3
"""
auth module
"""

from flask import request
from typing import List, TypeVar
from fnmatch import fnmatch
import os

session_name = os.getenv('SESSION_NAME', None)


class Auth:
    """
    auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth func
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for pattern in excluded_paths:
            if fnmatch(path, pattern.rstrip('/') + '*'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header func
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user func
        """
        return None

    def session_cookie(self, request=None):
        """session cookie method"""
        if request is None:
            return None
        _my_session_id = request.cookies.get(session_name)
        return _my_session_id
