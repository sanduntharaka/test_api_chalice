from .supbase_config import supabase
import json


def insert_data(table_name, data):
    try:
        response = (
            supabase.table(table_name)
            .insert(data)
            .execute()
        )
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}


def get_all_data(table_name):
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


def get_data_by_id(table_name, column_name, value):
    try:
        response = (
            supabase.table(table_name)
            .select('*')
            .eq(column_name, value)
            .execute()
        )
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}


def update_table_data(table_name, column_name, value, data):
    try:
        response = (
            supabase.table(table_name)
            .update(data)
            .eq(column_name, value)
            .execute()
        )
        return response.json()
    except Exception as e:
        print(e)
        return {'error': str(e)}
