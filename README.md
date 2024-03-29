[![Codacy Security Scan](https://github.com/gseldon/yandex-cloud-certificate-manager-get/actions/workflows/codacy.yml/badge.svg)](https://github.com/gseldon/yandex-cloud-certificate-manager-get/actions/workflows/codacy.yml) [![Snyk Container](https://github.com/gseldon/yandex-cloud-certificate-manager-get/actions/workflows/snyk-container.yml/badge.svg)](https://github.com/gseldon/yandex-cloud-certificate-manager-get/actions/workflows/snyk-container.yml)

# Программа скачивания сертификатов с YandexCloud Certificate Manager

Запрашивает из каталога сервис.
Получает все выпущенные сертификаты.
При наличии сертификатов, проверяет на доступность. 
Скачивает их в указанную  папку. 

## Подготовка

Для сервисного аккаунта, с доступом к сертификатом, подготовить файл .pem 

```./service_private_key.pem```

Создать файл настроек ```setting.example.py``` > ```setting.py```

### Доработать

- [] Лог пишет два раза((, видимо что-то с созданием объекта

    ```
    2022-06-21 14:08:54,051 [INFO] Получение токена
    2022-06-21 14:08:54,051 [INFO] Получение токена
    2022-06-21 14:08:54,146 [INFO] IAM токен получен
    2022-06-21 14:08:54,146 [INFO] IAM токен получен
    2022-06-21 14:08:54,270 [INFO] Сертификат для tele-med.ai не требуется обновлять
    2022-06-21 14:08:54,270 [INFO] Сертификат для tele-med.ai не требуется обновлять
    2022-06-21 14:08:54,291 [INFO] Сертификат для edu.tele-med.ai не требуется обновлять
    2022-06-21 14:08:54,291 [INFO] Сертификат для edu.tele-med.ai не требуется обновлять
    2022-06-21 14:08:54,450 [INFO] Сертификат для mosmed.ai скачен
    2022-06-21 14:08:54,450 [INFO] Сертификат для mosmed.ai скачен
    ```
- [ ] Подумать с общим файлом настроек. Слишком много одинаковых переменных.
- [ ] Добавить перевыпуск токена по времени.
- [ ] Расширить исключения, логировать их.
- [ ] Добавить докер, для встраивания в сервисы.
