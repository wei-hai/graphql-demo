"""
Environment variables
"""
import os

# Environment
ENV = os.getenv("ENV", "development")
SERVICE_NAME = "backend"

# JWT
JWT_SECRET = os.getenv("JWT_SECRET", "secret")
JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET", "refresh_secret")
JWT_EXPIRATION = int(os.getenv("JWT_EXPIRATION", "3600"))
JWT_REFRESH_EXPIRATION = int(os.getenv("JWT_REFRESH_EXPIRATION", "86400"))

# Database
PRIMARY_DATABASE_URL = os.getenv(
    "PRIMARY_DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/dbname"
)
REPLICA_DATABASE_URL = os.getenv(
    "REPLICA_DATABASE_URL", PRIMARY_DATABASE_URL
)

# Instrument
SENTRY_DSN = "https://28ed46e0f403456091ee6b71ba29a272@o376446.ingest.sentry.io/5197268"
