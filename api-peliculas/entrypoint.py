import os

from app import create_app
 
settings_module = os.getenv('APP_SETTINGS_MODULE')
print(f'Loading settings: {settings_module}')
app = create_app(settings_module)
