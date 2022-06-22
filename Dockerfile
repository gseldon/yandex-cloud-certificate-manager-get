FROM bitnami/python:3.10

ENV PYTHONUNBUFFERED 1

RUN addgroup project \
    && adduser --system --no-create-home --disabled-password --disabled-login -q --ingroup project project

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./app /app
RUN mkdir -p /certificate_folder/
RUN chown -R project:project /app /certificate_folder

USER project
WORKDIR /app

CMD [ "python", "update_certificate.py" ]