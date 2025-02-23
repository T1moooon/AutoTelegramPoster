import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote


def download_image(image_url, save_path, params=None):
    response = requests.get(image_url, params=params)
    response.raise_for_status()

    folder_path = Path(save_path).parent
    folder_path.mkdir(parents=True, exist_ok=True)

    with open(save_path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url_to_extension):
    path = urlsplit(url_to_extension).path
    filename = unquote(Path(path).name)
    return Path(filename).suffix
