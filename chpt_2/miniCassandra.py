# http://www.jiuzhang.com/solution/mini-cassandra/
# Cassandra这个数据结构有两个级别的键

# raw_key 类似于哈希值
# column_key
# column_value
# 现在要实现下面两个方法：

# 1.insert(raw_key, column_key, column_value)
# 2.query(raw_key, column_start, column_end) 返回一个列表

# Define
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MiniCassandra:

    def __init__(self):
        # do intialization if necessary
        self.table = dict()

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        # write your code here
        if raw_key not in self.table:
            self.table[raw_key] = {}
        self.table[raw_key][column_key] = column_value
        self.table[raw_key] = dict(sorted(self.table[raw_key].items(), key=lambda x : x[0]))
    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        # write your code here
        ret = []
        if raw_key not in self.table:
            return ret
        cols = self.table[raw_key]
        for key, value in cols.items():
            if key >= column_start and key <= column_end:
                ret.append(Column(key, value))
        return ret

def printRes(ret):
    print('[')
    for i in range(len(ret)):
        print('[' + ', '.join(map(str, ret[i])) + ']')
    print(']')

if __name__ == "__main__":
    miniCas = MiniCassandra()
    miniCas.insert("google", 1, "haha")
    ret = miniCas.query("google", 0, 1)
    printRes(ret)

