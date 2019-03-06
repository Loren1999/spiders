#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb as mysql


def main():
    count = 0
    # 打开数据库连接
    con = mysql.connect(host="localhost", user="root", passwd="password", db="spiders", charset="utf8")
    # 获取操作游标
    cursor = con.cursor()
    # 获取所有记录列表并去重
    sql = "SELECT content FROM content;"
    cursor.execute(sql)
    results = list(tuple(set(cursor.fetchall())))
    print("总数据量{}".format(len(results)))
    # 清空表中所有内容
    del_sql = "truncate table content;"
    cursor.execute(del_sql)
    # 拼装SQL，开始批量插入
    for row in results:
        ins_sql = "INSERT INTO content(content) VALUE('{}')".format(row[0])
        # print(ins_sql)
        cursor.execute(ins_sql)
        con.commit()
        count += 1

    print("总共插入{}条数据".format(count))
    cursor.close()
    con.close()


if __name__ == '__main__':
    main()
