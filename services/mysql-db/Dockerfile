FROM mysql:latest

# Optionally, you can specify additional configuration files or scripts
# COPY custom-config-file.cnf /etc/mysql/conf.d/

# Optionally, you can run SQL scripts to initialize the database
COPY migration/init.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
