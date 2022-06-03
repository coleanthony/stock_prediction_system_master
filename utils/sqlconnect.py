import pymysql
from sqlalchemy import create_engine

class mysql_conn(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='your passwd', db='stock', port=3306,charset='utf8')
        self.cursor = self.conn.cursor()
        self.engine = create_engine("{your engine}")

    # 执行modify(修改)相关的操作
    def execute_modify_mysql(self, sql):
        self.cursor.execute(sql)

    def execute_commit(self):
        self.conn.commit()

    def execute_select(self,sql):
        #查询是否含有该表
        result=[]
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __del__(self):
        # 魔术方法, 析构化 ,析构函数
        self.cursor.close()
        self.conn.close()