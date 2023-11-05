# Commands and utilities for postgresql

* For conection
  * sudo docker-compose exec db psql -U IagoLaura -d WhitePort
* When you are inside of the db:
  * To show relations
    * \dt
  * To execute a .sql file
    * \i /docker-entrypoint-initdb.d/table.sql
