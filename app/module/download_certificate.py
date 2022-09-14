import os

import requests

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', os.pardir)
)


def download_certificate(iam: str, certificate_id: str, site: str):
    """Download certificate.

    Arguments:
        iam:            IAM токен
        certificate_id: id сертификата.
    """
    headers = {
        'Authorization': f'Bearer {iam}',
    }
    certificate_service = 'https://data.certificate-manager.api.cloud.yandex.net'
    certificate_manager = (
        f'{certificate_service}/certificate-manager/v1/certificates/'
        f'{certificate_id}:getContent'
    )

    get_cert_url = certificate_manager

    response = requests.get(
        get_cert_url,
        headers=headers,
    ).json()

    full_chain_file_name = (
        f'certificate_folder/{site}_{certificate_id}_full_chain.pem'
    )
    private_file_name = (
        f'certificate_folder/{site}_{certificate_id}_private.pem'
    )

    full_chain_file = os.path.join(BASE_DIR, full_chain_file_name)
    private_file = os.path.join(BASE_DIR, private_file_name)

    with open(full_chain_file, 'w', encoding="utf-8") as file:
        for i in range(len(response)):
            file.write(response['certificateChain'][0])

    with open(private_file, 'w', encoding="utf-8") as f:
        f.write(response['privateKey'])
