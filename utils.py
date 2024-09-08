import logging
from pathlib import Path
from rich.logging import RichHandler

# Set up logging
def setup_logging():
    log_dir = Path(__file__).resolve().parent / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[RichHandler()]
    )

def read_usernames_from_file(filename: Path) -> list:
    """Read usernames from a file."""
    if not filename.is_file():
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    with filename.open('r') as file:
        return file.read().splitlines()

def write_available_usernames(filename: Path, usernames: list):
    """Write available usernames to a file."""
    if not filename.parent.exists():
        filename.parent.mkdir(parents=True, exist_ok=True)
    
    with filename.open('w') as file:
        for username in usernames:
            file.write(f"{username}\n")
