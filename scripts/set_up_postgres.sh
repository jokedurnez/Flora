# https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi

sudo apt install -y postgresql libpq-dev postgresql-client postgresql-client-common

sudo su postgres
createuser pi -P --interactive
psql -c "create database flora;"
exit

psql -d flora -c "create table metrics (datetime timestamp, acc_x double precision, acc_y double precision, acc_z double precision);"
