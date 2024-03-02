FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate

# RUN mkdir -p /app/staticfiles

# RUN python manage.py collectstatic --noinput --clear

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]