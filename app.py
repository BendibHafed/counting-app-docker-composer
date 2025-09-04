import time
import redis
from flask import Flask
import os

app = Flask(__name__)

# Configuration automatique
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

print(f"Connecting to Redis at {redis_host}:{redis_port}")

cache = redis.Redis(
    host=redis_host,
    port=redis_port,
    socket_connect_timeout=5,
    socket_timeout=5,
    decode_responses=True
)

def get_hit_count():
    retries = 5
    while retries > 0:
        try:
            return cache.incr('hit')
        except redis.exceptions.ConnectionError as exc:
            retries -= 1
            if retries == 0:
                raise exc
            time.sleep(0.5)
    return 0

@app.route("/")
def hello():
    try:
        count = get_hit_count()
        return f"You have visited me {count} times."
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    try:
        cache.ping()
        print("Connected to Redis successfully!")
    except Exception as e:
        print(f"Redis connection failed: {e}")
    
    app.run(host="0.0.0.0", port=5000, debug=True)
else:
    # Gunicorn use or others
    print("Flask app loaded in production mode")