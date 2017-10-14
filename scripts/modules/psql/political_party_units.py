from modules.psql.database import Database
db = Database()

def get_political_party_unit_by_slug_name(params):
    sql_params = [params['slug_name'] + '%']
    sql_stmt = '''select *
        from political_party_units
        where slug_name ilike %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_political_party_unit_by_rid(params):
    sql_params = [params['registration_id']]
    sql_stmt = '''select *
        from political_party_units
        where registration_id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def touch_political_party_unit(params):
    insert_params = get_insert_params(params)
    result = db.upsert_record(get_political_party_unit_by_rid, params, 'political_party_units', insert_params)
    return result

def get_insert_params(params):
    keys = ['registration_id', 'name', 'slug_name', 'party']
    return db.get_parms(params, keys)
