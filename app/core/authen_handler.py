import os
from datetime import datetime, timedelta
from fastapi.params import Security

import jwt


from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext


class AuthHandler:
    security = HTTPBearer()
    hasher = CryptContext(schemes=["bcrypt"])
    secret = os.getenv("SECRET", "secret")

    def encode_password(self, plain_password):
        return self.hasher.hash(plain_password)

    def verify_password(self, plain_password, encoded_password):
        return self.hasher.verify(plain_password, encoded_password)

    def encode_token(self, username):
        payload = {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30),
            "scope": "access_token",
            "sub": username,
        }
        return jwt.encode(payload, "secret", algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            if payload["scope"] == "access_token":
                return payload["sub"]
            raise HTTPException(401, "scope invalid")
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "token invalid")

    # Refresh token
    def encode_refresh_token(self, username):
        payload = {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=1, minutes=30),
            "scope": "refresh_token",
            "sub": username,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_refresh_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            if payload["scope"] == "refresh_token":
                return payload["sub"]
            raise HTTPException(401, "scope invalid")
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "refresh token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "refresh token invalid")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth_handler = AuthHandler()
