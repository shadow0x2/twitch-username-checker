import asyncio
import logging 
from aiohttp import ClientSession
from config import ASSETS_DIR, OUTPUT_DIR
from twitch_api import get_oauth_token, check_twitch_username
from utils import setup_logging, read_usernames_from_file, write_available_usernames
from rich.console import Console
from rich.text import Text

# Initialize rich console
console = Console()

async def main():
    setup_logging()

    username_file = ASSETS_DIR / 'username.txt'
    output_file = OUTPUT_DIR / 'available_usernames.txt'

    try:
        usernames = read_usernames_from_file(username_file)

        async with ClientSession() as session:
            oauth_token = await get_oauth_token(session)
            tasks = [check_twitch_username(session, username.strip(), oauth_token) for username in usernames]
            results = await asyncio.gather(*tasks)

            available_usernames = [username for username, available in zip(usernames, results) if available]
            write_available_usernames(output_file, available_usernames)

            # Display available usernames
            if available_usernames:
                # Use rich for colorful output
                console.print("\n[bold green]Available Usernames:[/bold green]")
                console.print("[bold red]List Includes Banned/Closed Accounts. \n[/bold red]")
                for username in available_usernames:
                    console.print(f"  - [bold cyan]{username}[/bold cyan]")  # Cyan color for usernames
                
                console.print(f"\nTotal available: [bold green]{len(available_usernames)}[/bold green]")
            else:
                console.print("[bold red]No available usernames found.[/bold red]")
            
            console.print(f"Total checked: [bold yellow]{len(usernames)}[/bold yellow]")
            console.print(f"Output saved at [bold magenta]{output_file}[/bold magenta]\n")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
