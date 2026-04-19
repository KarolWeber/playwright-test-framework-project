FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"]