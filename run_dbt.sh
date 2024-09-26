#!/bin/bash
dbt run
psql -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO joseph;"
