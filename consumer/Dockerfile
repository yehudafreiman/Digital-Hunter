FROM python:3.10
WORKDIR /app
COPY consumer/requirements.txt .
RUN pip install -r requirements.txt
COPY shared ./shared
COPY consumer ./consumer
CMD ["python", "consumer.py"]