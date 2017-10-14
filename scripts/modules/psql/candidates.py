

from modules.psql.database import Database
db = Database()

def get_candidate_by_candidate_slug_name(params):
    sql_params = [params['committee_slug_name'] + '%']
    sql_stmt = '''select *
        from candidates
        where committee_slug_name ilike %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_candidate_by_rid(params):
    sql_params = [params['registration_id']]
    sql_stmt = '''select *
        from candidates
        where registration_id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def upsert_candidates(params):
    upsert_params = get_upsert_params(params)
    result = db.upsert_record(get_candidate_by_rid, params, 'candidates', upsert_params, 'registration_id')
    return result

def get_upsert_params(params):
    keys = ['registration_id', 'first_name', 'middle_name', 'last_name', 'slug_name', 'party', 'committee_name', 'committee_slug_name', 'office', 'district', 'last_pulled_at']
    return db.get_parms(params, keys)

def get_insert_params(params):
    keys = ['registration_id', 'committee_name', 'committee_slug_name']
    return db.get_parms(params, keys)

# TODO: get more data for prior candidates
def touch_candidate(params):
    insert_params = get_insert_params(params)
    result = db.touch_candidate(get_candidate_by_rid, params, 'candidates', insert_params, 'registration_id')
    return result

def get_candidates_to_check_contributions(params):
    sql_params = [params['limit']]
    sql_stmt = '''select * from candidates
        where slug_name is not null
        order by last_pulled_at desc, last_name, first_name
        limit %s'''
    return db.run_query(sql_stmt, sql_params)

def update_last_pulled_at(params):
    sql_params = [params['candidate_rid']]
    sql_stmt = '''update candidates set last_pulled_at = now()
        where registration_id = %s returning *'''
    return db.run_query(sql_stmt, sql_params, 'one')
