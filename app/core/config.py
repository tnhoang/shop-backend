import secrets
from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "PROJECT NAME"
    API_V1_STR: str

    @validator("PROJECT_NAME", pre=True)
    def project_name_cant_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            raise ValueError(v)
        return v

    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
