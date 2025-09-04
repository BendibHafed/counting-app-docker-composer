FROM python:3.12-alpine
WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Ajoutez cette ligne pour exposer le port
EXPOSE 5000

# Add entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]