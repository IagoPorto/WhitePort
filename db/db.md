# Commands and utilities for postgresql

* For connection
  * sudo docker-compose exec db psql -U IagoLaura -d WhitePort
* When you are in PostgreSQL:
  * To show relations
    * \dt
  * To show a especific table
    * \d <table_name>
  * To execute a .sql file
    * \i /docker-entrypoint-initdb.d/table.sql
