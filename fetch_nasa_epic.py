import argparse
import requests
from pathlib import Path
from urllib.parse import urlencode
from datetime import datetime
from utils import download_image


def download_epic_images(api_key, count=5, folder="images"):
    params = {
        "api_key": api_key,
    }
    encoded_params = urlencode(params)
    url = f'https://api.nasa.gov/EPIC/api/natural?{encoded_params}'
    response = requests.get(url)
    response.raise_for_status()
    epic_data = response.json()
    epic_data = epic_data[:count]
    Path(folder).mkdir(parents=True, exist_ok=True)
    for index, image in enumerate(epic_data):
        image_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        image_name = image["image"]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime('%Y/%m/%d')}/png/{image_name}.png?api_key={api_key}"
        save_path = Path(folder) / f"nasa_epic_{index}.png"
        download_image(image_url, save_path)
        print(f"Скачано: {save_path}")


def main():
    parser = argparse.ArgumentParser(description="Скачивает фотографии Земли из NASA EPIC.")
    parser.add_argument("--api_key", required=True, help="API ключ для доступа к NASA API.")
    parser.add_argument("--count", type=int, default=5, help="Количество изображений для скачивания.")
    parser.add_argument("--folder", default="images", help="Папка для сохранения изображений.")
    args = parser.parse_args()
    download_epic_images(args.api_key, args.count, args.folder)


if __name__ == "__main__":
    main()
