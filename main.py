import os
import telebot
import instaloader
import requests

API_TOKEN = 'BOT_FATHER_TOKEN'

bot = telebot.TeleBot(API_TOKEN)
loader = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me an Instagram video link and I'll download it for you.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if "instagram.com" in url:
        try:
            video_path = download_instagram_video(url)
            if video_path:
                with open(video_path, 'rb') as video_file:
                    bot.send_video(message.chat.id, video_file)
                os.remove(video_path)
            else:
                bot.send_message(message.chat.id, "Failed to download video.")
        except Exception as e:
            bot.send_message(message.chat.id, f"An error occurred: {e}")
    else:
        bot.send_message(message.chat.id, "Please send a valid Instagram video link.")

def download_instagram_video(url):
    post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
    video_url = post.video_url
    if video_url:
        video_content = requests.get(video_url).content
        video_path = f"{post.shortcode}.mp4"
        with open(video_path, 'wb') as video_file:
            video_file.write(video_content)
        return video_path
    return None

if __name__ == "__main__":
    bot.polling()
