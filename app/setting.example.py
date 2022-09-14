# Тестовый сервисный аккаунт с правом скачивания сертификатов
SERVICE_ACCOUNT_ID = 'SERVICE_ACCOUNT_ID'

# id ключа ключа для сервисного аккаунта
SERVICE_PRIVATE_KEY_ID = 'SERVICE_PRIVATE_KEY_ID'
SERVICE_PRIVATE_KEY_PEM = 'service_private_key.pem'

RETRY_TIME = 86400

FOLDER_ID = 'certificate_manager_folder_id'

DOMAINS = {
    "domain1": {
        "certificate_id": "certificate_id_1",
        "test_site": [
            "test_site_1",
            "test_site_2"
        ]
    },
    "domain2": {
        "certificate_id": "certificate_id_2",
        "test_site": [
            "test_site_1"
        ]
    }
}
