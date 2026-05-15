FROM python:3.13.9-slim
WORKDIR /salary-app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/ ./src/
COPY models/ ./models/

EXPOSE 5000

CMD ["python", "src/app.py"]