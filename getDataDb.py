
def get_data_from_rds(conn):
    with conn.cursor() as cur:
        cur.execute("")
        rows = cur.fetchall()
        str = None
        for row in rows:
            print(row[0]+', '+row[1]+', '+row[2]+', '+row[3])
            str = row[0]+', '+row[1]+', '+row[2]+', '+row[3]

        return str
    