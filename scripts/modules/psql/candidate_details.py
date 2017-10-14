from modules.psql.database import Database
db = Database()

def get_candidate_details_by_id(params):
    sql_params = [params['id']]
    sql_stmt = '''select *
        from candidate_details
        where id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def upsert_candidate_details(params):
    upsert_params = get_upsert_params(params)
    result = db.upsert_record(get_candidate_details_by_id, params, 'candidate_details', upsert_params, 'id')
    return result

def get_upsert_params(params):
    keys = ['id', 'party', 'committee_name', 'office', 'district']
    return db.get_parms(params, keys)
