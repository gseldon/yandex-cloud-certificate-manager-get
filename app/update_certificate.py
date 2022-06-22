import os
import time
from dotenv import load_dotenv

import setting
from module.iam_token import get_iam_token
from module.info_cert import CertificateInfo
from module.download_certificate import download_certificate
from module.ssl_expiry_datetime import ssl_expiry_datetime
from module.logger import Logger

load_dotenv()

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', os.pardir)
)
DOMAINS = setting.DOMAINS
FOLDER_ID = setting.FOLDER_ID
RETRY_TIME = setting.RETRY_TIME


def check_exist_cert(domain, certificate_id):
    full_chain_file_name = (
        f'certificate_folder/{domain}_{certificate_id}_full_chain.pem'
    )
    private_file_name = (
        f'certificate_folder/{domain}_{certificate_id}_private.pem'
    )
    if (
        os.path.exists(os.path.join(BASE_DIR, full_chain_file_name))
        or os.path.exists(os.path.join(BASE_DIR, private_file_name))
    ):
        return True
    return False


def main():
    logger = Logger().get_logger()
    while True:
        logger.debug('Получение токена')
        iam = get_iam_token()

        for domain in DOMAINS:
            certificate_id = DOMAINS[domain].get('certificate_id')
            cert = CertificateInfo(certificate_id, FOLDER_ID, iam)
            date_yandex_not_after = cert.get_not_after_date()

            if check_exist_cert(domain, certificate_id):
                logger.debug(
                    f'Сертификат домена {domain} найден в папке,'
                    'проверяем дату'
                )
                for i in range(len(DOMAINS[domain]['test_site'])):
                    test_site = DOMAINS[domain]['test_site'][i]
                    date_site_not_after = ssl_expiry_datetime(test_site)
                    if (date_yandex_not_after < date_site_not_after):
                        try:
                            download_certificate(iam, certificate_id, domain)
                            logger.info(f'Сертификат для {domain} скачен')
                        except Exception as error:
                            logger.error(
                                'Ошибка скачивания сертификата'
                                f'{domain} {error}'
                            )
                    else:
                        logger.info(
                            f'{test_site} -> Сертификат для {domain} не требуется обновлять'
                        )
            else:
                logger.warning(
                        f'Сертификат для {domain} не найдет, скачиваю'
                    )
                try:
                    download_certificate(iam, certificate_id, domain)
                    logger.info(f'Сертификат для {domain} скачен')
                except Exception as error:
                    logger.error(
                        f'Ошибка скачивания сертификата {domain} {error}'
                    )
        logger.info(f'Ожидаю {RETRY_TIME} секунд')
        time.sleep(RETRY_TIME)


if __name__ == '__main__':
    main()
