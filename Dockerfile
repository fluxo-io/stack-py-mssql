FROM python:3.11-slim

# EULA automatisch akzeptieren + Noninteractive Mode aktivieren
ENV ACCEPT_EULA=Y
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gnupg2 ca-certificates apt-transport-https \
    unixodbc unixodbc-dev build-essential && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/ms.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ms.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
      > /etc/apt/sources.list.d/microsoft.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    msodbcsql18 mssql-tools18 && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/mssql-tools18/bin:${PATH}"
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]