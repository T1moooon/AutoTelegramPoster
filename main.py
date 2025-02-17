import requests
import os
from pathlib import Path
from urllib.parse import urlsplit,  unquote, urlencode
from datetime import datetime
from environs import Env


def download_image(image_url, save_path):
    response = requests.get(image_url)
    response.raise_for_status()

    folder_path = os.path.dirname(save_path)
    Path(folder_path).mkdir(parents=True, exist_ok=True)

    with open(save_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder="images"):
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    images = launch_data.get('links', {}).get('flickr', {}).get('original', [])
    Path(folder).mkdir(parents=True, exist_ok=True)
    if images:
        for index, image in enumerate(images):
            save_path = os.path.join(folder, f"spacex_{index}.jpg")
            download_image(image, save_path)


def get_file_extension(url_to_extension):
    path = urlsplit(url_to_extension).path
    filename = unquote(os.path.basename(path))
    _, extension = os.path.splitext(filename)
    return extension


def download_nasa_images(api_key, count=30, folder="images"):
    params = {
        "api_key": api_key,
        "count": count,
    }
    encoded_params = urlencode(params)
    url = f"https://api.nasa.gov/planetary/apod?{encoded_params}"
    response = requests.get(url)
    response.raise_for_status()
    apod_data = response.json()
    Path(folder).mkdir(parents=True, exist_ok=True)
    image_counter = 0
    for apod in apod_data:
        if apod.get("media_type") == "image":
            image_url = apod["url"]
            extension = get_file_extension(image_url)
            save_path = os.path.join(folder, f"nasa_apod_{image_counter}{extension}")
            download_image(image_url, save_path)
            image_counter += 1


def download_epic_images(api_key, count, folder="images"):
    params = {
        "api_key": api_key,
    }
    encoded_params = urlencode(params)
    url = f'https://api.nasa.gov/EPIC/api/natural?{encoded_params}'
    responce = requests.get(url)
    responce.raise_for_status()
    epic_data = responce.json()
    epic_data = epic_data[:count]
    Path(folder).mkdir(parents=True, exist_ok=True)
    for index, image in enumerate(epic_data):
        image_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        image_name = image["image"]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime('%Y/%m/%d')}/png/{image_name}.png?api_key={api_key}"
        save_path = os.path.join(folder, f"nasa_epic_{index}.png")
        download_image(image_url, save_path)
    return image_url


def main():
    env = Env()
    env.read_env()
    api_key = env.str("API_KEY")
    fetch_spacex_last_launch()
    download_nasa_images(api_key, count=15)
    download_epic_images(api_key, count=5)


if __name__ == "__main__":
    main()
