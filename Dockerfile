FROM python:3.11
RUN wget https://s3.amazonaws.com/shopify-managemant-app/wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN tar xvjf wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN mv wkhtmltopdf-amd64 /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

WORKDIR /app

COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate



EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
