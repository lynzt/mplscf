from modules.psql.database import Database
db = Database()

def get_alternate_name_by_slug(params):
    sql_params = [params['slug_name']]
    sql_stmt = '''select *
        from alternate_names
        where slug_name = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_alternate_name_by_rid(params):
    sql_params = [params['registration_id']]
    sql_stmt = '''select *
        from alternate_names
        where registration_id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_insert_params(params):
    keys = ['registration_id', 'name', 'slug_name']
    return db.get_parms(params, keys)

# TODO: get more data for prior alternate_names
def touch_alternate_name(params):
    insert_params = get_insert_params(params)
    result = db.touch_record(get_alternate_name_by_slug, params, 'alternate_names', insert_params)
    return result
