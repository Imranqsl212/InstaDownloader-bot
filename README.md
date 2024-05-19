```markdown
# Instagram Video Downloader Telegram Bot

This Telegram bot allows users to download videos from Instagram by simply sending the video link. The bot uses the `instaloader` library to fetch the video URL and `requests` to download the video. The downloaded video is then sent back to the user in MP4 format.

## Features

- Download Instagram videos by sending a link to the bot.
- Automatically sends the downloaded video to the user.
- Deletes the downloaded video file after sending to save space.

## Prerequisites

- Python 3.6 or higher
- A Telegram bot token (you can obtain one by creating a bot on Telegram through BotFather)

## Installation


1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/instagram-video-downloader-bot.git](https://github.com/Imranqsl212/InstaDownloader-bot/tree/master)
   ```

2. Install the required libraries:
   ```bash
   pip install instaloader requests pyTelegramBotAPI
   ```

3. Replace `'YOUR_TELEGRAM_BOT_API_TOKEN'` in `main.py` with your actual Telegram bot token.

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. Open Telegram and start a chat with your bot (search for the bot by its username or use the link provided by BotFather).

3. Send an Instagram video link to the bot. The bot will download the video and send it back to you.

## Code Overview

- `main.py`: The main script that contains the bot implementation.
- `download_instagram_video(url)`: Function that downloads the Instagram video from the provided URL using `instaloader` and `requests`.
- `handle_message(message)`: Function to handle incoming messages and process Instagram links.

## Dependencies

- `instaloader`: Library to interact with Instagram and download media.
- `requests`: Library to handle HTTP requests.
- `pyTelegramBotAPI`: Library to interact with the Telegram Bot API.

## Example

1. Start the bot:
   ```bash
   python main.py
   ```

2. Send a message to the bot with an Instagram video link:
   ```
   https://www.instagram.com/.......
   ```

3. The bot will reply with the downloaded video in MP4 format.

## Contributing

If you have any suggestions or find any bugs, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

