from modules.psql.database import Database
db = Database()

def get_contributions_by_id(params):
    sql_params = [params['source_id'], params['source_type'], params['target_id'], params['date'], params['amount']]
    sql_stmt = '''select *
        from contributions
        where source_id = %s
        and source_type = %s
        and target_id = %s
        and date = %s
        and amount = %s
        '''
    return db.run_query(sql_stmt, sql_params, 'one')

def upsert_contributions(params):
    upsert_params = get_upsert_params(params)
    result = db.upsert_record(get_contributions_by_id, params, 'contributions', upsert_params, 'id')
    return result

def get_upsert_params(params):
    keys = ['source_id', 'source_type', 'target_id', 'date', 'in_kind', 'in_kind_description', 'amount']
    return db.get_parms(params, keys)
