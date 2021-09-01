# 操作数据库类
import pymysql
from config.settings import db_cfg


class mysqlUtil:
    # 初始化参数
    def __init__(self, my_cfg=db_cfg):
        self.db_cfg = my_cfg
        self.connection = 0

    # 建立连接
    def connect_db(self):
        try:
            self.db = pymysql.connect(**self.db_cfg)
        except pymysql.Error as e:
            print(e)
            print('error with connect_db')
        else:
            self.connection = 1
            return self.db

    # 获得游标对象
    def get_cur(self):
        try:
            self.connect_db()
            self.cursor = self.db.cursor()
        except pymysql.Error as e:
            print(e)
            print('error with get_cur')
        else:
            return self.cursor

    # 关闭连接
    def close_db(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
        except pymysql.Error as e:
            print(e)
            print('error with close_db')
        else:
            self.connection = 0
            return True

    # 增数据一条
    def insert_one(self, sql, *value):
        try:
            handler = self.get_cur()
            res = handler.execute(sql, *value)
            self.db.commit()
        except pymysql.Error as e:
            self.cursor.rollback()   # 如果有错误，就回滚
            print(e)
            print('error with insert')
        else:
            self.close_db()
            return res

    # 增数据批量
    def insert_lots(self, sql, *value):
        return "unfinished function"
        try:
            handler = self.get_cur()
            res = handler.execute(sql, *value)
            self.db.commit()
        except pymysql.Error as e:
            # self.handler.commit()   # 如果上面的提交有错误，那么只执行对的那一个提交
            self.cursor.rollback()   # 如果有错误，就回滚
            print(e)
            print('error with insert')
        else:
            self.close_db()
            return res

    # 查数据一条
    def select_one(self, sql, *value):
        return "unfinished function"
        handler = self.get_cur()
        handler.execute(sql, *value)
        res = handler.fetchone()
        self.db.commit()
        self.close_db()
        return res

    # 查数据列表
    def select_list(self, sql, *value):
        return "unfinished function"
        handler = self.get_cur()
        handler.execute(sql, *value)
        res = curses.fetchall()
        self.db.commit()
        self.close_db()
        return res

    # 更新数据
    def update(self, sql, *value):
        return "unfinished function"
        handler = self.get_cur()
        res = handler.excute(sql, *value)
        self.db.commit()
        self.close_db()
        return res

    # 删除数据
    def delete(self, sql, *value):
        return "unfinished function"
        handler = self.get_cur()
        res = handler.excute(sql, *value)
        self.db.commit()
        self.close_db()
        return res


if __name__ == "__main__":
    # print(db_cfg)
    db = mysqlUtil()

    # print(db.db_cfg)
    db.get_cur()
    print(db.cursor)
    print(db.connection)
    db.close_db()
    print(db.connection)
    # print(db.update())
