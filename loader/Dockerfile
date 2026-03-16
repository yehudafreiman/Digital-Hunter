FROM python:3.10
WORKDIR /app
COPY loader/requirements.txt .
RUN pip install -r requirements.txt
COPY shared ./shared
COPY loader .
CMD ["python", "loader.py"]
