from modules.psql.database import Database
db = Database()

def get_political_committee_by_slug_name(params):
    sql_params = [params['slug_name'] + '%']
    sql_stmt = '''select *
        from political_committees
        where slug_name ilike %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_political_committee_by_rid(params):
    sql_params = [params['registration_id']]
    sql_stmt = '''select *
        from political_committees
        where registration_id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

# TODO: get more data for prior committees
def touch_political_committee(params):
    insert_params = get_insert_params(params)
    result = db.touch_record(get_political_committee_by_rid, params, 'political_committees', insert_params)
    return result

def get_insert_params(params):
    keys = ['registration_id', 'name', 'slug_name']
    return db.get_parms(params, keys)
