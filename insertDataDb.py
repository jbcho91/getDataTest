
def insert_data_to_rds(conn, data):
    with conn.cursor() as cur:
        insert_query = """
        INSERT INTO your_table_name (property_id, name, url) 
        VALUES (%s, %s, %s)
        """
        for property in data['data']['rows']:
            cur.execute(insert_query, (
                property['propertyId'],
                property['name'],
                property['url']
            ))
        conn.commit()