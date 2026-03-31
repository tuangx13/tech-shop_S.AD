-- PostgreSQL init script
-- Note: laptop_db is created by POSTGRES_DB in docker-compose.yml
-- This script creates additional databases

-- Create mobile_db if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mobile_db') THEN
        PERFORM dblink_exec('dbname=' || current_database(), 'CREATE DATABASE mobile_db');
    END IF;
END
$$;
