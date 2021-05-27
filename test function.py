import pandas as pd
import sqlite3


def cal_cost(job_id):
    #calculates total cost of job when given job ID
    sql_connect=sqlite3.connect('job_data.db')
    cursor=sql_connect.cursor()
    query = select
    assert isinstance(job_id, object)
    job_id from object
    results = cursor.execute(query)
    if scrap in results is aluminum:
        scrap_val= weight*20
    else:
        scrap_val = weight*10
    time = man_hours in results
    total= time + scrap_val

    print(total)