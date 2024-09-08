import aiohttp
from config import TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET

async def get_oauth_token(session: aiohttp.ClientSession) -> str:
    """Fetch OAuth token from Twitch."""
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    
    async with session.post(url, data=params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get("access_token")
        else:
            raise Exception(f"Failed to get OAuth token. Status code: {response.status}")

async def check_twitch_username(session: aiohttp.ClientSession, username: str, oauth_token: str) -> bool:
    """Check if a Twitch username is available or taken."""
    if len(username) < 4:
        return None

    url = f"https://api.twitch.tv/helix/users?login={username}"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {oauth_token}"
    }
    
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            if not data['data']:
                return True  # Username is available
            else:
                return False  # Username is taken
        else:
            raise Exception(f"Failed to check username {username}. Status code: {response.status}")
