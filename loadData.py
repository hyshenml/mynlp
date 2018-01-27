# -*- coding: utf-8 -*-
import MySQLdb
import pandas

class MyDb():
    def __enter__(self):
        self.conn=MySQLdb.connect(host="localhost",user="sml",passwd="91004",db='huxiu',charset="utf8")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

def load_articles():
    l=[]
    with MyDb() as conn:
        sql="select * from articleItem limit 1000";
        c=conn.cursor()
        c.execute(sql)
        for row in c.fetchall():
            try:
                row=list(row)
                l.append(row)
            except ValueError,e:
                print e
    df=pandas.DataFrame(l,columns=['title','comment_num','store_num','text','time','author_id'])

    return df


