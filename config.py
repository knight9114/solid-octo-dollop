from dataclasses import dataclass
import os

@dataclass
class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'default-secret-key'