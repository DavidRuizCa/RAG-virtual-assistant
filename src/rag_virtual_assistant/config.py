from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    anthropic_api_key: SecretStr
    database_url: str
    langsmith_api_key: SecretStr
    langchain_tracing_v2: bool = False

    model_config = SettingsConfigDict(env_file=".env")