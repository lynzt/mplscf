#!/usr/bin/python
import os
import psycopg2
import psycopg2.extras
import urllib

class Database:

    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        self._db_url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
        self._conn = self.init_db_conn()

        self._cur = self._conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        self._days_prior = 90


    def init_db_conn(self):
        try:
            conn = psycopg2.connect(
                database=self._db_url.path[1:],
                user=self._db_url.username,
                password=self._db_url.password,
                host=self._db_url.hostname,
                port=self._db_url.port
            )
            conn.autocommit = True
            return conn
        except:
            print ("I am unable to connect to the database.")

    def get_parms(self, params, keys):
        keys.append('created_at')
        keys.append('updated_at')
        return self.dict_comprehension(params, keys)

    def dict_comprehension(self, params, keys):
        return {key:value for key, value in params.items() if key in keys}

# todo: look at qrm for module or expand this...
    def run_query(self, sql, params, qrm=None):
        self._cur.execute(sql, params)
        if qrm == 'one':
            res = self._cur.fetchone()
        else:
            res = self._cur.fetchall()
        return res

    def touch_record(self, select_stmt, select_params, table_name, params):
        results = select_stmt(select_params)
        if results and len(results) > 0:
            return results
        else:
            return self.insert_table_row(table_name, params)

    def upsert_record(self, select_stmt, select_params, table_name, params, key_id):
        results = select_stmt(select_params)

        if results and len(results) > 0:
            # print ('results')
            # print (results)
            params['id'] = results['id']
            return self.update_table_row(table_name, key_id, params)
        else:
            return self.insert_table_row(table_name, params)

    def insert_table_row(self, table_name, table_details):
        sql_params = []
        sql_placeholders = '';
        sql_stmt = 'insert into %s (' % table_name

        for key, value in table_details.items():
            sql_stmt += key + ', '
            sql_placeholders += '%s, '
            sql_params.append(value)
        sql_stmt = str.rstrip(sql_stmt, ', ')
        sql_placeholders = str.rstrip(sql_placeholders, ', ')
        sql_stmt += ') values ('+ sql_placeholders +') returning *'

        print ("sql_stmt: %s" % sql_stmt)
        return self.run_query(sql_stmt, sql_params, 'one')

    def update_table_row(self, table_name, key_id, table_details):
        sql_params = []
        sql_stmt = 'update %s set ' % table_name

        id_to_use = table_details[key_id]
        table_details.pop(key_id, None)

        for key, value in table_details.items():
            if key == 'created_at':
                continue
            sql_stmt += key + ' = %s, '
            sql_params.append(value)
        sql_stmt = str.rstrip(sql_stmt, ', ')
        sql_stmt += ' where '+ key_id + ' = %s returning *'
        sql_params.append(id_to_use)
        return self.run_query(sql_stmt, sql_params, 'one')
