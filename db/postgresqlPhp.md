postgresqlPhp.md  
docker run --name postgres -e POSTGRESQL_ADMIN_PASSWORD=mysecretpassword -d -p 5432:5432 centos/postgresql-95-centos7
docker exec -it postgres bash  
docker logs postgres  
###### quit cmd
\q
###### login
```
psql --username=tom --password --dbname=jerry
sudo -i -u postgres
sudo - postgres
passwd postgres
psql -d postgres
```
TARMS_DB_20171215=#
psql -U postgres  //psql: FATAL:  ユーザ "postgres" で対向(peer)認証に失敗しました
###### list user
```
\du
CREATE USER srs WITH PASSWORD 'myPassword';
CREATE USER cube3_dev_user WITH PASSWORD 'password';
CREATE DATABASE cube3_dev;
GRANT ALL PRIVILEGES ON DATABASE cube3_dev to cube3_dev_user;
ALTER USER user_name WITH PASSWORD 'new_password';
ALTER USER postgres WITH PASSWORD 'password';

```

###### list tables
list db
```
\l
```
\d  
\d tbname  
###### view current db name
```
\c
```
\conninfo
psql -d template1
psql template1
psql -d postgres
psql postgres

CREATE DATABASE my_app;  
CREATE USER my_app WITH PASSWORD 'secret';  
pg_dump dbname > outfile  
pg_restore -d dbname backupfilename  

SELECT table_name as name FROM INFORMATION_SCHEMA.tables WHERE table_schema = 'public'

\dt public.dir_users;

ALTER SCHEMA name RENAME TO new_name
ALTER SCHEMA name OWNER TO new_owner

select schema_name from information_schema.schemata
result with: public
\dn list schema;

postgresql.x86_64 0:9.2.23-3.el7_4
```
yum install postgresql-server postgresql-contrib
postgresql-setup initdb
vi /var/lib/pgsql/data/pg_hba.conf
systemctl restart postgresql
```
set host ident to md5 and set host 127.0.0.1-> 0.0.0.0/0
```
systemctl start postgresql
systemctl restart postgresql
systemctl enable postgresql
sudo -i -u postgres
sudo - postgres
```
switch user to postgres

```
yum install postgresql
which psql
```
FATAL: Peer authentication failed for user "postgres"
    pg_ctl -D /var/lib/pgsql/data/userdata -l logfile start
cat -n /var/lib/pgsql/data/postgresql.conf | grep listen_addresses

vi /var/lib/pgsql/data/postgresql.conf
change
listen_addresses = 'localhost'
to 
listen_addresses = '*'
