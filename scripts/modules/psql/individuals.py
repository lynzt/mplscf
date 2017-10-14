from modules.psql.database import Database
db = Database()

def get_individual_by_slug_name(params):
    sql_params = [params['slug_name']]
    sql_stmt = '''select *
        from individuals
        where slug_name = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def touch_individual(params):
    insert_params = get_insert_params(params)
    result = db.touch_record(get_individual_by_slug_name, params, 'individuals', insert_params)
    return result

def get_insert_params(params):
    keys = ['first_name', 'middle_name', 'last_name', 'slug_name', 'city', 'state', 'employer', 'is_lobbyist']
    return db.get_parms(params, keys)
