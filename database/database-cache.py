import redis
import json
import time

r = redis.Redis(host='127.0.0.1', port=6379, password='0gj9VMMpJh/dW6QZz5H9Qmc95u7Rhl8OJyScKVNBs6CeAmPp4kDi68pXpcJL+YdGR1SUsUpGz/3hvtgT', db=0)

def schedule_row_cache(conn, row_id, delay):

	conn.zadd('delay:', row_id, delay)

	conn.zadd('schedule:', row_id, time.time())


def cache_rows(conn):
	while not QUIT:

		next = conn.zrange('schedule:', 0, 0, withscores=True)


		now = time.time()
		if not next or next[0][1] > now:

			time.sleep(.05)


			continue

		row_id = next[0][0]

		delay = conn.zscore('delay:', row_id)


		if delay <= 0:

			conn.zrem('delay:', row_id)
			conn.zrem('schedule:', row_id)
			conn.delete('inv:' + row_id)


			continue

		row = Inventory.get(row_id)


		conn.zadd('schedule:', row_id, now + delay)
		conn.set('inv:' + row_id, json.dumps(row.to_dict()))

