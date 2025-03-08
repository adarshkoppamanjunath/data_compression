# Use an official lightweight Python image
FROM python:3.11-slim
WORKDIR /app
COPY  . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "test_data_compression.py", "--tb=line", "--disable-warnings"]
