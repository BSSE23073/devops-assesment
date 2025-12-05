from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379, socket_timeout=5)

@app.route('/')
def hello():
    try:
        redis.incr('hits')
        count = redis.get('hits').decode('utf-8')
        return f"Hello! I have been seen {count} times.\n"
    except Exception as e:
        return "Hello! (Database not connected yet, but App is running!)\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
