def dictfetchall(cursor):
    #Return all rows from a cursor as a dict
    rows = cursor.fetchall()
    desc = [item[0] for item in cursor.description]
    return [dict(zip(desc, item)) for item in rows]