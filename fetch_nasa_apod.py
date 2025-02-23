import argparse
import requests
import os
from pathlib import Path
from utils import download_image, get_file_extension
from dotenv import load_dotenv


def download_nasa_images(api_key, count=30, folder="images"):
    params = {
        "api_key": api_key,
        "count": count,
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_images = response.json()
    Path(folder).mkdir(parents=True, exist_ok=True)
    image_counter = 0
    for apod in apod_images:
        if apod.get("media_type") == "image":
            continue
        image_url = apod["url"]
        extension = get_file_extension(image_url)
        save_path = Path(folder) / f"nasa_apod_{image_counter}{extension}"
        download_image(image_url, save_path)
        print(f"Скачано: {save_path}")
        image_counter += 1


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Скачивает фотографии NASA APOD.")
    parser.add_argument("--count", type=int, default=5, help="Количество изображений для скачивания.")
    parser.add_argument("--folder", default="images", help="Папка для сохранения изображений.")
    args = parser.parse_args()
    api_key = os.environ['API_KEY']
    download_nasa_images(api_key, args.count, args.folder)


if __name__ == "__main__":
    main()
