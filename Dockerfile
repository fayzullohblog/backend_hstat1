FROM python:3.11

# Install wkhtmltopdf from the alpine-wkhtmltopdf image

RUN set -e; \
        apk add --no-cache mariadb-connector-c-dev ;\
        apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        mariadb-dev \
        jpeg-dev \
        zlib-dev \
        libffi-dev \
        musl-dev \
        libxml2-dev \
        libxslt-dev \
        wkhtmltopdf \
        poppler-utils;
COPY DockerVue/wkhtmltopdf /usr/bin/wkhtmltopdf
COPY DockerVue/wkhtmltoimage /usr/bin/wkhtmltoimage



RUN set -e; \
    pip install --upgrade pip; \
    pip install -r requirements.txt;
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate

# Uncomment these lines if needed for collecting static files
# RUN mkdir -p /app/staticfiles
# RUN python manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
