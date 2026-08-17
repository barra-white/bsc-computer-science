# Weather Forecast App

Lab 2 — Cloud Infrastructure & Services (CS3204), Year 3, BSc Computer Science.

A Flask app that pulls a Met Éireann weather forecast (XML), parses and aggregates it by day, stores the results in a MySQL database, and renders them as an HTML table.

## Setup

The app reads its database connection from environment variables:

```bash
export DB_HOST=your-db-host
export DB_USER=your-db-user
export DB_PASSWORD=your-db-password
pip install -r requirements.txt
```

## Usage

```bash
python3 application.py
```
