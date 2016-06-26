import redis
redisClient=redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
clients_machine_ip = []
clients_monitor_count = 0
