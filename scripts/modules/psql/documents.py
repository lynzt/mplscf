from modules.psql.database import Database
db = Database()

def get_documents_by_name(params):
    sql_params = [params['name'] + '%']
    sql_stmt = '''select *
        from documents
        where name ilike %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_documents_by_candidate_id(params):
    sql_params = [params['candidate_id']]
    sql_stmt = '''select *
        from documents
        where candidate_id = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def get_documents_by_id_name(params):
    sql_params = [params['candidate_id'], params['name']]
    sql_stmt = '''select *
        from documents
        where candidate_id = %s
        and name = %s'''
    return db.run_query(sql_stmt, sql_params, 'one')

def touch_documents(params):
    insert_params = get_insert_params(params)
    result = db.upsert_record(get_documents_by_id_name, params, 'documents', insert_params, 'id')
    return result

def get_insert_params(params):
    keys = ['candidate_id', 'name', 'href', 'file_path']
    return db.get_parms(params, keys)
