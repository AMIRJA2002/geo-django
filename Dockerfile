FROM python:3.12.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# Install GDAL and other dependencies
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . /app

ENV GDAL_DATA /usr/share/gdal

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py runserver 0.0.0.0:8000
