from app.core.config import get_settings

settings = get_settings()

print(f"App name: {settings.app_name}")
print(f"App Environment: {settings.groq_api_key}")