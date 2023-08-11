from pydantic import Field, validator
from enum import Enum
from pydantic_settings import BaseSettings
import yaml

class ConfigEnv(str, Enum):
    DEV = "dev"
    PROD = "prod"

class DBConfig(BaseSettings):
    host: str = Field(default="localhost", env="db_host")
    port: int = Field(default=100, env="db_port")
    username: str = Field(default="user", env="db_username")
    password: str = Field(default="user", env="db_password")
    database: str = Field(default="dev", env="db_database")
    
    @validator('port')
    def validate_port(cls, value):
        if not (10 <= value <= 1024):  # 범위 내에 있는지 확인
            raise ValueError("Port must be between 10 and 1024 (inclusive)")
        return value

class AppConfig(BaseSettings):
    env: ConfigEnv = Field(default="dev", env="env")
    db: DBConfig = DBConfig()

# YAML 파일을 읽어옴
with open("dev_config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# 예상값 설정
expected = {
    "env": "dev",
    "db": {
        "host": "localhost",
        # "port": 200,  # 예시로 12345로 수정
        "username": "user",  # 예시로 수정
        "password": "password",  # 예시로 수정
        "database": "dev"
    }
}

# Pydantic 모델을 사용하여 YAML 데이터를 파싱
config_with_pydantic = AppConfig(**config)

# 테스트
assert config_with_pydantic.env == ConfigEnv.DEV
# assert config_with_pydantic.db.dict() == expected["db"]
