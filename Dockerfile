FROM python:3.11

# Install required dependencies for wkhtmltopdf
RUN apk update && apk add --no-cache \
    ca-certificates \
    fontconfig \
    libjpeg \
    libpng \
    libressl-dev \
    libwebp \
    libxcb \
    libxml2 \
    libxslt \
    libgcc \
    libstdc++ \
    libx11 \
    libxrender \
    libxext \
    ttf-dejavu \
    ttf-droid \
    ttf-freefont \
    ttf-liberation \
    ttf-ubuntu-font-family \
    wkhtmltopdf

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
