from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    openai_api_key: SecretStr
    database_url: str
    langsmith_api_key: SecretStr
    langchain_tracing_v2: bool = False
    langsmith_endpoint: str
    langchain_project: str
    postgres_user: str
    postgres_password: SecretStr
    postgres_db: str

    model_config = SettingsConfigDict(env_file=".env")