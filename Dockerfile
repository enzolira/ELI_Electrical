FROM python:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4000
CMD python ./server.py

