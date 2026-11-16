from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="MYAPP_",
        env_file=".env",
        extra="ignore",
    )

    app_name: str = "Food ordering API"
    environment: str = "dev"

    database_url: SecretStr
    db_pool_size: int = 5
    db_max_overflow: int = 5

    jwt_secret: SecretStr
    jwt_algorithm: str = "HS256"
    access_token_ttl_minutes: int = 15
