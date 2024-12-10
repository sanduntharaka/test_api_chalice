from chalicelib.supabase_module.supabase_config import supabase


def insert(table_name, data):
    response = (
        supabase.table(table_name)
        .insert(data)
        .execute()
    )
    return response.json()


def get_all(table_name):
    response = (
        supabase.table(table_name)
        .select('*')
        .execute()
    )
    return response.json()


def get_by_column(table_name, params):
    '''
    params is dict of column_name and value
    '''
    query = supabase.table(table_name).select('*')
    for column_name, value in params.items():
        query = query.eq(column_name, value)

    response = query.execute()
    return response.json()


def update(table_name, params, data):
    '''
        params is dict of column_name and value
    '''

    query = supabase.table(table_name).update(data)
    for column_name, value in params.items():
        query = query.eq(column_name, value)

    response = query.execute()
    return response


def filter_by_range(table_name, params, filter):
    '''
    params is dict of column_name and value
    filter is list of start and end
    '''
    query = supabase.table(table_name).select('*')
    for column_name, value in params.items():
        query = query.eq(column_name, value)
    query = query.gte(filter['column'],  filter['start'])
    query = query.lte(filter['column'],  filter['end'])

    response = query.execute()
    return response.json()


def call_function(function_name, params):
    response = (
        supabase.rpc(function_name, params)
        .execute()
    )
    return response
