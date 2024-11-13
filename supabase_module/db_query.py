from .supabase_config import supabase


def insert(table_name, data):
    try:
        response = (
            supabase.table(table_name)
            .insert(data)
            .execute()
        )
        return response.json()
    except Exception as e:
        print('db error:', e)
        return {'error': str(e)}


def get_all(table_name):
    try:
        response = (
            supabase.table(table_name)
            .select('*')
            .execute()
        )
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}


def get_by_column(table_name, params):
    '''
    params is dict of column_name and value
    '''
    try:
        query = supabase.table(table_name).select('*')
        for column_name, value in params.items():
            query = query.eq(column_name, value)

        response = query.execute()
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}


def update(table_name, params, data):
    '''
        params is dict of column_name and value
    '''
    try:

        query = supabase.table(table_name).update(data)
        for column_name, value in params.items():
            query = query.eq(column_name, value)

        response = query.execute()
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}


def filter_by_date_range(table_name, params, filter):
    '''
    params is dict of column_name and value
    filter is list of start_date and end_date
    '''
    try:
        query = supabase.table(table_name).select('*')
        for column_name, value in params.items():
            query = query.eq(column_name, value)
        query = query.gte(filter['column'],  filter['start'])
        query = query.lte(filter['column'],  filter['end'])

        response = query.execute()
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}
