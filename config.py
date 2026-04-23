

# Author: Zirwa Omar
# Date: 2026-04-23
# Purpose: Database configuration for Sakila Flask Application
#
# Author: Team Member: Sana Lone
# Date: 2026-04-23
# Purpose: Health check configuration merged from feature/add-healthcheck
# Version: 1.1 - Added input validation for timeout variables


import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

try:
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
except ValueError:
    CONNECTION_TIMEOUT = 30

try:
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
except ValueError:
    HEALTH_CHECK_INTERVAL = 10