# http://lintcode.com/en/problem/memcache/
# 实现下列几个方法：
# 1.get(curtTime, key). 得到key的值，如果不存在返回2147483647
# 2.set(curtTime, key, value, ttl). 设置一个pair(key,value)，有效期从curtTime到curtTime + ttl -1 , 如果ttl为0，则一直存在
# 3.delete(curtTime, key). 删除这个key
# 4.incr(curtTime, key, delta). 给key的value加上delta，并且返回 如果不存在返回 2147483647。
# 5.decr(curtTime, key, delta). 给key的value减去delta，并且返回 如果不存在返回 2147483647。

MAX_INT = 2147483647

class Value:
    def __init__(self, value, time):
        self._value = value
        self._expireAt = time

class Memcache:
    def __init__(self):
        # do intialization if necessary
        # in dict, key, value is type of Value, containing
        self.map = dict()

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        # write your code here
        if key not in self.map:
            return MAX_INT
        value = self.map[key]
        if value._expireAt == -1 or curtTime <= value._expireAt:
            return value._value
        else:
            # if expired, return not-found
            return MAX_INT
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        # write your code here
        if ttl:
            value = Value(value, curtTime + ttl - 1)
        else:
            value = Value(value, -1)
        self.map[key] = value

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        # write your code here
        if key not in self.map:
            return
        else:
            del self.map[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        # write your code here
        # cannot use
        # if key not in self.map:
        # because key may in map but already expired
        if self.get(curtTime, key) == MAX_INT:
            return MAX_INT
        else:
            self.map[key]._value += delta
            return self.map[key]._value
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        # write your code here
        if self.get(curtTime, key) == MAX_INT:
            return MAX_INT
        else:
            self.map[key]._value -= delta
            return self.map[key]._value


if __name__ == "__main__":
    # WRITE SOME TEST CASES

