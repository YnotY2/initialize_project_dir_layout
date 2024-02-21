import os

# Database PostgreSQL Credentials
postgresql_db_name = os.getenv("postgresql_db_name","<name_here>")
postgresql_db_passwd = os.getenv("postgresql_db_passwd", "<passwd_here>")
postgresql_db_usr = os.getenv("postgresql_db_usr", "<user_here>")
postgresql_port = os.getenv("postgresql_port", "5432")      # Default port// Change if wanted
postgresql_host = os.getenv("postgresql_host", "localhost")      # Locally hosted db// Change if wanted

# Other credentials
