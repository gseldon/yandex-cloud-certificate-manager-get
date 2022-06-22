# Тестовый сервисный аккаунт с правом скачивания сертификатов
SERVICE_ACCOUNT_ID = 'ajet9b3qs476ck5r2rf6'
# id ключа ключа для сервисного аккаунта
SERVICE_PRIVATE_KEY_ID = 'ajehfc5akk81efcuijrs'
SERVICE_PRIVATE_KEY_PEM = 'service_private_key.pem'

RETRY_TIME = 86400

FOLDER_ID = 'b1gml69t5c5d4h6f56nk'

DOMAINS = {
        "tele-med.ai": {
            "certificate_id": "fpq3fvrfjs0fo7qv32qs",
            "test_site": [
                "tele-med.ai",
                "edu.tele-med.ai"
            ]
        },
        "rpcmr.ru": {
            "certificate_id": "fpqdnqc4miqm5ichn20s",
            "test_site": [
                "mosmed.ai"
            ]
        }
}
