
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DEFAULT_TIMEOUT=180
ENV PIP_RETRIES=5

COPY requirements.txt .

RUN pip install --no-cache-dir --retries 5 --timeout 180 -r requirements.txt \
    && pip install --no-cache-dir --retries 5 --timeout 180 gunicorn

COPY . .

RUN sed -i 's/\r$//' /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh \
    && mkdir -p /app/instance

EXPOSE 5000

CMD ["sh", "entrypoint.sh"]
