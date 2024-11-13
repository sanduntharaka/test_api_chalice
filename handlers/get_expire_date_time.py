from datetime import datetime, timedelta


def get_expire_datetime(date):
    initial_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    end_date_time = initial_datetime + timedelta(days=30)

    return end_date_time.strftime("%Y-%m-%d %H:%M:%S.%f")
