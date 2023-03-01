FROM python:3.10-buster

ENV PYTHONUNBUFFERED 1
ENV USER=project

RUN addgroup project \
    && adduser --system --no-create-home --disabled-password --disabled-login -q --ingroup project project

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY --chown=${USER}:${USER} . /app
RUN mkdir -p /certificate_folder/
RUN chown -R project:project /app /certificate_folder

USER project
WORKDIR /app

CMD [ "python", "update_certificate.py" ]