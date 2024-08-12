import json
from connection import connect_to_rds
from getDataDb import get_data_from_rds
from getRedfin import fetch_redfin_data


def main():
    # RDS 연결
    conn = connect_to_rds()

    try:
        # RDS에서 데이터 가져오기
        fromDb = get_data_from_rds(conn)

        # Redfin API 데이터 가져오기
        redfin_data = fetch_redfin_data(fromDb)
        title = "redfin_data_with_db.txt"
        with open(title, "w") as file:
                json.dump(redfin_data, file, indent=4)
        # RDS에 데이터 넣기
        #insert_data_to_rds(conn, redfin_data)
    
    finally:
        # 연결 종료
        conn.close()

# 실행
main()