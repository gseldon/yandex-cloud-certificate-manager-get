import OpenSSL
import secrets

DOMAIN = 'adfs.tele-med.ai'
CERT_ID = 'fpqmt77topfnhohfm68v'

password = secrets.token_urlsafe(32)

with open(
    f'./{DOMAIN}_{CERT_ID}_private.pem', 'r'
) as file:
    private_key = file.read()

with open(
    f'./{DOMAIN}_{CERT_ID}_full_chain.pem', 'r'
) as file:
    certificate = file.read()


key = OpenSSL.crypto.load_privatekey(
    OpenSSL.crypto.FILETYPE_PEM, private_key
)
cert = OpenSSL.crypto.load_certificate(
    OpenSSL.crypto.FILETYPE_PEM, certificate
)

pkcs = OpenSSL.crypto.PKCS12()
pkcs.set_privatekey(key)
pkcs.set_certificate(cert)

with open(DOMAIN + '.pfx', 'wb') as file:
    file.write(pkcs.export(passphrase=password.encode('ASCII')))

print(f'Пароль к сертификату {DOMAIN}: {password}')
