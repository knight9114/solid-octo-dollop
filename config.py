from dataclasses import dataclass
import os
from pathlib import Path

@dataclass
class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'default-secret-key'
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{(Path(__file__).parent / "app.db").resolve().absolute()}'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False