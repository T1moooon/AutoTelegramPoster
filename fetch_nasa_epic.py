import argparse
import requests
import os
from pathlib import Path
from datetime import datetime
from utils import download_image
from dotenv import load_dotenv


def download_epic_images(api_key, count=5, folder="images"):
    params = {
        "api_key": api_key,
    }
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()
    epic_images = epic_images[:count]
    Path(folder).mkdir(parents=True, exist_ok=True)
    for index, image in enumerate(epic_images):
        image_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        image_name = image["image"]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime('%Y/%m/%d')}/png/{image_name}.png"
        save_path = Path(folder) / f"nasa_epic_{index}.png"
        download_image(image_url, params={"api_key": api_key}, save_path=save_path)
        print(f"Скачано: {save_path}")


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Скачивает фотографии Земли из NASA EPIC.")
    parser.add_argument("--count", type=int, default=5, help="Количество изображений для скачивания.")
    parser.add_argument("--folder", default="images", help="Папка для сохранения изображений.")
    args = parser.parse_args()
    api_key = os.environ['API_KEY']
    download_epic_images(api_key, args.count, args.folder)


if __name__ == "__main__":
    main()
