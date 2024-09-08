# Twitch Username Checker

## Overview

The **Twitch Username Checker** is a Python-based application designed to check the availability of Twitch usernames. It uses the Twitch API to determine if a username is available or already taken, and provides colorful, user-friendly console output using the `rich` library.

## Features

- **Username Availability Check**: Verify if a Twitch username is available.
- **Rich Console Output**: Styled and colorful output with the `rich` library.
- **Asynchronous Processing**: Efficiently handles multiple username checks concurrently.

## Prerequisites

Ensure you have the following before running the application:

- Python 3.7 or higher
- `pip` for managing Python packages

## Setup Instructions

### 1. Clone the Repository

   Start by cloning the repository to your local machine:

   ``` 
   `git clone https://github.com/yourusername/twitch-username-checker.git`
    `cd twitch-username-checker`
   ```

### 2. Create a Virtual Environment

   It is recommended to create a virtual environment to manage dependencies. This helps to avoid conflicts between packages used in different projects.

   - **On macOS/Linux:**

     ### `python -m venv venv`
     ### `source venv/bin/activate`

   - **On Windows:**

     ```
     `python -m venv venv`
     `venv\Scripts\activate`
      ```

   After activating the virtual environment, your command prompt should show the environment's name, indicating that it's active.

### 3. Install Dependencies

   Install the required Python packages using `pip`. Ensure your virtual environment is activated before running this command:

   ``` `pip install -r requirements.txt`

   This will install all necessary packages listed in `requirements.txt`.

### 4. Configure Environment Variables

   You need to configure your Twitch API credentials. Create a `.env` file in the root directory of the project with the following content:

   ``` 
   `TWITCH_CLIENT_ID=your_client_id`
   `TWITCH_CLIENT_SECRET=your_client_secret`
   ```

   Replace `your_client_id` and `your_client_secret` with your actual Twitch API credentials. These credentials are required to authenticate requests to the Twitch API.

### 5. Directory Structure

   Ensure your project directory follows this structure for proper functionality:

   ```
   twitch-username-checker/ ├── assets/ │ └── username.txt # File containing usernames to check ├── logs/ │ └── app.log # Log file for application output ├── output/ │ └── available_usernames.txt # File where available usernames are saved ├── .env #        File with Twitch API credentials ├── main.py # Main script to run the application └── requirements.txt # File listing project dependencies
   ```

This structure ensures that the application can locate configuration files, input files, and save outputs correctly. Make sure to place your username list in the `assets/username.txt` file, and the script will handle the rest.


## Usage

1. **Prepare Usernames File**

Add the usernames you want to check to `assets/username.txt`. Each username should be on a new line.

2. **Run the Application**

Execute the script to start checking usernames:

### `python main.py`

The application will:
- Read usernames from `assets/username.txt`
- Check each username's availability using the Twitch API
- Save available usernames to `output/available_usernames.txt`
- Display results in the console

3. **View Results**

Check `output/available_usernames.txt` for a list of available usernames. The console will also show the total number of usernames checked and the number of available usernames.

## Logging

Logs and errors are recorded in `logs/app.log`. Use this file for debugging and monitoring.

## Troubleshooting

- **OAuth Token Issues**: Verify your credentials in the `.env` file. Ensure they are correct and have the required permissions.
- **Network Errors**: Ensure your internet connection is stable. The application needs to connect to the Twitch API.

## Contributing

Contributions are welcome! To contribute:
- Open an issue for suggestions or bugs.
- Submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For support or inquiries, dm velikakladusa on Discord.
