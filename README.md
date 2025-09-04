#  Simple Counting App – Dev & Prod Docker Guide

This project runs a Flask + Redis app using Docker Compose, with separate files for development and production.

---

## How to Run

### Development Mode

```bash
docker compose -f docker-compose.dev.yaml up --build
```
- Uses python app.py
- Enables debug=True
- Connects to Redis via service name
- Optional: hot reload if using flask run

### Production Mode
```bash
docker compose -f docker-compose.yml up --build
```
- Uses Gunicorn (CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"])
- Runs in multi-worker mode
- Logs to stdout
- Optimized for container lifecycle
### Project Structure
.
├── app.py </br>
├── Dockerfile </br>
├── requirements.txt </br>
├── docker-compose.yml </br>        # Production
├── docker-compose.dev.yaml </br>   # Development
└── entrypoint.sh </br>             # Optional: switches modes

### Redis Setup
Redis runs as a service in both modes
Flask connects using:
bash```
redis.Redis(host=os.getenv("REDIS_HOST", "localhost"))
```

🧪 Common Issues
Problem           	          Fix 
ModuleNotFoundError	          Check import paths in app.py
Container exits immediately	  Use correct CMD or entrypoint
Redis not reachable	Retry     logic or depends_on

