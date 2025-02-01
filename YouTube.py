import subprocess

url = input("Введите URL видео/плейлиста: ")
save_directory = "/home/evgeniy/Видео/"
resolution = input("Введите желаемое разрешение (например, 720p, 1080p и т.д.): ")

subprocess.run(
    [
        "yt-dlp",
        "-o",
        f"{save_directory}/%(title)s.%(ext)s",
        "-f",
        f"bestvideo[height<={resolution}]+bestaudio/best",
        url,
    ]
)

# /home/evgeniy/Видео/
# https://youtu.be/RUnarFFpHOg?si=8GFjAPs-fcEH7yPL
