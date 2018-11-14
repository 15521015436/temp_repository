import pymysql
import sys


def connect_database():
    try:
        conn = pymysql.connect(host='14.152.59.237', port=1296, user='yf133',
                               passwd='hyyQzeOB0OKpSbCf', db='spotphoto', charset='utf8')
        return conn
    except Exception:
        print("connect failed, program exit")
        sys.exit(0)


def execute(conn, sql_cmd):
    print(sql_cmd)
    cur = conn.cursor()
    cur.execute(sql_cmd)
    data = cur.fetchall()
    cur.close()
    return data


if __name__ == "__main__":
    db = connect_database()
    data_recall = execute(db, 'select * from spot_list')
    print('sql select length: ', len(data_recall))
    url_list = []
    for i in range(len(data_recall)):
        # prefix of url(fourth index)
        url = str(data_recall[i][4])
        # postfix of url(fifth index)
        sub_url_list = str(data_recall[i][5]).split(',')
        for t in sub_url_list:
            url_list.append(url+t)
    print(url_list)
