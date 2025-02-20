import argparse
import requests
from pathlib import Path
from utils import download_image


def fetch_spacex_last_launch(launch_id=None, folder="images"):
    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    images = launch_data.get('links', {}).get('flickr', {}).get('original', [])
    Path(folder).mkdir(parents=True, exist_ok=True)
    if images:
        for index, image in enumerate(images):
            save_path = Path(folder) / f"spacex_{index}.jpg"
            download_image(image, save_path)
            print(f"Скачано: {save_path}")


def main():
    parser = argparse.ArgumentParser(description="Скачивает фотографии последнего запуска SpaceX.")
    parser.add_argument("--folder", default="images", help="Папка для сохранения изображений.")
    parser.add_argument("--launch_id", help="ID запуска SpaceX. Если не указан, скачивается последний запуск.")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id, args.folder)


if __name__ == "__main__":
    main()
