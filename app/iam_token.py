import os
import time
import jwt
import requests
from dotenv import load_dotenv

import setting
from .logger import Logger

load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SERVICE_ACCOUNT_ID = setting.SERVICE_ACCOUNT_ID
SERVICE_PRIVATE_KEY_ID = setting.SERVICE_PRIVATE_KEY_ID
SERVICE_PRIVATE_KEY_PEM = os.path.join(
    BASE_DIR, setting.SERVICE_PRIVATE_KEY_PEM
)
ENDPOINT = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'

logger = Logger().get_logger()


def get_jwt_token() -> str:
    """Получение JWT токена для сервисного аккаунта.
    SERVICE_ACCOUNT_ID: id сервисного аккаунта с правами
    certificate-manager.certificates.downloader
    SERVICE_PRIVATE_KEY_PEM: pem файл для сервисного аккаунта
    SERVICE_PRIVATE_KEY_ID: id pem ключа.
    [FAQ](https://cloud.yandex.ru/docs/iam/operations/iam-token/create-for-sa).
    """
    with open(SERVICE_PRIVATE_KEY_PEM, 'r') as private:
        # Чтение закрытого ключа из файла.
        private_key = private.read()

    now = int(time.time())
    payload = {
            'aud': ENDPOINT,
            'iss': SERVICE_ACCOUNT_ID,
            'iat': now,
            'exp': now + 360
    }

    # Формирование JWT.
    encoded_token = jwt.encode(
        payload,
        private_key,
        algorithm='PS256',
        headers={'kid': SERVICE_PRIVATE_KEY_ID})
    return encoded_token


def exchange_jwt(jwt_token) -> str:
    """Обмен JWT на IAM токен."""
    iam_headers = {
      'Content-Type': 'application/json',
    }
    iam_body = {'jwt': jwt_token}
    iam_request = requests.post(
      ENDPOINT,
      headers=iam_headers,
      json=iam_body,
    ).json()
    iam = iam_request.get('iamToken')
    return iam


def get_iam_token() -> str:
    """Получение IAM токена."""
    jwt_token = get_jwt_token()
    try:
        iam_token = exchange_jwt(jwt_token)
        if iam_token is not None:
            logger.info('IAM токен получен')
            return iam_token
    except Exception as error:
        logger.critical('IAM не выпустился', exc_info=error)


def main():
    get_iam_token()


if __name__ == '__main__':
    main()
