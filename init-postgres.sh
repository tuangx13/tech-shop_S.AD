#!/bin/bash
set -e

# Create mobile_db database
# laptop_db is already created by POSTGRES_DB environment variable
psql -v ON_ERROR_STOP=0 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE mobile_db;
EOSQL

echo "PostgreSQL databases initialized successfully"
