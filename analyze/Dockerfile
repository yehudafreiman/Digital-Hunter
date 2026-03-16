FROM python:3.10
WORKDIR /app
COPY analyze/requirements.txt .
RUN pip install -r requirements.txt
COPY shared ./shared
COPY analyze .
CMD ["python", "analyze.py"]