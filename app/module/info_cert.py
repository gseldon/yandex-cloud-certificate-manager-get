"""
Obtaining information on certificates.
"""
from datetime import datetime

import requests

ENDPOINT = (
    'https://certificate-manager.api.cloud.yandex.net/certificate-manager/v1/certificates'
)


class CertificateInfo:
    """
    Obtaining information on certificates.
    """
    def __init__(self,
                 certificate_id: str,
                 folder_id: str,
                 iam: str,
                 ) -> None:
        self.certificate_id = certificate_id
        self.folder_id = folder_id
        self.iam = iam

    def get_info(self) -> dict:
        headers = {'Authorization': f'Bearer {self.iam}'}
        params = {'folderId': self.folder_id}
        certificate_manager = ENDPOINT
        certificate_num = 0
        response = requests.get(
            certificate_manager,
            headers=headers,
            params=params
        ).json()
        certificates_count = len(response['certificates'])

        for certificate in range(certificates_count):
            if response['certificates'][certificate].get('id') == self.certificate_id:
                certificate_num = certificate
        certificate_info = response['certificates'][certificate_num]
        return certificate_info

    def get_not_after_date(self) -> datetime:
        certificate_info = self.get_info()
        date_after_str = certificate_info.get('notAfter')
        date_after = datetime.strptime(date_after_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_after
