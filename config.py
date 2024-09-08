import os
from pathlib import Path
from dotenv import load_dotenv

# Define paths
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'
ASSETS_DIR = BASE_DIR / 'assets'
LOGS_DIR = BASE_DIR / 'logs'
OUTPUT_DIR = BASE_DIR / 'output'

# Load environment variables
load_dotenv(dotenv_path=ENV_FILE)

# Access environment variables
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
