from modules.psql.database import Database
db = Database()

def get_contributions_by_id(params):
    sql_params = [params['date'], params['source_id'], params['target_id'], params['amount']]
    sql_stmt = '''select *
        from contributions
        where date = %s
        and source_id = %s
        and target_id = %s
        and amount = %s
        '''
    return db.run_query(sql_stmt, sql_params, 'one')

def upsert_contributions(params):
    upsert_params = get_upsert_params(params)
    result = db.upsert_record(get_contributions_by_id, params, 'contributions', upsert_params, 'id')
    return result

def get_upsert_params(params):
    keys = ['source_id', 'target_id', 'date', 'in_kind', 'in_kind_description', 'amount']
    return db.get_parms(params, keys)
