__author__ = "richard.m"

# SQL functions

import pyodbc


def create_conn(driver, server, db_name, user="cordic", password="12345"):
    conn_str = str(
        "driver=" + driver + ";server=" + server + ";database=" + db_name + ";uid=" + user + ";pwd=" + password)
    connection = pyodbc.connect(conn_str, autocommit=True)
    cursor = connection.cursor()
    return cursor


def select(cursor, sql_from, sql_what="*"):
    sql_select = str("select " + sql_what + " from " + sql_from)
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    for row in rows:
        print row.sql_what


def update(cursor, sql_what, sql_set, sql_set_value, sql_where, sql_where_value):
    sql_update = str(
        "update " + sql_what + " set " + sql_set + "=" + sql_set_value + " where " + sql_where + "=" + sql_where_value)
    cursor.execute(sql_update)
    print cursor.rowcount, "lines updated"


def test_tc():
    cursor = create_conn('{SQL Server}', '.', 'Taxi1')
    try:
        select(cursor, 'asset')
        return True
    except:
        return False

if __name__ == "__main__":
    print "This is a helper, don't call explicitly"
    raw_input("Press Enter to exit")