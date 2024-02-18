import redis

# Redis连接参数
redis_config = {"host": "127.0.0.1", "port": 6379, "password": "", "db": 0}

# 连接到Redis
r = redis.Redis(**redis_config)

# 获取数据量
value = r.get("use_proxy")
print("Value of 'use_proxy' key in Redis:", value)