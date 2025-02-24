# Космический Телеграм

Этот проект позволяет скачивать фотографии космоса с различных источников (NASA APOD, NASA EPIC, SpaceX) и публиковать их в Telegram-канале. Включает несколько скриптов для скачивания и публикации изображений.

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

Создайте файл `.env` в корне проекта и добавьте туда следующие переменные:

```env
TG_BOT_TOKEN=ваш_токен_бота
TG_CHAT_ID=ваш_chat_id
NASA_API_KEY=ваш_api_ключ_от_nasa
TG_BOT_DELAY=4  # Задержка в часах для публикации (по умолчанию 4)
```

## Скрипты

### 1. `fetch_nasa_apod.py`
Скачивает фотографии из коллекции NASA Astronomy Picture of the Day (APOD).

**Использование:**
```bash
python fetch_nasa_apod.py [--count 5] [--folder images]
```
- `--count`: Количество изображений для скачивания (по умолчанию 5).
- `--folder`: Папка для сохранения изображений (по умолчанию `images`).

**Пример:**
```bash
python fetch_nasa_apod.py --count 10 --folder nasa_apod
```

### 2. `fetch_nasa_epic.py`
Скачивает фотографии Земли из коллекции NASA EPIC (Earth Polychromatic Imaging Camera).

**Использование:**
```bash
python fetch_nasa_epic.py [--count 5] [--folder images]
```
- `--count`: Количество изображений для скачивания (по умолчанию 5).
- `--folder`: Папка для сохранения изображений (по умолчанию `images`).

**Пример:**
```bash
python fetch_nasa_epic.py --count 3 --folder nasa_epic
```

### 3. `fetch_spacex_images.py`
Скачивает фотографии последнего запуска SpaceX или указанного запуска по ID.

**Использование:**
```bash
python fetch_spacex_images.py [--folder images] [--launch_id ваш_launch_id]
```
- `--folder`: Папка для сохранения изображений (по умолчанию `images`).
- `--launch_id`: ID запуска SpaceX. Если не указан, скачиваются фотографии последнего запуска.

**Пример:**
```bash
python fetch_spacex_images.py --folder spacex --launch_id 5eb87d47ffd86e000604b38a
```

### 4. `post_telegram_bot.py`
Отправляет одно изображение в Telegram-канал. Если изображение не указано, выбирает случайное из папки `images`.

**Использование:**
```bash
python post_telegram_bot.py [--image путь_к_изображению]
```
- `--image`: Путь к изображению для отправки. Если не указан, выбирается случайное изображение из папки `images`.

**Пример:**
```bash
python post_telegram_bot.py --image images/nasa_apod_0.png
```

### 5. `publish_photos.py`
Публикует фотографии из указанной папки в Telegram-канал с заданной задержкой. Если фотографии заканчиваются, перемешивает их и начинает заново.

**Использование:**
```bash
python publish_photos.py [--folder images]
```
- `--folder`: Папка с фотографиями для публикации (по умолчанию `images`).

**Пример:**
```bash
python publish_photos.py --folder nasa_images
```

## Настройка

### Telegram-бот:
1. Создайте бота через `BotFather` и получите токен.
2. Добавьте бота в канал и сделайте его администратором.
3. Узнайте `chat_id` канала (можно использовать метод `getUpdates`).

### NASA API:
- Получите API ключ на [NASA API](https://api.nasa.gov/).

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/)