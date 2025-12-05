# Use a lightweight python image
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Expose port 5000
EXPOSE 5000
CMD ["python", "app.py"]
