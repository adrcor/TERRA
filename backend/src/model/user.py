from __future__ import annotations
from dataclasses import dataclass, asdict
from client import client
import re
from typing import Any


@dataclass
class User:
    id_user: str
    username: str
    username_lower: str

    @staticmethod
    def new(id_user: str, username: str, username_lower: str | None=None) -> User:
        if username_lower is None:
            username_lower = username.lower()
        return User(id_user, username, username_lower)
    
    @staticmethod
    def get(id_user: str) -> User | None:
        response = client.table('user_data').select('*').eq('id_user', id_user).execute()
        return User.new(**response.data[0]) if response.data else None
    
    def add(self) -> User | None:
        response = client.table('user_data').insert(self.as_dict()).execute()
        if response.data:
            user = response.data[0]
            return User.new(user['id_user'], user['username'], user['username_lower'])

    def as_dict(self) -> dict[str, str]:
        return asdict(self)

    @staticmethod
    def verify_length(username: str) -> bool:
        print(username)
        return 4 <= len(username) <= 16
    
    @staticmethod
    def verify_chars(username: str) -> bool:
        return bool(re.fullmatch(r'^[a-zA-Z0-9_-]+$', username))
    
    @staticmethod
    def verify_available(username: str) -> bool:
        response = client.table('user_data').select('*').eq('username_lower', username.lower()).execute()
        return not bool(response.data)

