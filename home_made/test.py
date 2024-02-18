import redis

# Redis连接参数
redis_config = {"host": "127.0.0.1", "port": 6379, "password": "", "db": 0}

# 连接到Redis
r = redis.Redis(**redis_config)

# 获取数据量
data_size = r.dbsize()
print("Total number of keys in the Redis database:", data_size)