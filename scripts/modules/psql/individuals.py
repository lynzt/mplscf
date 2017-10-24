from modules.psql.database import Database
db = Database()

def get_individual_by_id(params):
    sql_params = [params['id']]
    sql_stmt = '''select *
        from individuals
        where id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

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
    keys = ['first_name', 'middle_name', 'last_name', 'slug_name', 'city', 'state', 'employer']
    return db.get_parms(params, keys)


def get_update_append_employer(params):
    sql_params = [params['value'], params['id']]
    sql_stmt = '''update individuals set employer = employer || %s
        where id = %s returning *'''
    return db.run_query(sql_stmt, sql_params, 'one')

# def get_update_append_field(params):
#     sql_params = [params['field'], params['field'], params['value'], params['id']]
#     sql_stmt = '''update individuals set %s = %s || %s
#         where id = %s returning *'''
#     return db.run_query(sql_stmt, sql_params, 'one')
