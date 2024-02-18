import redis

# Redis连接参数
redis_config = {"host": "127.0.0.1", "port": 6379, "password": "", "db": 0}

# 连接到Redis
r = redis.Redis(**redis_config)

# 获取哈希表中键值对的数量
item_dict = r.hgetall("use_proxy")
print(item_dict.values())